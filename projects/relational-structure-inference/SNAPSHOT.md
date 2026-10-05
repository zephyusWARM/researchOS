# Snapshot

Updated: 2026-10-05 16:12 +08:00

Status: **trajectory-level privacy audit active; first implementation blockers verified**

The original lineage-mapping task remains open. A focused subtask, `task-nri-trajectory-privacy`, is now active because the privacy formulation has become a materially separate research question.

## Current privacy formulation under audit

Candidate privacy unit: one complete simulation / trajectory record.

Candidate raw-data adjacency: replacement or add/remove of one complete trajectory while the rest of the training corpus is unchanged.

Candidate mechanism: a DP-compatible variant of NRI trained with per-record gradient clipping plus calibrated Gaussian noise, with formal accounting across all optimization steps.

Candidate release surface: at minimum the trained model parameters; any released inferred relations, embeddings, predictions, or downstream artifacts are intended to be treated as post-processing only if they are computed exclusively from a valid DP-trained model and non-private/public inputs.

These are **working hypotheses, not yet promoted claims**. In particular, the fact that the original implementation batches simulations does not by itself establish that a trajectory is the semantically correct privacy record.

## Verified implementation blockers in original NRI

### 1. Batch-dependent layers couple candidate records

Primary code: `ethanfetaya/NRI:modules.py`.

The original `MLP` uses `nn.BatchNorm1d`. Its helper flattens a tensor from
`[num_sims, num_things, features]` to `[num_sims * num_things, features]`
before applying batch normalization. Therefore batch statistics depend jointly on
multiple simulations in a minibatch. The CNN encoder also contains BatchNorm1d.

Consequence: the original architecture is **not directly compatible with the standard
independent-record DP-SGD argument** in which each clipped gradient contribution is
defined from one record. This does not make DP impossible; the architecture must be
changed or the normalization statistics must be handled with a privacy-valid design.

Source: https://github.com/ethanfetaya/NRI/blob/master/modules.py

### 2. Train-wide min/max normalization is data-dependent cross-record preprocessing

Primary code: `ethanfetaya/NRI:utils.py`.

For the standard spring/charged-particle loader, `loc_max`, `loc_min`,
`vel_max`, and `vel_min` are computed from the entire training array and then used
to normalize train/validation/test data. The Kuramoto loader similarly computes
train-wide feature extrema.

Under adjacency defined on the **raw trajectory corpus**, changing one trajectory can
change those extrema and therefore change the transformed values of many/all other
records. A DP-SGD accountant applied only after this transformation does not
automatically establish trajectory-level DP for the raw input dataset.

Candidate repairs include public/fixed physical bounds, deterministic public clipping
followed by a fixed affine transform, or private estimation of normalization
statistics with composed privacy accounting.

Source: https://github.com/ethanfetaya/NRI/blob/master/utils.py

### 3. A trajectory is a natural computational sample, but semantic adjacency is unresolved

The original loader constructs a `TensorDataset(feat_train, edges_train)` whose first
axis is `num_sims`, and the DataLoader batches those simulations. This supports using
one simulation/trajectory as a **computational record** for per-example gradients.
It does not yet prove that this is the scientifically appropriate privacy object for
human/multi-agent/physical datasets.

Source: https://github.com/ethanfetaya/NRI/blob/master/utils.py

## OpenGU / graph-unlearning boundary

OpenGU is currently classified as an **adjacent privacy line, not a direct DP
precedent**.

OpenGU (NeurIPS 2025 Datasets & Benchmarks) standardizes graph unlearning across
node/edge/feature deletion requests, downstream graph tasks, 16 unlearning algorithms,
37 datasets, and 13 GNN backbones. Its reference object is an updated model after a
specific deletion request, compared against retraining on the pruned graph.

Certified Graph Unlearning (Chien, Pan, Milenkovic) is especially relevant because it
explicitly distinguishes certified removal from differential privacy. A DP-trained
model can satisfy a strong one-record deletion stability condition without an
after-the-fact model update, but certified removal permits a deletion-specific update
and can preserve more utility. The same symbols `(epsilon, delta)` can therefore
refer to guarantees over different mechanisms/distributions and must not be conflated.

OpenGU source: https://github.com/bwfan-bit/OpenGU
Certified Graph Unlearning: https://arxiv.org/abs/2206.09140

## Immediate next actions

1. Pin down the raw privacy object, adjacency, threat model, release surface, and
   guarantee before proposing a method.
2. Search direct precedent for DP latent-relation inference, trajectory/time-series
   model training, graph structure learning, causal/structure discovery, and dynamical
   system identification.
3. Compare the strongest relevant graph-DP line, especially multigranular topology
   protection, against trajectory-level NRI privacy.
4. Specify DP-compatible NRI surgery: remove/replace BatchNorm, use public/fixed
   normalization bounds, and verify per-trajectory loss/gradient semantics.
5. Decide whether the resulting research problem contains a nontrivial contribution
   beyond applying standard DP-SGD.

## Persistence rule for this run

Persist again when one of the following happens: the privacy formulation changes,
a direct precedent materially threatens novelty, a proof/implementation blocker is
resolved, or a go/no-go research decision is reached. Routine browsing is not a commit
boundary.
