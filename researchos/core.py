from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

FOLDERS = ("tasks", "runs", "sources", "evidence", "claims")
PREFIX = {"tasks":"task-", "runs":"run-", "sources":"src-", "evidence":"ev-", "claims":"claim-"}
REQUIRED = {
    "tasks": {"id","title","status","question","created_at","max_active_runs"},
    "runs": {"id","task_id","status","started_at"},
    "sources": {"id","title","source_type","locator","captured_at"},
    "evidence": {"id","source_id","statement","locator","captured_at","evidence_type"},
    "claims": {"id","claim_key","revision","statement","status","evidence_ids","created_at"},
}
TASK_STATUSES={"open","active","blocked","done","cancelled"}
RUN_STATUSES={"running","succeeded","failed","interrupted","superseded"}
TERMINAL_RUNS=RUN_STATUSES-{"running"}
CLAIM_STATUSES={"proposed","supported","disputed","retired"}
EVIDENCE_TYPES={"quote","paraphrase","data","metadata","observation"}
PROJECT_STATUSES={"active","paused","complete","archived"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    dt=datetime.fromisoformat(value.replace("Z","+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return dt


def record_map(project: Path) -> dict[str, dict[str, dict[str, Any]]]:
    out={folder:{} for folder in FOLDERS}
    for folder in FOLDERS:
        base=project/folder
        if not base.exists():
            continue
        for path in sorted(base.glob("*.json")):
            obj=load_json(path)
            rid=obj.get("id", path.stem)
            out[folder][rid]=obj
    return out


def latest_claims(claims: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    superseded={c.get("supersedes") for c in claims.values() if c.get("supersedes")}
    return sorted((c for cid,c in claims.items() if cid not in superseded), key=lambda c:(c.get("claim_key",""), c.get("revision",0)))


def project_summary(project: Path) -> dict[str, Any]:
    meta=load_json(project/"project.json")
    rec=record_map(project)
    return {
        "project":meta,
        "counts":{k:len(v) for k,v in rec.items()},
        "statuses":{k:dict(Counter(x.get("status","n/a") for x in v.values())) for k,v in rec.items()},
        "latest_claims":latest_claims(rec["claims"]),
    }
