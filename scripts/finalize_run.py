#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from researchos.core import TERMINAL_RUNS, load_json
from researchos.validation import validate_repo

p=argparse.ArgumentParser(description="Terminalize one running researchOS run")
p.add_argument('project')
p.add_argument('run_id')
p.add_argument('status',choices=sorted(TERMINAL_RUNS))
p.add_argument('--summary',required=True)
p.add_argument('--reason',default=None)
a=p.parse_args()
project=(ROOT/a.project).resolve(); path=project/'runs'/f'{a.run_id}.json'
if not path.exists(): raise SystemExit(f"missing run: {path}")
obj=load_json(path)
if obj.get('status')!='running': raise SystemExit(f"run is already {obj.get('status')}; terminal records are immutable")
obj['status']=a.status
obj['ended_at']=datetime.now().astimezone().isoformat(timespec='seconds')
obj['summary']=a.summary
obj['termination_reason']=a.reason
path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
errors=validate_repo(ROOT)
if errors:
    print("terminalization produced invalid repository:")
    for e in errors: print(f"- {e}")
    raise SystemExit(1)
print(f"finalized {a.run_id} → {a.status}")
