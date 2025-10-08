import sys
from pathlib import Path

# Ensure the repository root is on sys.path during pytest collection so
# tests can import the StudentDataGUI package (which lives in repo/StudentDataGUI).
ROOT = Path(__file__).resolve().parent.parent
root_str = str(ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)
