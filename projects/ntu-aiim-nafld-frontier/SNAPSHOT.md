# SNAPSHOT

Updated: 2026-10-12T22:42:08+08:00

## Current state

The broad frontier survey remains paused. The first reproducible private extract-level audit has been followed by a targeted proposal-feasibility study. Its private deliverables are `NAFLD_Proposal_v0.1_20261012.md` and `NAFLD_Proposal_Research_Package_20261012.zip`. The package includes a source-threat matrix, descriptive design-support checks, exact synthetic examples, and checked elementary paired-loss bounds. No real-cohort prediction model or external replication has been completed.

This public checkpoint records research workflow and generic design decisions only. Do not upload course records, full codebooks, private evidence, participant timelines, detailed numerical findings, or the private proposal package to this repository. Prior publication-scope questions remain unresolved.

## Candidate research question

When can the incremental predictive value of patient history be supported under incomplete outcomes and changes in which historical records are retained? This is a proposed evaluation problem, not an established finding or a confirmed novel method.

Keep three mechanisms distinct: changes to historical inputs, changes to future examination/detection, and changes to the selected study population. Input deletion with unchanged labels cannot validate a new disease-detection policy. A common retrospective landmark comparison also does not establish that its risk set could have been identified at prediction time.

## Novelty threats to compare

- Informative-sampling adjustment: https://proceedings.mlr.press/v202/vanderschueren23a.html
- Clinical-presence shift and joint survival prediction: https://arxiv.org/abs/2508.05472
- Structural irregular-time-series perturbation: https://proceedings.neurips.cc/paper_files/paper/2025/hash/4eb5daabc45b45a9a312aa2c8fca8a74-Abstract-Conference.html
- Partial-identification model evaluation: https://papers.nips.cc/paper_files/paper/2024/hash/f4c6bec746b0aeca8c2cd15096f1ad1f-Abstract-Conference.html
- Survival score validity under administrative censoring: https://jmlr.org/papers/v24/19-1030.html

Generic observation-aware architectures, history-versus-current comparison, and elementary missing-label bounds are not adequate novelty claims. The proposed temporal extension and combined evaluation protocol require further proof-level comparison and empirical validation.

## Next actions

Continue existing `task-data-audit`; it remains open for original processing provenance and an as-of data contract.

1. Verify eligibility, visit retention, terminal-visit measurements, event definition, missing-data processing, baseline origins, exposure assignment and censoring.
2. Establish whether a clinically prospective landmark risk set can be formed using information available at that date. Otherwise explicitly restrict claims to the selected retrospective extract population.
3. Freeze the target as recorded first detection; biological onset, current disease state, and standardized-screening outcomes require separate assumptions.
4. Predefine horizon, raw-prefix information sets, chronological label-availability cutoffs, participant splits and paired comparison procedure before fitting outcome models.
5. Run the smallest fair current/history/observation comparison once its source contract is usable. Report unknown outcomes, assumption-based scores and compatible gain ranges separately.
6. Develop simulations that independently control biology, observation, extraction and censoring; include settings in which simple summaries are stable and history genuinely helps.
7. Compare temporal paired-loss bounds against existing partial-identification and interval-censored evaluation methods. Do not promote elementary algebra into a novelty theorem.
8. Verify external dataset access and task alignment before promising replication. No external dataset has been acquired in this milestone.

## Retained exploration lines

History decomposition; observation/detection and extraction; pre-detection metabolic signatures; environmental change and incidence; causal identifiability and transportability. The private proposal prioritizes a conditional history-evaluation path, without declaring the other lines scientifically unimportant.

## Recovery

Read the private proposal and research dossier before restarting research. The proposal is v0.1 and includes falsification and downgrade conditions. Original source scripts and terminal-visit data remain important gaps. The older survey run metadata still has a running entry; do not infer an active worker or invent its missing end time.

## Research rule

Problem first. Information second. Method last. No private audit finding, real-cohort history improvement, biological mechanism, causal effect, broad transportability or top-conference novelty is asserted by this public checkpoint.
