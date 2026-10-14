# SNAPSHOT

Updated: 2026-10-14T15:48:28+08:00

## Current state

The broad frontier survey remains paused. The private extract audit and v0.1 proposal have now been stress-tested with controlled simulations, independent elementary-math checks, and a small public PBC pilot. A targeted GNN necessity review was added for AIIM Week 9. All new fitted models use synthetic or public data; no MJ prediction model has been fitted. The public pilot is an internal structural control on another disease and endpoint, not external validation of NAFLD prediction.

Private deliverables from this milestone: `NAFLD_GNN_Research_v0.2_20261014.md`, `NAFLD_Proposal_Stress_Test_20261014.md`, and `NAFLD_Research_v0.2_Package_20261014.zip`. The package retains the original proposal/dossier and supplies additive corrections, reproducible scripts, aggregate evidence, and supported/inferred/proposed claim records.

This public checkpoint records workflow and generic design decisions only. Do not upload course records, full codebooks, participant timelines, detailed private findings, or the private research package. Prior publication-scope questions remain unresolved.

+## 2026-10-14 v0.3 additive milestone

The targeted study now includes a second public longitudinal control (author-supplied AIDS data) and an official two-cycle NHANES CAP surrogate experiment. Public source bytes were acquired and hashed, the relevant XPORT fields were checked with an independent reader, and the aggregate outputs were freshly reproduced. The source-bank restoration control was also repeated without changing the original locked predictions. No private MJ outcome model was fitted.

Private deliverables: `NAFLD_Deep_Research_v0.3_20261014.html`, its Markdown source, `NAFLD_Proposal_Prelude_v0.3_20261014.md`, and `NAFLD_Research_v0.3_Package_20261014.zip`. The package preserves the v0.2 milestone and contains current scripts, aggregate evidence, source hashes, claim boundaries and scientific figures. Raw participant records and individual predictions are excluded.

New design decisions:

- Treat CAP surrogate estimation, recorded disease detection, latent disease and mortality as distinct tasks. Two NHANES cycles are distinct participants, not individual longitudinal validation.
- Count validation annotations in any label-scarcity claim. Artificial withholding differs from outcome censoring.
- Define the reference bank independently from the outcome-learning domain. Restoring earlier QC-excluded people can change contextual predictions without adding their labels; this dependence also occurs in non-GNN summaries.
- Separate known-label/fixed-prediction bounds from evaluation of a different reference graph. Independent-reference relaxations can be valid but loose; shared-node constraints may tighten joint risk bounds.
- Separate useful history from biological path dependence. Past measurements can denoise a static current latent state.
- Compare graph learners with strong smooth own-feature and equal-information relational controls. Local finite-sample gains do not establish GNN necessity.
- Distinguish finite-cohort identification, target-design uncertainty and training uncertainty. Numerical derivative/parser checks validate implementation, not unknown clinical selection assumptions.

Clinical history value under an explicit as-of contract remains the actionable main line. Joint incremental-value evaluation under uncertain membership, reference context and outcomes is a conditional methods branch, not a confirmed novelty claim. It must survive direct comparisons with medical selection bounds, collective graph certificates and a simple fixed-reference deployment contract. A change of loss, medical dataset or non-adversarial intent alone is insufficient novelty.

New public primary sources:

- TMLR 2024 population-graph reassessment: https://github.com/tamaramueller/population_graphs . The successfully read full text is an older review attachment: https://openreview.net/notes/edits/attachment?id=XMk37YzJNc&name=pdf ; sections 5.1-5.2 and 6-7. Do not attribute its exact table to the final version.
- KDD 2026 selection-bias performance bound: https://arxiv.org/html/2606.00563v1 ; sections 3.1-3.3, Theorem 3.1; code https://github.com/kara-liu/selection_gap_est . Its assumptions and fixed-predictor scope remain relevant comparison requirements.
- Collective graph-injection certification: https://arxiv.org/html/2403.01423v1 ; sections 3.1-3.2 and 5.1-5.3. Shared-budget joint certification already exists; no first-joint-bound claim is warranted.
- NHANES original data/docs: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/LUX_J.htm and https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/LUX_L.htm ; variance guidance https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx . Added QC eligibility is a selected domain.
- AIDS author object/docs: https://github.com/drizopoulos/JMbayes2/blob/master/data/aids.rda and https://drizopoulos.github.io/JMbayes2/reference/aids.html ; actual object structure and supplied CD4 scale were checked privately.

The next step remains original source-pipeline reconciliation and a frozen risk-set/reference contract. If those cannot be reconstructed, restrict empirical claims to the selected retained population. Stop the methods branch if existing bounds suffice, plausible bounds remain uninformative, or a fixed reference contract solves the practical task. The broad survey remains paused; this was a targeted additive milestone.


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

Read the v0.3 research report and proposal prelude first, then the two v0.2 reports and the archived v0.1 proposal/dossier and prior audit. Do not restart broad surveying or treat PBC as MJ replication. Raw public PBC records are not bundled; the private package retains source hashes and reproduction instructions. Original source scripts and terminal-visit data remain important gaps. The older survey run metadata still has a running entry; do not infer an active worker or invent its missing end time.

## Research rule

Problem first. Information second. Method last. No MJ model improvement, causal relationship, biological mechanism, broad transportability or top-conference novelty is asserted by this checkpoint.
