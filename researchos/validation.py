from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .core import *


def _rel(path: Path, root: Path) -> str:
    try: return str(path.relative_to(root))
    except ValueError: return str(path)


def validate_project(project: Path, root: Path | None=None) -> list[str]:
    root=root or project.parent.parent
    errors=[]
    pf=project/"project.json"
    if not pf.exists():
        return [f"{_rel(project,root)}: missing project.json"]
    try: meta=load_json(pf)
    except Exception as e: return [f"{_rel(pf,root)}: invalid JSON: {e}"]
    for k in ("id","title","status","cutoff_date","created_at"):
        if k not in meta: errors.append(f"{_rel(pf,root)}: missing field {k}")
    if meta.get("status") not in PROJECT_STATUSES: errors.append(f"{_rel(pf,root)}: invalid project status {meta.get('status')!r}")

    rec={folder:{} for folder in FOLDERS}
    paths={folder:{} for folder in FOLDERS}
    for folder in FOLDERS:
        base=project/folder
        if not base.exists():
            errors.append(f"{_rel(base,root)}: missing directory")
            continue
        for path in sorted(base.glob("*.json")):
            try: obj=load_json(path)
            except Exception as e:
                errors.append(f"{_rel(path,root)}: invalid JSON: {e}"); continue
            missing=REQUIRED[folder]-set(obj)
            if missing: errors.append(f"{_rel(path,root)}: missing fields {sorted(missing)}")
            rid=obj.get("id")
            if not isinstance(rid,str) or not rid.startswith(PREFIX[folder]):
                errors.append(f"{_rel(path,root)}: id must start with {PREFIX[folder]!r}"); continue
            if path.stem != rid:
                errors.append(f"{_rel(path,root)}: filename must equal id ({rid}.json)")
            if rid in rec[folder]: errors.append(f"{_rel(path,root)}: duplicate id {rid}")
            rec[folder][rid]=obj; paths[folder][rid]=path

    tasks, runs, sources, evs, claims=(rec[x] for x in FOLDERS)
    # enums + timestamps + task references
    for tid,t in tasks.items():
        if t.get("status") not in TASK_STATUSES: errors.append(f"{project.name}/tasks/{tid}: invalid status {t.get('status')!r}")
        m=t.get("max_active_runs")
        if not isinstance(m,int) or isinstance(m,bool) or m<1: errors.append(f"{project.name}/tasks/{tid}: max_active_runs must be integer >= 1")
        p=t.get("parent_task_id")
        if p and p not in tasks: errors.append(f"{project.name}/tasks/{tid}: unknown parent_task_id {p}")
        try: parse_time(t["created_at"])
        except Exception as e: errors.append(f"{project.name}/tasks/{tid}: invalid created_at: {e}")

    active=defaultdict(list)
    for rid,r in runs.items():
        if r.get("status") not in RUN_STATUSES: errors.append(f"{project.name}/runs/{rid}: invalid status {r.get('status')!r}")
        if r.get("task_id") not in tasks: errors.append(f"{project.name}/runs/{rid}: unknown task_id {r.get('task_id')}")
        if r.get("status")=="running": active[r.get("task_id")].append(rid)
        if r.get("status") in TERMINAL_RUNS and not r.get("ended_at"): errors.append(f"{project.name}/runs/{rid}: terminal run requires ended_at")
        if r.get("status")=="running" and r.get("ended_at"): errors.append(f"{project.name}/runs/{rid}: running run must not have ended_at")
        try: st=parse_time(r["started_at"])
        except Exception as e: errors.append(f"{project.name}/runs/{rid}: invalid started_at: {e}"); st=None
        if r.get("ended_at"):
            try:
                en=parse_time(r["ended_at"])
                if st and en<st: errors.append(f"{project.name}/runs/{rid}: ended_at precedes started_at")
            except Exception as e: errors.append(f"{project.name}/runs/{rid}: invalid ended_at: {e}")
    for tid,rids in active.items():
        if tid in tasks and len(rids)>tasks[tid].get("max_active_runs",1):
            errors.append(f"{project.name}/tasks/{tid}: {len(rids)} active runs exceed max_active_runs={tasks[tid].get('max_active_runs')}: {', '.join(rids)}")

    for sid,s in sources.items():
        if not isinstance(s.get("locator"),str) or not s.get("locator").strip(): errors.append(f"{project.name}/sources/{sid}: locator required")
        if s.get("supersedes") and s["supersedes"] not in sources: errors.append(f"{project.name}/sources/{sid}: unknown supersedes {s['supersedes']}")

    for eid,e in evs.items():
        if e.get("source_id") not in sources: errors.append(f"{project.name}/evidence/{eid}: unknown source_id {e.get('source_id')}")
        if e.get("evidence_type") not in EVIDENCE_TYPES: errors.append(f"{project.name}/evidence/{eid}: invalid evidence_type {e.get('evidence_type')!r}")
        if not isinstance(e.get("locator"),str) or not e.get("locator").strip(): errors.append(f"{project.name}/evidence/{eid}: locator required")

    by_key=defaultdict(list)
    children=defaultdict(list)
    for cid,c in claims.items():
        if c.get("status") not in CLAIM_STATUSES: errors.append(f"{project.name}/claims/{cid}: invalid status {c.get('status')!r}")
        if not isinstance(c.get("revision"),int) or isinstance(c.get("revision"),bool) or c.get("revision",0)<1: errors.append(f"{project.name}/claims/{cid}: revision must be integer >= 1")
        ids=c.get("evidence_ids")
        if not isinstance(ids,list): errors.append(f"{project.name}/claims/{cid}: evidence_ids must be list"); ids=[]
        if c.get("status") in {"supported","disputed"} and not ids: errors.append(f"{project.name}/claims/{cid}: {c.get('status')} claim requires evidence")
        for eid in ids:
            if eid not in evs: errors.append(f"{project.name}/claims/{cid}: unknown evidence_id {eid}")
        by_key[c.get("claim_key")].append(c)
        if c.get("supersedes"): children[c["supersedes"]].append(cid)

    for key,items in by_key.items():
        if not key: errors.append(f"{project.name}/claims: claim_key cannot be empty"); continue
        revs={c.get("revision"):c for c in items}
        if len(revs)!=len(items): errors.append(f"{project.name}/claims/{key}: duplicate revision number")
        for c in items:
            rev=c.get("revision")
            prev=c.get("supersedes")
            if rev==1 and prev: errors.append(f"{project.name}/claims/{c.get('id')}: revision 1 must not supersede another claim")
            if rev and rev>1:
                if not prev: errors.append(f"{project.name}/claims/{c.get('id')}: revision {rev} requires supersedes")
                elif prev not in claims: errors.append(f"{project.name}/claims/{c.get('id')}: unknown supersedes {prev}")
                else:
                    p=claims[prev]
                    if p.get("claim_key")!=key: errors.append(f"{project.name}/claims/{c.get('id')}: supersedes must use same claim_key")
                    if p.get("revision")!=rev-1: errors.append(f"{project.name}/claims/{c.get('id')}: supersedes revision must be {rev-1}")
        # no forks: any node may have at most one child; exactly one leaf
        ids={c.get("id") for c in items}
        for parent,kids in children.items():
            relevant=[x for x in kids if x in ids]
            if parent in ids and len(relevant)>1: errors.append(f"{project.name}/claims/{key}: revision fork from {parent}: {', '.join(relevant)}")
        superseded={c.get("supersedes") for c in items if c.get("supersedes")}
        leaves=[c.get("id") for c in items if c.get("id") not in superseded]
        if len(leaves)>1: errors.append(f"{project.name}/claims/{key}: multiple latest leaves: {', '.join(leaves)}")

    # Required recovery surface
    for name in ("PROGRAM.md","SNAPSHOT.md","COVERAGE.md"):
        if not (project/name).exists(): errors.append(f"{project.name}: missing recovery file {name}")
    return errors


def validate_repo(root: Path) -> list[str]:
    errors=[]
    projects=root/"projects"
    if not projects.exists(): return ["projects/: missing directory"]
    for p in sorted(x for x in projects.iterdir() if x.is_dir()):
        errors.extend(validate_project(p,root))
    return errors
