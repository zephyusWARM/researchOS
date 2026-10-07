# SNAPSHOT

Updated: 2026-10-07 — Phase 2 deep-survey checkpoint

## Current state

The research line has moved from a first-pass frontier map to a red-teamed problem hierarchy.

**Central conclusion:** the hardest part of protein–ligand 3D ML is no longer merely encoding 3D geometry. The unresolved core is learning transferable ligand-conditioned state changes and ensemble/thermodynamic behavior under leakage-resistant, deployment-realistic evaluation.

## High-confidence findings

1. Static all-atom complex prediction is strong but not equivalent to de novo molecular recognition. Post-cutoff Runs N' Poses evidence points to pose memorization; PoseBench shows persistent difficulty on blind/apo/novel/multiligand settings.
2. Pose correctness and receptor-state correctness are distinct. KinConfBench finds weak coupling between ligand-pose geometry and correct kinase state, plus mode collapse and apo drift.
3. Affinity evaluation remains highly leakage-sensitive. CleanSplit and LP-PDBBind independently show that similarity control changes conclusions; a 2026 target-mirroring preprint raises an additional red-team warning about sequence-only split rules.
4. Deployment structures matter. Structure-based affinity models degrade when crystal inputs are replaced by apo, docked, predicted or cofolded inputs.
5. ML plus physics is a credible frontier. An unseen-GPCR study shows physics-based refinement can rescue consequential local cofolding errors and downstream free-energy behavior.
6. Ensemble ML is progressing but coverage, probabilities and kinetics must be separated. BioEmu is a strong positive counterexample; reviews still identify thermodynamic weighting, kinetics, environmental dependence and benchmarking as open.
7. 3D generation is not solved by valid geometry. MolGenBench reports weak target awareness, bioactive-space coverage and unseen-protein generalization across 17 methods.
8. Data quality and negative supervision are central. Target 2035 treats standardized positive/negative binding data as foundational; PLINDER operationalizes similarity-aware structural evaluation.

## Preliminary ranking

1. Ligand-conditioned state failure / apo drift in cofolding.
2. Decompose the real incremental value of 3D under leakage-resistant affinity evaluation.
3. Uncertainty-gated hybrid ML → physics refinement.
4. Ensemble-aware docking value map.
5. Functional-failure confidence / calibration.
6. Protonation/water/tautomer robustness.
7. Hard-OOD target-aware generation.
8. Binding-kinetics learning.

The ranking is provisional, not a thesis lock.

## Strongest conceptual model

Treat a protein–ligand system as a distribution over coordinates, conformational state and physical microstate conditioned on molecular identity and environment. Static pose prediction only covers a slice of this object. Affinity/selectivity depend on ensemble free energies; kinetics additionally depends on transition barriers.

## Immediate next durable action

Run a reproducible KinConfBench-centered pilot using released outputs: quantify apo drift, state error, sample diversity and confidence; stratify by post-cutoff novelty and ligand/state class; test whether ensemble disagreement and cheap physicochemical diagnostics predict failure; then seek at least one non-kinase replication.

In parallel, complete the open-source hybrid-physics feasibility audit and the physical-microstate evidence gap.
