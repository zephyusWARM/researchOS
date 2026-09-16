#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from researchos.core import project_summary

if len(sys.argv)!=2:
    print("usage: python scripts/status.py projects/<project>"); raise SystemExit(2)
project=(ROOT/sys.argv[1]).resolve()
summary=project_summary(project); meta=summary['project']
print(f"Project: {meta['title']}")
print(f"Status:  {meta['status']}")
print(f"Cutoff:  {meta['cutoff_date']}")
for folder in ('tasks','runs','sources','evidence','claims'):
    statuses=summary['statuses'][folder]
    suffix=', '.join(f"{k}={v}" for k,v in sorted(statuses.items()))
    print(f"{folder:9} {summary['counts'][folder]:4}"+(f"  ({suffix})" if suffix else ""))
print(f"latest claim leaves: {len(summary['latest_claims'])}")
