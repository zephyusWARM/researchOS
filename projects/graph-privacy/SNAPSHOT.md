# Snapshot

Status: **active — bootstrap landscape established; project selection not frozen**

## Current task

`task-graph-privacy-landscape` — reconstruct the 2019–2026 graph-privacy landscape and identify tractable final-project hypotheses. Tracking issue: #5.

## Current conceptual map

The strongest organizing axis is **privacy unit × dependency mechanism × release surface**, not simply "which GNN uses DP."

A node/entity or relation can influence many neighborhood aggregations, diffusion steps, gradients, or coupled relation samples. This makes adjacency definition and sensitivity control central.

Current lanes:
1. formal graph/GNN DP;
2. attacks and auditing;
3. private relational / pretrained learning;
4. graph unlearning;
5. graph pre-trained/foundation-model privacy.

## Instructor-relevant lineage

Eli Chien's graph-privacy line is a useful local anchor:
- 2023: multigranular topology protection for decoupled graph convolutions;
- 2024: differentially private graph diffusion;
- 2025: private graph-relational learning for pretrained/LLM fine-tuning;
- 2025: entity-level DP for relational learning.

This is not treated as the whole field.

## Initial project hypotheses

**H1 — Formal privacy granularity vs matched empirical leakage.** Cross edge/relation- and node/entity-level guarantees with link-stealing and membership-inference attacks. Ask whether leakage tracks the object the guarantee actually protects.

**H2 — Audit graph unlearning beyond the deleted item.** Compare certified and approximate graph unlearning using attacks on the deleted node/edge and structurally affected neighbors.

**H3 — Privacy of latent relational-structure inference.** Bridge to NRI: infer a sensitive interaction graph from trajectories and study the privacy–identifiability tradeoff or leakage from released relation posteriors.

**H4 — Privacy auditing for graph pre-trained models.** Reproduce/extend recent membership-auditing work across domains or text-attributed graphs.

## Current operational judgment

H1 and H2 should be stress-tested first for course-sized reproducibility and novelty. H3 is the strongest bridge to the existing NRI line but has higher theory/scope risk. H4 is current but may be compute-heavy. This is a work-prioritization judgment, not a scientific result.

## Next action

For H1/H2, identify exact open-source baselines/datasets, normalize protected units and threat models, estimate compute, and search 2025–2026 work specifically to falsify novelty before discussing the project with the instructor.
