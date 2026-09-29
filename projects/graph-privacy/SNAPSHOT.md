# Snapshot

Status: **active — deep survey corrected the NRI data model and split the problem into two privacy settings**

## Major correction

Canonical NRI does not use one fixed graph for all synthetic trajectories. The official generator samples a fresh edge graph per simulation/example.

The previous fixed-(G) formulation therefore describes a **modified fixed-system/system-identification setting**, not the canonical NRI benchmark.

## Current map

### Setting A — canonical NRI
- one trajectory/example (x_i);
- one latent graph (G_i);
- graph varies across examples;
- main privacy issue: training-record privacy vs inference-time privacy of a query’s latent topology.

### Setting B — fixed system
- many trajectories share one (G);
- (G) is a global/system-level property;
- main privacy issue: record privacy vs shared-topology privacy.

## Key taxonomy

Five distinct privacy units/release settings must be kept separate:
1. edge/relation privacy;
2. node/entity privacy;
3. whole graph as a training record;
4. shared/global/latent topology privacy;
5. inference-query privacy.

## Current gap signal

Targeted searches through 2026-09-29 found dense adjacent work but no direct primary paper that formulates formal topology privacy specifically for Kipf-style NRI / close neural latent-interaction inference.

This is not proof of novelty.

## Candidate course directions

- **A:** canonical NRI + inference-time topology privacy.
- **B:** fixed-system NRI + record-DP vs topology-privacy granularity mismatch.
- **C:** topology-adjacent formal DP for nonlinear relational inference as a stretch/theory extension.

For instructor discussion, A and B should be presented as distinct settings rather than merged into one claim.

## Next action

Create a one-page protected-object matrix and check implementation feasibility:
- per-example gradients for NRI training;
- fixed-graph data generator;
- topology attack/recovery metrics;
- output perturbation candidate for Setting A;
- sensitivity/stability assumptions for topology adjacency in Setting B.
