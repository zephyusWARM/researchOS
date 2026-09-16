# Architecture

## 1. System boundary

`researchOS` is **not** a multi-agent framework, browser, vector database, or chat UI. It is a durable state protocol.

```text
Transient compute                         Durable state
─────────────────                         ─────────────
ChatGPT / other model  ───────────────▶   Git repository
browser / scripts                          project program
manual reading                             task + run records
ad-hoc analysis                            source + evidence records
                                           claim revisions
                                           coverage + snapshot
```

## 2. Entities

### Project
A bounded research program with scope, cutoff date, quality bar, and deliverables.

### Task
A persistent research question or unit of work. A retry never creates a new task merely because execution failed.

### Run
One concrete execution attempt for a task. It records where the attempt started, what happened, and how it ended.

### Source
A bibliographic/documentary object: paper, thesis, webpage, dataset, official record, transcript, etc.

### Evidence
A bounded observation extracted from a source with a precise locator. Evidence is not a vague summary of a whole document.

### Claim revision
A synthesized proposition. Claims are append-only revisions grouped by `claim_key`; a new revision points to the prior revision with `supersedes`.

### Snapshot
The small human-readable restart surface for a project. It tells a fresh worker what is true now, what is unresolved, and what to do next.

## 3. Provenance graph

```text
claim.evidence_ids[]
          │
          ▼
      evidence ─────▶ source

run ─────▶ task
```

A `supported` claim must have evidence. Every evidence record must resolve to one source.

## 4. State machines

```text
Task: open → active ↔ blocked → done | cancelled
Run:  running → succeeded | failed | interrupted | superseded
Claim revision status: proposed | supported | disputed | retired
```

`superseded` is deliberately **derived** for claims: if a newer claim revision points to an older revision, the older revision is superseded without mutating its historical file.

## 5. Append-only history

Canonical `sources/`, `evidence/`, and `claims/` records are immutable after merge. Correct them by adding a replacement/superseding record.

A run can be updated exactly once from `running` to a terminal state. After it is terminal, it is immutable.

Tasks, `SNAPSHOT.md`, and `COVERAGE.md` are living state and may change through reviewed commits.

## 6. Concurrency

Each task declares `max_active_runs` (default policy: 1). Validation rejects more simultaneous `running` runs than the task permits. This prevents accidental duplicate workers while still allowing explicit parallel research.

Claim revisions also reject forks: a `claim_key` may have only one latest leaf unless the system is explicitly extended to model branches.

## 7. Recovery

`python scripts/context.py projects/<project>` produces a bounded restart packet from canonical state. A conversation should never be required to remember facts that are absent from Git.

## 8. Integration boundary

Substantial canonical changes should enter `main` through PR review and CI. CI validates references, state machines, revision chains, concurrency limits, and immutable-history rules.
