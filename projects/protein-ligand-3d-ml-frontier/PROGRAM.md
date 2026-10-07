# PROGRAM

## Core question

As of 2026-10-07, what are the genuinely unsolved problems in 3D machine learning for small-molecule drug–protein systems, and which research directions remain scientifically important, empirically defensible, and realistically attackable rather than being another incremental geometric-network variant?

## Scope

Primary scope:
- small-molecule–protein interaction structure
- blind docking and cofolding
- binding pose and binding-affinity prediction
- apo → holo / induced-fit behavior
- conformational ensembles and protein/ligand dynamics
- structure-based 3D ligand generation and lead optimization
- physically informed representations, scoring and simulation
- dataset construction, benchmark design, OOD evaluation and uncertainty

Adjacent topics are included only when they directly constrain drug–protein 3D ML: protein structure prediction, molecular dynamics, ML force fields, water/ion/protonation effects, free-energy methods, protein design and experimental structural biology.

## Central working hypothesis

The field's bottleneck has shifted. Encoding 3D coordinates and respecting Euclidean symmetries are necessary but are no longer the whole frontier. The harder problems are whether models generalize to new pockets and chemotypes, represent receptor flexibility and conformational ensembles, learn binding energetics rather than dataset similarity, preserve physical/chemical validity, and produce experimentally useful molecules.

This is a working hypothesis to be stress-tested, not a premise to protect.

## Research axes

1. Representation: 2D molecular graphs, 3D coordinates, equivariance, chirality, local/global geometry.
2. Complex structure: docking, cofolding, pocket finding, apo-to-holo, multiligand complexes.
3. Scoring: affinity, ranking, virtual screening, selectivity, uncertainty.
4. Dynamics: conformational ensembles, induced fit, cryptic pockets, kinetics and sampling.
5. Physics: solvation, water, ions, protonation/tautomer states, electrostatics, entropy, long-range interactions.
6. Generation: pocket-conditioned 3D generation, lead optimization, synthesizability and target specificity.
7. Data/evaluation: PDBbind/BindingMOAD/PLINDER-like corpora, leakage, similarity, temporal split, experimental negatives.
8. Translation: prospective validation, hit rates, medicinal-chemistry usefulness and closed-loop design.

## Evidence rules

1. Prefer peer-reviewed primary papers, challenge/benchmark papers, major reviews and official datasets.
2. Record exact evaluation conditions: holo vs apo input, crystal vs predicted receptor, known vs unknown pocket, single vs multiple ligands, ligand/protein similarity to training data.
3. Never equate pose RMSD with affinity, affinity with biochemical activity, or activity with drug usefulness.
4. Treat random splits as weak evidence for generalization unless protein/pocket/ligand similarity is audited.
5. Treat benchmark leakage and near-duplicate structural similarity as first-class confounders.
6. Separate static-structure accuracy from conformational-ensemble accuracy.
7. Track chemical validity, steric clashes, stereochemistry, protonation/tautomer state, water/ions and interaction fingerprints when relevant.
8. For generative models, require more than validity/novelty/docking-score surrogates: target awareness, realistic 3D conformations, synthesizability and ideally experimental activity.
9. Architecture novelty is low priority unless it attacks a documented failure mode.
10. Preserve negative results and benchmark failures.

## Initial candidate directions

These are hypotheses for later red-team, not final recommendations:

1. Ensemble-aware / receptor-flexible protein–ligand prediction under true OOD splits.
2. Reliable affinity or virtual-screening models with leakage-resistant splits and calibrated uncertainty.
3. 3D generative models constrained by physical validity, target-specific interactions and synthesizability.
4. Hybrid ML + physics approaches for water, protonation, long-range electrostatics or free-energy-sensitive ranking.
5. Benchmark/data work that reveals where current cofolding/docking systems fail on novel pockets, apo structures and multiligand settings.

## Anti-goal

Do not start from “I want to use GNN / Transformer / diffusion.” Start from a failure mode whose existence is supported by evidence, then ask what representation or method is required.
