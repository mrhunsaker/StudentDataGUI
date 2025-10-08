#!/usr/bin/env python3
"""
Shared artifact utilities for StudentDataGUI.

This module centralizes:
  - Student name sanitization for filesystem safety
  - Conversion / normalization of part score structures
  - Writing CSV artifacts (horizontal or vertical layouts)
  - Writing JSON snapshot artifacts
  - A unified write_session_artifacts() entry point

Intent (Option 2 of the refactor plan):
  Keep existing page logic (DB interactions remain in each page),
  but consolidate repeated CSV/JSON/file path logic here.

Database Schema Alignment:
  The database schema (tables: Student, ProgressType, ProgressSession,
  AssessmentPart, AssessmentResult, etc.) is NOT modified here.
  These helpers only persist derivative artifacts (CSV / JSON / HTML) in
  the filesystem under APP_HOME / StudentDataFiles / <SanitizedStudentName>.

Layouts:
  - "horizontal":
      One row per session with columns:
        date, code1, code2, ..., codeN
      (Mirrors current Abacus & Digital Literacy style.)
  - "vertical":
      One row per part per session with columns:
        student, date, code, score, notes
      (Matches current Braille & ScreenReader style.)

Usage Pattern:
  from StudentDataGUI.appHelpers.artifacts import write_session_artifacts
  write_session_artifacts(
      base_dir=APP_HOME,
      student_name=raw_name_from_ui,
      date_val="2025-01-15",
      part_scores={"P1_1": 2, "P1_2": 3, ...}  # OR {"P1_1": (part_id, 2), ...}
      notes="optional",
      prefix="Abacus",        # will generate CSV name like AbacusSkillsProgression.csv
      layout="horizontal"     # or "vertical"
  )

Returned Value:
  A dict containing absolute Path objects (as strings) to created/updated artifacts.

Thread / Concurrency Note:
  For multi-user scenarios, naive appends to CSV can interleave.
  A simple advisory file lock is provided (POSIX only). On non-POSIX platforms,
  the lock is a no-op to preserve compatibility.

Author: Refactor helper (Option 2)
"""

from __future__ import annotations

import json
import os
import re
import datetime
from pathlib import Path
from contextlib import contextmanager
from typing import Dict, Tuple, Iterable, Literal, Any

# Attempt to import fcntl for advisory locking (POSIX). Graceful fallback if unavailable.
try:
    import fcntl  # type: ignore

    _HAVE_FCNTL = True
except Exception:  # pragma: no cover
    _HAVE_FCNTL = False

# Public exports
__all__ = [
    "sanitize_student_name",
    "normalize_part_scores",
    "write_session_artifacts",
    "ArtifactPaths",
]

LayoutType = Literal["horizontal", "vertical"]


class ArtifactPaths(Dict[str, str]):
    """
    Simple dictionary subclass used as a semantic return type for
    write_session_artifacts. Keys:
      - student_dir
      - csv_path
      - json_path (if include_json=True)
    Additional keys may be added in the future (e.g., html_path).
    """

    pass


# ---------------------------------------------------------------------------
# Name Sanitization
# ---------------------------------------------------------------------------

_SANITIZE_PATTERN = re.compile(r'[<>:"/\\|?*\x00-\x1f]+')


def sanitize_student_name(name: str) -> str:
    """
    Normalize and sanitize a student name for safe directory usage.
    - Collapses internal whitespace
    - Strips leading/trailing spaces & dots
    - Replaces reserved / unsafe characters with underscores

    Parameters
    ----------
    name : str
        Raw student name from UI or input.

    Returns
    -------
    str
        A cleaned, filesystem-safe name.
    """
    cleaned = " ".join(name.split()).strip().strip(".")
    cleaned = _SANITIZE_PATTERN.sub("_", cleaned)
    # Avoid empty directory names if user entered only invalid chars
    return cleaned or "Unknown_Student"


# ---------------------------------------------------------------------------
# Part Score Normalization
# ---------------------------------------------------------------------------


