#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from researchos.core import record_map, parse_time
from researchos.validation import validate_repo

p=argparse.ArgumentParser()
p.add_argument('project')
p.add_argument('--stale-hours',type=float,default=12)
a=p.parse_args(); project=(ROOT/a.project).resolve()
errors=validate_repo(ROOT)
if errors:
    print('ERRORS')
    for e in errors: print(f'- {e}')
else: print('Structural validation: PASS')
now=datetime.now(timezone.utc); stale=[]
for r in record_map(project)['runs'].values():
    if r.get('status')=='running':
        age=now-parse_time(r['started_at']).astimezone(timezone.utc)
        if age>timedelta(hours=a.stale_hours): stale.append((r['id'],age))
if stale:
    print('WARN: stale running runs')
    for rid,age in stale: print(f'- {rid}: {age}')
else: print('Stale-run check: PASS')
raise SystemExit(1 if errors else 0)
