# researchOS Invariants

1. **Conversation independence** — no canonical fact may exist only in chat history.
2. **Task/run separation** — retries create new runs, not duplicate tasks.
3. **Evidence provenance** — evidence identifies exactly one source.
4. **Claim provenance** — supported claims identify evidence.
5. **Append-only knowledge history** — merged source, evidence, and claim records are not rewritten.
6. **Terminal-run immutability** — a terminal run is a historical record.
7. **Single terminalization** — a merged running run may transition once to a terminal state without changing its identity/start fields.
8. **Explicit uncertainty** — proposed, supported, disputed, retired, unknown, stale, and inferred are not silently conflated.
9. **Concurrency is explicit** — active runs may not exceed the owning task's `max_active_runs`.
10. **No claim forks** — each `claim_key` has one latest revision leaf.
11. **Coverage accounting** — systematic scans record what was and was not searched.
12. **Restartability** — `SNAPSHOT.md` plus canonical records must orient a fresh worker.
13. **Canonical review** — substantial state enters `main` through CI-reviewed integration.
14. **Minimal machinery** — infrastructure is added only to prevent observed classes of research failure.
15. **Low-frequency, high-information persistence** — GitHub is durable state, not live telemetry or a scratchpad. Do not commit per query, page, paper, or minor thought. Research first; batch-persist only after a meaningful semantic/epistemic delta, a crash-critical checkpoint, run lifecycle transition, or coherent integration milestone.