def normalize_part_scores(part_scores: Dict[str, Any]) -> Dict[str, int]:
    """
    Normalize part_scores into a dict[str, int].

    Acceptable inputs:
      - { code: score_int }
      - { code: (part_id:int, score_int) }
      - { code: [part_id, score_int] }

    Raises
    ------
    ValueError
        If a score cannot be interpreted as an int.

    Returns
    -------
    dict[str, int]
        Mapping of part code -> score.
    """
    normalized: Dict[str, int] = {}
    for code, value in part_scores.items():
        if isinstance(value, tuple) and len(value) == 2:
            _, score = value
        elif isinstance(value, list) and len(value) == 2:
            _, score = value
        else:
            score = value
        try:
            normalized[code] = int(score)
        except Exception as e:
            raise ValueError(f"Invalid score for part '{code}': {value}") from e
    return normalized


# ---------------------------------------------------------------------------
# File Locking Helpers (Advisory)
# ---------------------------------------------------------------------------


@contextmanager
def _locked_file(path: Path, mode: str):
    """
    Context manager providing an advisory lock for writes.

    On POSIX, applies fcntl.LOCK_EX for exclusive locking.
    On non-POSIX platforms or if fcntl is unavailable, acts as a normal open().

    Parameters
    ----------
    path : Path
        The file path to open.
    mode : str
        File open mode, e.g. 'a', 'w', 'r+'.

    Yields
    ------
    file object
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    f = open(path, mode, newline="", encoding="utf-8")
    try:
        if _HAVE_FCNTL and "w" in mode or "a" in mode:
            try:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            except Exception:
                # Fallback silently if locking fails
                pass
        yield f
    finally:
        if _HAVE_FCNTL:
            try:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            except Exception:
                pass
        f.close()


# ---------------------------------------------------------------------------
# CSV Writers
# ---------------------------------------------------------------------------


def _write_csv_horizontal(
    csv_path: Path, date_val: str, scores: Dict[str, int]
) -> None:
    """
    Append a single horizontal session row to CSV.

    Header row written if file does not exist:
      date, code1, code2, ..., codeN
    """
    write_header = not csv_path.exists()
    ordered_codes = list(scores.keys())
    with _locked_file(csv_path, "a") as f:
        if write_header:
            f.write(",".join(["date"] + ordered_codes) + "\n")
        row = [date_val] + [str(scores[c]) for c in ordered_codes]
        f.write(",".join(row) + "\n")


def _write_csv_vertical(
    csv_path: Path,
    student: str,
    date_val: str,
    scores: Dict[str, int],
    notes: str | None,
) -> None:
    """
    Append one row per (student, date, code) to CSV in long/vertical format.

    Header: student,date,code,score,notes
    """
    write_header = not csv_path.exists()
    safe_notes = (notes or "").replace("\n", " ").replace("\r", " ").strip()
    with _locked_file(csv_path, "a") as f:
        if write_header:
            f.write("student,date,code,score,notes\n")
        for code, score in scores.items():
            f.write(
                ",".join([
                    _csv_escape(student),
                    _csv_escape(date_val),
                    _csv_escape(code),
                    str(score),
                    _csv_escape(safe_notes),
                ])
                + "\n"
            )


def _csv_escape(value: str) -> str:
    """
    Minimal CSV escaping: wrap in quotes if comma or quote present.
    """
    if '"' in value:
        value = value.replace('"', '""')
    if "," in value or '"' in value:
        value = f'"{value}"'
    return value


# ---------------------------------------------------------------------------
# JSON Snapshot Writer
# ---------------------------------------------------------------------------


def _write_json_snapshot(
    json_dir: Path,
    prefix: str,
    student: str,
    date_val: str,
    scores: Dict[str, int],
    notes: str | None,
) -> Path:
    """
    Write a timestamped JSON snapshot of the session.

    Returns
    -------
    Path
        The path to the created JSON file.
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    json_path = json_dir / f"{prefix.lower()}_{ts}.json"
    payload = {
        "student_name": student,
        "date": date_val,
        "notes": notes,
        "part_scores": scores,
        "schema_version": 1,
    }
    with _locked_file(json_path, "w") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
    return json_path


