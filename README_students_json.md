Where students.json is loaded from

This project loads student names from a JSON file named `students.json`.

Search order (first match wins):

- `PROJECT_ROOT/json_Files/students.json` (package-local)
- `PROJECT_ROOT/json_files/students.json` (alternate case)
- `REPO_ROOT/json_Files/students.json` (repo root)
- `REPO_ROOT/json_files/students.json` (repo root alt case)
- `APP_HOME/json_Files/students.json` (runtime data directory)
- `APP_HOME/json_files/students.json`

Behavior:
- If a `students.json` is found outside the package-local folder, it will be copied into `PROJECT_ROOT/json_Files/students.json` so subsequent accesses are stable.
- If none is found, the application will create a minimal `PROJECT_ROOT/json_Files/students.json` containing `{"students": []}` to avoid repeated missing-file warnings.

If you want to provide an initial roster, place `students.json` in the repository root `json_Files/` folder (this is what the project historically used). Otherwise, the app will create an empty roster file automatically at startup.