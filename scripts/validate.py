#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from researchos.validation import validate_repo

errors=validate_repo(ROOT)
if errors:
    print("researchOS validation FAILED")
    for e in errors: print(f"- {e}")
    raise SystemExit(1)
print("researchOS validation PASSED")