# ---------------------------------------------------------------------------
# Unified Artifact Writer
# ---------------------------------------------------------------------------


def write_session_artifacts(
    base_dir: str | Path,
    student_name: str,
    date_val: str,
    part_scores: Dict[str, Any],
    notes: str | None = None,
    prefix: str = "Session",
    layout: LayoutType = "horizontal",
    include_json: bool = True,
    csv_filename: str | None = None,
) -> ArtifactPaths:
    """
    Write CSV (and optional JSON) artifacts for a single progress session.

    Parameters
    ----------
    base_dir : str | Path
        Root application home (e.g. APP_HOME). The student directory is created beneath:
          base_dir / "StudentDataFiles" / <SanitizedStudentName>
    student_name : str
        Raw name provided by UI (will be sanitized).
    date_val : str
        Session date (ISO or other valid string; no parsing enforced here).
    part_scores : dict
        Mapping of part code -> score OR part code -> (part_id, score).
    notes : str | None
        Optional free-form notes; sanitized for CSV (newlines removed).
    prefix : str
        Logical prefix for artifacts (e.g., "Abacus", "Braille"). Influences CSV base name
        if csv_filename not provided. JSON snapshots always lower-case the prefix in their
        filename prefix.
    layout : Literal["horizontal","vertical"]
        CSV layout style:
          - horizontal: one row per session (date + all codes as columns)
          - vertical:   one row per code (student,date,code,score,notes)
    include_json : bool
        Whether to emit a JSON snapshot.
    csv_filename : str | None
        Override default CSV filename. If None:
            horizontal -> f"{prefix}SkillsProgression.csv"
            vertical   -> f"{prefix}SkillsProgression.csv"

    Returns
    -------
    ArtifactPaths
        Dict-like with keys:
          student_dir, csv_path, (optional) json_path
    """
    base_path = Path(base_dir).resolve()
    student_clean = sanitize_student_name(student_name)
    student_dir = base_path / "StudentDataFiles" / student_clean
    student_dir.mkdir(parents=True, exist_ok=True)

    # Normalize incoming part_scores to code->score
    normalized_scores = normalize_part_scores(part_scores)

    if not csv_filename:
        csv_filename = f"{prefix}SkillsProgression.csv"

    csv_path = student_dir / csv_filename

    if layout == "horizontal":
        _write_csv_horizontal(csv_path, date_val, normalized_scores)
    elif layout == "vertical":
        _write_csv_vertical(csv_path, student_clean, date_val, normalized_scores, notes)
    else:
        raise ValueError(f"Unsupported layout '{layout}'")

    result = ArtifactPaths(
        student_dir=str(student_dir),
        csv_path=str(csv_path),
    )

    if include_json:
        json_path = _write_json_snapshot(
            json_dir=student_dir,
            prefix=prefix,
            student=student_clean,
            date_val=date_val,
            scores=normalized_scores,
            notes=notes,
        )
        result["json_path"] = str(json_path)

    return result


# ---------------------------------------------------------------------------
# CLI / Manual Test (Optional)
# ---------------------------------------------------------------------------

if __name__ == "__main__":  # Simple manual smoke test
    tmp_root = Path(os.environ.get("ARTIFACT_TMP", "./_artifact_test")).resolve()
    sample_scores = {
        "P1_1": (10, 2),
        "P1_2": (11, 3),
        "P1_3": (12, 1),
    }
    out = write_session_artifacts(
        base_dir=tmp_root,
        student_name="Jane  Doe  ",
        date_val="2025-01-15",
        part_scores=sample_scores,
        notes="Great progress\nNeeds follow-up on place value.",
        prefix="Abacus",
        layout="horizontal",
        include_json=True,
    )
    print("Artifacts written:", out)
