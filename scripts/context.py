#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from researchos.recovery import build_context

if len(sys.argv)!=2:
    print("usage: python scripts/context.py projects/<project>"); raise SystemExit(2)
project=(ROOT/sys.argv[1]).resolve()
print(build_context(project))
