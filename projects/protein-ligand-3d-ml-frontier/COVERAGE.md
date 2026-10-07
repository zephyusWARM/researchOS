# COVERAGE

Cutoff: **2026-10-07**

| Universe | Required coverage | Current state |
|---|---|---|
| A. 2D graph vs explicit 3D representation | when 3D helps, when conformers add noise, multimodal baselines | partial |
| B. Geometric/equivariant architectures | SE(3)/E(3), chirality, local/global geometry, scalability | partial |
| C. Docking / cofolding / pocket prediction | holo, apo→holo, blind pocket, multiligand, novel pose | seeded |
| D. Binding affinity / scoring / virtual screening | leakage, protein/ligand/pocket OOD, ranking, uncertainty | seeded |
| E. Dynamics / conformational ensembles | ensemble prediction, induced fit, cryptic pockets, kinetics | next |
| F. Physical chemistry | water, ions, protonation, tautomers, entropy, electrostatics, long-range, free energy | not yet deep-scanned |
| G. 3D molecule generation / lead optimization | target awareness, validity, conformation, synthesizability, activity | next |
| H. Data infrastructure / benchmarking | PDBbind, BindingMOAD, PLINDER-like sets, temporal splits, negatives | partial |
| I. Prospective / experimental validation | real hit rate, medicinal-chemistry utility, assay confirmation | not yet deep-scanned |
| J. Research opportunity selection | clean problem statements, datasets, baselines, compute, venue | pending |

## Required saturation checks before selecting a project

- pocket/protein/ligand similarity-aware splits
- temporal split where possible
- crystal/holo versus predicted/apo receptor inputs
- known pocket versus blind docking
- single ligand versus cofactors/multiligand
- structural accuracy versus interaction fingerprint fidelity
- affinity correlation versus ranking/enrichment
- uncertainty and failure detection
- receptor/ligand flexibility and ensemble coverage
- water/protonation/tautomer/ion sensitivity
- stereochemistry and chemical validity
- synthesizability and medicinal-chemistry filters
- prospective experimental evidence
- computational cost and reproducibility
