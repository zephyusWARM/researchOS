# researchOS

A durable, auditable research operating system for long-horizon AI-assisted research.

> **Conversations are disposable. Research state is not.**

`researchOS` is the durable state layer between transient research execution (ChatGPT, browsers, scripts, human reading) and a long-lived, reviewable knowledge base in Git.

## Core loop

```text
Project
  ↓
Task ──────── persistent research question
  ↓
Run ───────── one disposable execution attempt
  ↓
Source ────── document / paper / webpage / dataset
  ↓
Evidence ──── bounded attributable observation
  ↓
Claim ─────── synthesized proposition, append-only revisions
  ↓
Review / PR
  ↓
Snapshot ──── compact restart surface
```

## Five invariants

1. **Resume after failure** — a fresh conversation can recover state without reading old chats.
2. **Trace every claim** — supported claims resolve to evidence, which resolves to sources.
3. **Separate task from attempt** — a task survives failed, interrupted, or superseded runs.
4. **Preserve history** — captured evidence and historical terminal runs are not silently rewritten.
5. **Prefer boring infrastructure** — Markdown + JSON + Git + standard-library Python before databases or agent frameworks.

## Repository map

```text
.research-os/     contracts, schemas, policies, ADRs, templates
.github/          Issue / PR workflow and CI integrity gate
researchos/       standard-library validation/recovery core
scripts/          operator commands
projects/         canonical research programs
tests/            integrity and state-machine tests
```

## Quick start

```bash
python scripts/validate.py
python scripts/status.py projects/ntu-gice-phase2
python scripts/context.py projects/ntu-gice-phase2
python -m unittest discover -s tests -p 'test_*.py'
```

## Recovery order

A new researcher or AI worker should read only these first:

1. `PROGRAM.md`
2. `SNAPSHOT.md`
3. `COVERAGE.md`
4. open/active task records
5. latest claim revisions
6. deeper source/evidence/run records only as needed

The first production dogfood project is `projects/ntu-gice-phase2`.
