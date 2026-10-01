# Working Formulation — Two Privacy Settings for Neural Relational Inference

## Correction to the previous formulation

The canonical NRI synthetic dataset does **not** hold one interaction graph fixed across all trajectory examples. The official generator samples a fresh spring-edge matrix for each simulation.

Therefore the privacy problem must be split.

## Setting A — canonical NRI / per-instance topology

Each trajectory (x_i) has its own latent graph (G_i).

Research question:

> A DP-trained NRI may protect the influence of training trajectory (x_i) on model parameters, but what protects the latent topology of a fresh private inference query (x_*) when the encoder explicitly outputs (q(G_*mid x_*))?

This is primarily an **inference-time/query privacy** problem.

Minimal experiment:
- use canonical NRI data;
- train a standard model;
- evaluate topology leakage from released edge posterior / latent representation;
- add an output/query privacy mechanism or empirical perturbation baseline;
- evaluate edge recovery vs dynamics prediction.

## Setting B — fixed-system / shared topology

One graph (G) generates many trajectories under different initial conditions/noise.

Research question:

> Does trajectory-record-level DP meaningfully protect a shared latent topology that is repeatedly expressed across many trajectory records?

This is a **privacy granularity / global-property** problem.

Minimal experiment:
- modify the spring simulator to draw one (G);
- generate many trajectories from that same (G);
- compare non-private vs trajectory-record-level DP training;
- measure membership privacy separately from topology recoverability;
- vary epsilon and number of trajectories.

## Formal extension

For Setting B, define topology adjacency directly between (G,G'), potentially one edge apart or bounded in a graph/operator norm.

For Setting A, define query/output privacy carefully if releasing inferred relations.

Do not conflate:
- edge/node DP on an observed training graph;
- whole-graph-as-record DP;
- training-record DP;
- global topology privacy;
- inference-query privacy.

## Falsification

The line should be narrowed or abandoned if:
- a direct NRI/topology-privacy precedent is found;
- no measurable distinction exists between record membership protection and topology recoverability in Setting B;
- useful inference-time privacy in Setting A destroys relational/dynamics utility immediately;
- topology adjacency yields only vacuous bounds under realistic nonlinear dynamics.
