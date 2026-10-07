# SNAPSHOT

Updated: 2026-10-07 16:18 +08:00

## Current state

Research line initialized with a first evidence-backed frontier scan. Seven high-signal sources and seven bounded evidence records are attached. Four empirical claims are promoted to supported status; one strategic prioritization claim remains proposed pending broader coverage.

## First-pass synthesis

1. **Static complex prediction has improved dramatically, but is not equivalent to solving protein–ligand modeling.** AlphaFold 3 expanded joint all-atom prediction to proteins, nucleic acids, small molecules, ions and modified residues. PoseBench and FoldBench show that performance still degrades on novel binding poses / low-similarity ligands and that apo-to-holo, blind-pocket and multiligand settings remain challenging.
2. **Binding-affinity leaderboards are unusually vulnerable to data similarity and leakage.** CleanSplit-style re-evaluation caused large drops for several existing models, so random or structurally overlapping splits are not credible evidence of transferable binding physics.
3. **Dynamics / conformational ensembles are a deeper frontier than a single predicted structure.** Proteins occupy interconverting ensembles linked to recognition, catalysis and allostery; current static predictors do not provide full ensemble distributions, and scalable atomistic ground truth is itself scarce.
4. **3D generation is far from solved in medicinal-chemistry terms.** Independent benchmarks report structural-validity/conformation failures, and the 2026 MolGenBench evaluation of 17 methods finds weak virtual-screening performance, limited target-specific bioactive coverage, risky motifs and reduced generalization to unseen proteins.
5. The working research thesis is therefore: **the highest-value frontier is shifting from “can a network encode 3D geometry?” toward “can a model learn transferable, dynamic and physically meaningful protein–ligand behavior under hard evaluation?”**

## What is NOT yet established

- A complete ranking of equivariant architectures or 3D foundation models.
- Whether ensemble-aware modeling is the best master's-scale project.
- Which public dataset gives the cleanest entry point for a publishable project.
- How much explicit water, protonation, ion treatment, entropy or long-range electrostatics explains current failures.
- Whether a benchmark/data-centric project would dominate a new model contribution in expected impact per unit effort.
- Prospective wet-lab hit-rate evidence across current 3D generative systems.

## Immediate next durable action

Phase 2 should expand the evidence graph across:
1. physical chemistry failure modes (water, protonation/tautomer, entropy, electrostatics);
2. conformational sampling / induced fit / cryptic pockets;
3. leak-proof and temporal benchmark design;
4. experimental/prospective validation of structure-based generative models;
5. concrete project candidates with datasets, baselines, compute budget, falsifiable hypotheses and venue fit.

Do not select a thesis direction until these five universes have been red-teamed.
