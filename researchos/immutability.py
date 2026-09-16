from __future__ import annotations
from typing import Any
from .core import TERMINAL_RUNS, RUN_STATUSES

IMMUTABLE_FOLDERS={"sources","evidence","claims"}
RUN_IDENTITY_FIELDS=("id","task_id","started_at","base_commit")


def classify_path(path: str) -> str | None:
    parts=path.split("/")
    if len(parts)>=4 and parts[0]=="projects" and parts[2] in IMMUTABLE_FOLDERS|{"runs"} and path.endswith(".json"):
        return parts[2]
    return None


def check_record_change(folder: str, old: dict[str,Any] | None, new: dict[str,Any] | None) -> list[str]:
    if old is None: return []  # additions are allowed
    if new is None: return [f"deletion forbidden for canonical {folder} record"]
    if folder in IMMUTABLE_FOLDERS:
        if old!=new: return [f"merged {folder} records are append-only; add a replacement/revision instead"]
        return []
    if folder=="runs":
        if old.get("status") in TERMINAL_RUNS:
            if old!=new: return ["terminal run is immutable"]
            return []
        if old.get("status")!="running": return [f"unknown prior run status {old.get('status')!r}"]
        if new.get("status") not in TERMINAL_RUNS: return ["a merged running run may only be changed by terminalizing it"]
        for f in RUN_IDENTITY_FIELDS:
            if old.get(f)!=new.get(f): return [f"run terminalization changed immutable field {f}"]
        if not new.get("ended_at"): return ["terminalized run requires ended_at"]
        return []
    return []
