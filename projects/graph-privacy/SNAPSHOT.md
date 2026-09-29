# Snapshot

Status: **active — first novelty red-team completed; original H1/H2 narrowed; latent-topology privacy promoted**

## Current task

`task-graph-privacy-landscape` — reconstruct the graph-privacy landscape and converge on a tractable final-project formulation. Tracking issue: #5.

## Material update from the 2026-09-29 red-team

The first two bootstrap hypotheses were more crowded than initially estimated.

### H1 — privacy granularity × empirical leakage

The broad version is **not sufficiently novel as a standalone project**.

- GAP already evaluates node-level DP against node membership inference in addition to formal edge/node privacy.
- CCS 2025 shows that edge-level DP can still be inadequate against graph-level topology inference.
- PETS 2026 shows that graph structure and train/test dependence can invalidate standard intuitions used in membership-inference auditing.

A course project could still reproduce a carefully matched subset, but "build the full matrix" is now treated as a survey/benchmark direction rather than the default research contribution.

### H2 — graph unlearning beyond the deleted item

The broad "look at affected neighbors" idea is also **substantially occupied**.

- GNNDelete explicitly formalizes Neighborhood Influence.
- Adaptive Graph Unlearning identifies architecture-dependent affected neighbors.
- WSDM 2026 unlearning inversion exploits local confidence changes around deleted edges.
- AAAI 2026 shows that unlearned GNNs retain attackable membership imprints.

A genuinely new H2 would need a sharper object, such as a **privacy spillover radius** or a guarantee/audit that quantifies leakage as a function of graph distance from the deletion. Novelty is not yet established.

## Promoted direction — H3: privacy of latent relational structure

The strongest remaining bridge to the existing relational-structure-inference program is now:

> **When trajectories are observed and an NRI-style model infers a latent interaction graph, how much privacy can be given to the latent edges/topology without destroying relation identifiability and dynamics prediction?**

Important historical context:

- Topology privacy from dynamical observations predates NRI: ACC 2015 studied differential privacy for protecting the topology of linear consensus networks from topology identification.
- IEEE TIFS 2023 explicitly treats latent graph structure as private information and studies obfuscation/utility trade-offs.
- NRI (ICML 2018) makes the latent interaction graph an explicit learned variable recovered from trajectories.

This means the project is **not** "nobody has ever thought about topology privacy." The candidate gap is narrower: connect modern neural relational inference / learned latent interaction posteriors to a topology-privacy formulation and measure the privacy–identifiability trade-off.

## Minimal experiment scaffold

Start deliberately small.

1. Use the standard 5-particle spring system with known ground-truth edges.
2. Train/reuse an NRI implementation to recover the latent graph and predict future trajectories.
3. Define the sensitive object explicitly: initially **one latent interaction edge**.
4. Compare non-private release against one or more trajectory/output perturbation mechanisms.
5. Measure at least:
   - edge-recovery accuracy/AUC (privacy leakage / identifiability),
   - trajectory prediction MSE (utility),
   - calibration or entropy of the inferred edge posterior.
6. Only call a mechanism "DP" if the adjacency relation and sensitivity/noise calibration are formally justified. Otherwise label it an empirical privacy perturbation baseline.

The original NRI code is old, but a later reimplementation can run the synthetic system without requiring a GPU, so the first experiment is course-feasible.

## Main unresolved theoretical question

What exactly is the neighboring object?

Candidates:
- **trajectory-record adjacency**: one observed trajectory/example differs;
- **entity adjacency**: one agent and all of its observations/interactions differ;
- **latent-edge/topology adjacency**: the underlying dynamical systems differ by one interaction edge.

The third is the scientifically interesting target, but it is not ordinary DP-SGD adjacency because changing one latent edge can alter an entire generated trajectory distribution. This is the core formulation problem to solve before claiming formal differential privacy.

## Next action

Do a formulation-first pass on H3:

- reconstruct the exact adjacency/noise mechanism used by prior topology-privacy work in dynamical systems;
- determine whether it can be translated to the NRI spring simulator or whether a weaker empirical privacy study is more honest;
- specify the released object (raw trajectories, trained model, inferred edge posterior, or all three);
- design a one-page experiment matrix that can be explained to Eli Chien before expanding implementation.

Team finalization remains due 2026-10-05, so the next durable milestone should be a concrete one-page problem formulation rather than another broad survey.
