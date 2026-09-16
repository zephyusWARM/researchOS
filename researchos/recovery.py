from __future__ import annotations
from pathlib import Path
from .core import load_json, record_map, latest_claims


def build_context(project: Path, claim_limit: int=20) -> str:
    meta=load_json(project/"project.json")
    rec=record_map(project)
    out=[]
    out.append(f"# Recovery Context — {meta['title']}")
    out.append(f"\nProject status: **{meta['status']}**  ")
    out.append(f"Research cutoff: **{meta['cutoff_date']}**\n")
    for name in ("PROGRAM.md","SNAPSHOT.md","COVERAGE.md"):
        p=project/name
        if p.exists():
            out.append(f"\n---\n## {name}\n\n{p.read_text(encoding='utf-8').strip()}\n")
    live=[t for t in rec['tasks'].values() if t.get('status') in {'open','active','blocked'}]
    out.append("\n---\n## Live tasks\n")
    if not live: out.append("\n_None._\n")
    for t in sorted(live,key=lambda x:x['id']):
        out.append(f"\n- **{t['id']}** [{t['status']}] {t['title']} — {t['question']}")
    active=[r for r in rec['runs'].values() if r.get('status')=='running']
    out.append("\n\n## Active runs\n")
    if not active: out.append("\n_None._\n")
    for r in sorted(active,key=lambda x:x['id']): out.append(f"\n- **{r['id']}** → {r['task_id']} (started {r['started_at']})")
    claims=latest_claims(rec['claims'])[-claim_limit:]
    out.append("\n\n## Latest claim revisions\n")
    if not claims: out.append("\n_None yet._\n")
    for c in claims:
        out.append(f"\n- **{c['claim_key']} r{c['revision']}** [{c['status']}] {c['statement']} (`{c['id']}`)")
    out.append("\n")
    return "".join(out)
