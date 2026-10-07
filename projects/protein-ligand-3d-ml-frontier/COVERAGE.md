# COVERAGE

Cutoff: **2026-10-07**

This ledger tracks what has actually been investigated. “Not found” never means “does not exist.”

| Universe | Required coverage | Current state |
|---|---|---|
| A. 2D graph vs explicit 3D representation | when 3D helps, when conformers add noise, multimodal baselines | partial; explicit controlled 2D-vs-3D audit still needed |
| B. Geometric/equivariant architectures | SE(3)/E(3), chirality, local/global geometry, scalability | partial; sufficient for frontier triage, not architecture ranking |
| C. Docking / cofolding / pocket prediction | holo, apo→holo, blind pocket, multiligand, novel pose, post-cutoff | deep-scanned: AF3, PoseBench, Runs N' Poses, KinConfBench, GPCR and ion-channel stress tests |
| D. Binding affinity / scoring / virtual screening | leakage, target/ligand/pocket OOD, ranking, uncertainty, deployment inputs | deep-scanned: CleanSplit, LP-PDBBind, target-mirroring red-team, computed-input robustness |
| E. Dynamics / conformational ensembles | ensemble prediction, induced fit, cryptic pockets, thermodynamic weighting, kinetics | deep-scanned conceptually; BioEmu + 2026 ensemble reviews; drug-bound cross-family benchmark still missing |
| F. Physical chemistry | water, ions, protonation, tautomers, entropy, electrostatics, long-range, free energy | broad scan complete; hybrid/free-energy evidence strong, variable-by-variable attribution remains open |
| G. 3D molecule generation / lead optimization | target awareness, validity, conformation, synthesizability, activity | deep-scanned at benchmark level: 2025 independent benchmark + 2026 MolGenBench; method-by-method lineage partial |
| H. Data infrastructure / benchmarking | PDBbind, CleanSplit, LP-PDBBind, PLINDER, temporal splits, negatives | deep-scanned for core resources |
| I. Prospective / experimental validation | real hit rate, medicinal-chemistry utility, assay confirmation | partial: positive wet-lab examples exist; recent reviews still describe field-wide prospective validation as scarce |
| J. Research opportunity selection | clean problem statements, datasets, baselines, compute, venue | Phase-2 preliminary ranking complete; pilot evidence required before topic lock |

## Required saturation checks before selecting a project

- protein/pocket/ligand/series similarity-aware splits
- temporal / post-cutoff evaluation
- ligand-only, protein-only and nearest-neighbor baselines
- crystal/holo versus predicted/apo receptor inputs
- known pocket versus blind docking
- single ligand versus cofactors/multiligand
- pose RMSD versus functional-state correctness
- structural accuracy versus interaction fingerprints / physical validity
- affinity correlation versus ranking/enrichment
- confidence calibration and selective failure detection
- receptor/ligand flexibility and ensemble coverage
- ensemble populations versus mere diversity
- water/protonation/tautomer/ion sensitivity
- stereochemistry and chemical validity
- synthesizability and medicinal-chemistry filters
- prospective experimental evidence
- computational cost and reproducibility
