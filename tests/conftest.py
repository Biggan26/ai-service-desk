import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent[1]
SRC_DIR = ROOT_DIR / "app"
if SRC_DIR.exists():
    sys.path.insert(0, str(SRC_DIR))
