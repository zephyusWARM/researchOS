# SNAPSHOT

Updated: 2026-10-14T14:49:31+08:00

## Current state

The broad frontier survey remains paused. The private extract audit and v0.1 proposal have now been stress-tested with controlled simulations, independent elementary-math checks, and a small public PBC pilot. A targeted GNN necessity review was added for AIIM Week 9. All new fitted models use synthetic or public data; no MJ prediction model has been fitted. The public pilot is an internal structural control on another disease and endpoint, not external validation of NAFLD prediction.

Private deliverables from this milestone: `NAFLD_GNN_Research_v0.2_20261014.md`, `NAFLD_Proposal_Stress_Test_20261014.md`, and `NAFLD_Research_v0.2_Package_20261014.zip`. The package retains the original proposal/dossier and supplies additive corrections, reproducible scripts, aggregate evidence, and supported/inferred/proposed claim records.

This public checkpoint records workflow and generic design decisions only. Do not upload course records, full codebooks, participant timelines, detailed private findings, or the private research package. Prior publication-scope questions remain unresolved.

## Candidate research question

After accounting for a patient's own available history, observation process and shared context, when does borrowing from similar patients improve prospective risk prediction, and does that gain transfer to future patients?

This extends the earlier candidate on history evaluation under incomplete outcomes and record retention. It remains unverified, not a demonstrated MJ effect or confirmed novel method. A graph is one implementation of relational borrowing; the question must remain useful without GNNs.

## Decisions from the new controls

- Keep biological changes, past observation, record retention, future detection and selected populations distinct. Input deletion with fixed labels does not validate a different screening policy.
- Require predictors and node/risk-set eligibility to be decidable using available past information. Participant-disjoint splits alone do not establish this.
- Downgrade elementary temporal paired-loss bounds to diagnostics/baselines. Independent LP checks and designed simulations do not establish new theory, population confidence coverage or sufficient practical gain.
- Do not use a competing model's own imputed labels as unqualified evidence that it wins. Cross-fitting alone does not validate unknown-outcome probabilities.
- Do not assume future selection always inflates history value; the exact counterexample and small public controls do not establish a universal bias direction.
- Distinguish useful relationships from useful GNN implementation. Beating a random graph is insufficient; compare full own-history baselines and non-GNN methods with the same reference access.
- A deterministic feature graph adds no raw observations conditional on the complete feature collection, but can still change finite-sample learning. Do not infer that all feature graphs are useless.
- Raw homophily depends on imbalance, endpoint, horizon and unknown outcomes. Heterophily alone does not determine whether aggregation loses useful information.

These are bounded decisions recorded in the private v0.2 claim ledger/reports, not publication-level findings about the course cohort.

## Public primary-source pointers

- G01, direct fatty-liver neighbor: https://doi.org/10.3346/jkms.2026.41.e30 — Methods and Results, same-visit semi-supervised classification. Graph-construction supplement not successfully retrieved; do not assert a preprocessing flaw without verification.
- G02, patient graph plus survival precedent: https://doi.org/10.3390/bioengineering10091046 — GNN-surv; not a reproduction or the same endpoint.
- G03, population graph construction: https://arxiv.org/pdf/1806.01738 — section 2.2 and discussion.
- G04, learning without a supplied graph: https://proceedings.mlr.press/v97/franceschi19a.html — sections 4.2–4.3 and Table 1.
- G05, ego/neighbor and heterophily: https://papers.nips.cc/paper_files/paper/2020/hash/58ae23d878a47004366189884c2f8440-Abstract.html — Table 1 and section 3; special theorem assumptions do not establish medical conclusions.
- G06, good/bad heterophily: https://arxiv.org/pdf/2106.06134 — sections 2–3 and Theorem 1.
- G07, feature-dependent distinguishability: https://proceedings.neurips.cc/paper_files/paper/2023/hash/5ba11de4c74548071899cf41dec078bf-Abstract-Conference.html — sections 2–3.
- G08, past-only risk-set foundation: https://stat.ethz.ch/R-manual/R-patched/library/survival/doc/timedep.pdf — section 2.
- Prior evaluation neighbors: https://papers.nips.cc/paper_files/paper/2024/hash/f4c6bec746b0aeca8c2cd15096f1ad1f-Abstract-Conference.html ; https://proceedings.mlr.press/v258/dervovic25a.html ; https://arxiv.org/html/2501.01280v1 ; https://arxiv.org/html/2306.08084v1 ; https://arxiv.org/html/2508.15489v1 . Exact assumptions and version distinctions are recorded privately.

Generic patient graphs, GNN survival heads, observation-aware architectures, history/current comparisons and elementary missing-label bounds are insufficient novelty claims. No citation count or title-match absence certifies novelty.

## Next actions

Continue existing `task-data-audit`; it remains open for original processing provenance and an as-of data contract.

1. Resolve eligibility, terminal-negative measurements, visit retention, missing-data processing, exposure lineage and label availability. If a prospective risk set cannot be reconstructed, restrict claims to the selected retrospective population.
2. Freeze recorded first detection as the target. Do not conflate current diagnosis, latent onset, mortality/transplant or standardized-screening outcomes.
3. Predefine horizon, raw prefix, chronological label cutoff, reference bank, participant split and evaluator before fitting MJ models.
4. Run a fair current/history/observation comparison. Then examine neighbor summaries or kernel borrowing before scaling graph learners.
5. Compare GNNs with equal-information own-history and non-GNN relational baselines, using comparable validation budgets. Keep inductive and permitted transductive tasks separate.
6. Add chronological/geographic tests under an explicit reference/context availability contract; random splits do not establish new-population deployment.
7. Pursue a method proposal only if a reproducible unresolved failure survives source reconciliation and strong baselines. Negative results can justify abandoning GNNs.

## Retained exploration lines

History decomposition; observation/detection and extraction; pre-detection metabolic signatures; environmental change and incidence; causal identifiability and transportability. Geographic or biological graphs need verified additional relations; do not invent them from the course theme.

## Recovery

Read the two v0.2 reports first, then the archived v0.1 proposal/dossier and prior audit. Do not restart broad surveying or treat PBC as MJ replication. Raw public PBC records are not bundled; the private package retains source hashes and reproduction instructions. Original source scripts and terminal-visit data remain important gaps. The older survey run metadata still has a running entry; do not infer an active worker or invent its missing end time.

## Research rule

Problem first. Information second. Method last. No MJ model improvement, causal relationship, biological mechanism, broad transportability or top-conference novelty is asserted by this checkpoint.
