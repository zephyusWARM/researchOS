# Snapshot

Status: **active — formulation narrowed to privacy-granularity mismatch in latent relational inference**

## Current task

`task-graph-privacy-landscape` — converge on a tractable final-project formulation. Tracking issue: #5.

## Current working title

**Record-Level DP Is Not Topology Privacy: Privacy Granularity in Neural Relational Inference**

## Core insight

NRI learns a latent interaction graph from observational trajectories. If many trajectory records are generated under the same graph, the graph is a **shared/system-level property**, not an individual record.

This creates a privacy-unit mismatch:

- **trajectory-record adjacency:** one observed trajectory is changed or removed;
- **topology adjacency:** the underlying interaction graph changes by one edge.

A record-level DP mechanism only promises indistinguishability under the first relation. It should not automatically be interpreted as protecting the second.

This is consistent with broader privacy literature: AISTATS 2023 explicitly treats global properties aggregated over many records as a privacy object distinct from individual-record privacy and develops distribution-privacy mechanisms rather than relying on crude group DP.

## Why this is stronger than the earlier H1/H2

The 2026-09-29 red-team found the broad H1/H2 spaces crowded:

- node-DP vs membership attacks already appears in GAP;
- edge-DP vs graph-level topology inference is already studied;
- graph unlearning already includes neighborhood influence, affected-neighbor methods, unlearning inversion, and post-unlearning membership attacks.

The latent-topology direction survives as a narrower question because it asks whether the **privacy unit itself is mis-specified** when relational structure is a shared latent variable.

## Historical boundaries

This is not a claim that topology privacy is new.

- ACC 2015 protects consensus-network topology with a topology-adjacent DP mechanism.
- IEEE TIFS 2023 treats latent graph structure as private information.
- AISTATS 2023 distinguishes protection of global dataset properties from individual-record privacy.
- NRI (ICML 2018) makes the underlying interaction graph an explicit learned latent variable.

The candidate contribution is the intersection: modern neural relational inference + explicit privacy granularity + privacy–identifiability–prediction trade-off.

## Minimal course experiment

Use the 5-particle spring benchmark.

- same latent graph (G), many trajectories;
- non-private NRI;
- trajectory-record-level DP-SGD NRI;
- sweep epsilon and number of trajectories;
- utility = trajectory prediction MSE;
- topology leakage/identifiability = edge accuracy/AUROC and posterior entropy.

If graph recovery remains useful under record-level DP, the correct interpretation is not “DP failed”; it is that record-level DP was not a topology-privacy guarantee.

## Main unresolved question

Can a useful **topology-adjacent** formal guarantee be adapted to nonlinear NRI dynamics, or should the course contribution stop after rigorously demonstrating the granularity mismatch and use topology perturbation only as an empirical baseline?

## Next action

Prepare an instructor-facing one-page formulation and verify:
1. per-trajectory DP-SGD accounting assumptions for NRI;
2. whether a directly comparable NRI/topology-privacy paper exists;
3. small-system compute/runtime;
4. whether topology adjacency can be bounded without turning the project into a full theory paper.
