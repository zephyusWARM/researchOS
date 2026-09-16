# Agent / AI Worker Contract

This repository may be edited by humans or transient AI research workers.

## Required behavior

1. Read `PROGRAM.md`, `SNAPSHOT.md`, and `COVERAGE.md` before deep work.
2. Reuse existing tasks; retries are new runs.
3. Never invent provenance. Unknown is a valid state.
4. Evidence must be attributable to a source and carry a precise locator.
5. Supported claims must cite evidence IDs.
6. Do not silently rewrite merged sources, evidence, claims, or terminal runs.
7. Represent corrections additively with new records/revisions.
8. Keep factual source reports, model inference, and unresolved questions distinct.
9. Before handoff, leave `SNAPSHOT.md` accurate enough for a fresh worker.
10. Run validation before proposing integration.

## Recovery command

```bash
python scripts/context.py projects/<project>
```

Treat its output as the minimum durable context packet, not as a substitute for reading evidence when making new claims.
