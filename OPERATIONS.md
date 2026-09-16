# Operations

## Start a research session

1. Read `PROGRAM.md`, `SNAPSHOT.md`, and `COVERAGE.md`.
2. Run `python scripts/status.py projects/<project>`.
3. Run `python scripts/context.py projects/<project>` for a compact restart packet.
4. Select an existing task. Do not create a duplicate task merely because a prior run failed.
5. Create a new run record with `status: running` and the Git base commit in `base_commit` when available.

## During research

- Add a source record when a document becomes part of the evidentiary corpus.
- Add evidence records for bounded observations with exact locators.
- Do not promote memory, search snippets, or model-generated text into evidence without an attributable source.
- Keep inference separate from source-reported fact.

## Finish or interrupt a run

Use:

```bash
python scripts/finalize_run.py projects/<project> <run-id> succeeded --summary "..."
```

Allowed terminal states are `succeeded`, `failed`, `interrupted`, and `superseded`.

If a browser/chat session dies, the next worker should finalize the abandoned `running` run as `interrupted` rather than pretending it never existed.

## Revise a claim

Never overwrite a merged claim record. Add a new revision with:

- the same `claim_key`
- `revision = previous + 1`
- `supersedes = <previous claim id>`
- evidence appropriate to the new statement/status

The prior claim becomes *effectively superseded* by graph structure, not by editing history.

## Pull requests

A research PR should state:

- task(s) advanced
- run(s) completed/interrupted
- sources/evidence added
- claims added/revised
- snapshot/coverage changes
- unresolved uncertainty

CI must pass before integration.

## Crash-recovery discipline

The canonical recovery surface is Git, not chat history. After meaningful progress, update durable state before continuing into another large research branch.
