#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from researchos.immutability import classify_path, check_record_change

p=argparse.ArgumentParser(description="Reject destructive edits to canonical research history")
p.add_argument('--base',required=True,help='base commit SHA/ref')
a=p.parse_args()

def git(*args):
    return subprocess.run(['git',*args],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)

diff=git('diff','--name-status',a.base,'HEAD')
if diff.returncode: raise SystemExit(diff.stderr)
errors=[]
for line in diff.stdout.splitlines():
    fields=line.split('\t'); status=fields[0]
    path=fields[-1]
    folder=classify_path(path)
    if not folder: continue
    old=None; new=None
    if not status.startswith('A'):
        shown=git('show',f'{a.base}:{path}')
        if shown.returncode==0:
            try: old=json.loads(shown.stdout)
            except Exception as e: errors.append(f"{path}: cannot parse base JSON: {e}")
    if not status.startswith('D'):
        try: new=json.loads((ROOT/path).read_text(encoding='utf-8'))
        except Exception as e: errors.append(f"{path}: cannot parse new JSON: {e}")
    for msg in check_record_change(folder,old,new): errors.append(f"{path}: {msg}")
if errors:
    print('researchOS immutable-history guard FAILED')
    for e in errors: print(f'- {e}')
    raise SystemExit(1)
print('researchOS immutable-history guard PASSED')
