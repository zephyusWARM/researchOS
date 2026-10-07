# SNAPSHOT

Updated: 2026-10-07 16:10 +08:00

## Current state

Research line initialized. The first checkpoint establishes that strong all-atom complex prediction does not imply robust OOD protein–ligand modeling, and that binding-affinity evaluation can be badly distorted by dataset leakage. Dynamics, physical chemistry and generation are scheduled for the next evidence expansion.

## First-pass synthesis

- AlphaFold 3 marks a major step in static all-atom biomolecular complex prediction.
- PoseBench shows that new binding poses, apo-to-holo inputs, uncommon targets and multiligand cases remain challenging, including a tension between structural accuracy and chemical specificity.
- CleanSplit shows that train–test similarity and redundancy can substantially inflate binding-affinity performance.

## Immediate next durable action

Attach evidence for conformational ensembles, similarity-sensitive all-atom benchmarks and 3D generative-model failures, then expand into water/protonation/entropy/electrostatics and prospective experimental validation.
