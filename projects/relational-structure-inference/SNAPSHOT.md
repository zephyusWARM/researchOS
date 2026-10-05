# Snapshot

Updated: 2026-10-05 16:32 +08:00

Status: **trajectory-level privacy audit active; release-surface split identified**

The original lineage-mapping task remains open. A focused subtask, `task-nri-trajectory-privacy`, is active because the privacy formulation has become a materially separate research question.

## Current privacy formulation under audit

Candidate privacy unit: one complete simulation / trajectory record.

Candidate raw-data adjacency: replacement or add/remove of one complete trajectory while the rest of the training corpus is unchanged.

Candidate training mechanism: a DP-compatible variant of NRI trained with per-record gradient clipping plus calibrated Gaussian noise, with formal accounting across all optimization steps.

### Release surface is now split into two distinct targets

**Target A — private training / model release.** Release trained encoder/decoder parameters, with trajectory-level DP protecting the influence/membership of each training trajectory.

**Target B — private latent-relation inference.** Release an inferred graph or edge distribution for a private trajectory, e.g. `q_phi(z | x_i)`.

Target B is not automatically protected by Target A. Even if the learned parameters `phi` are DP, computing and releasing `q_phi(z | x_i)` for a private record directly accesses `x_i` again. Standard DP post-processing only applies when the post-processing receives the DP output and public/non-private inputs; it does not cover fresh access to the protected raw record.

This distinction is now a central problem-formulation axis, not an implementation detail.

These are **working hypotheses, not yet promoted claims**. In particular, the fact that the original implementation batches simulations does not by itself establish that a trajectory is the semantically correct privacy record.

## Verified implementation blockers / obligations in original NRI

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

### 4. The original scalar NRI loss must be refactored into explicit per-trajectory contributions

Primary code: `ethanfetaya/NRI:train.py` and `utils.py`.

The training loop forms one scalar NLL plus KL loss for the minibatch and calls a
single `loss.backward()`. The NLL/KL expressions are sums over batch entries and are
algebraically separable across simulations once cross-simulation BatchNorm is removed,
so this appears repairable rather than a fundamental obstacle. A DP implementation
must nevertheless verify that clipping is applied to the gradient contribution of
each complete trajectory, including both encoder and decoder paths.

Source: https://github.com/ethanfetaya/NRI/blob/master/train.py

### 5. Validation-based checkpoint selection is outside the training accountant unless handled explicitly

The original training script evaluates the validation set every epoch and releases the
checkpoint with the smallest validation NLL. If the validation trajectories are also
private and are inside the intended privacy universe, this model-selection step is an
additional data-dependent mechanism that is not covered merely by making the training
optimizer DP.

Candidate repairs: use a public validation set, choose a fixed training schedule before
seeing private validation results, or privatize/account for model selection.

Source: https://github.com/ethanfetaya/NRI/blob/master/train.py

### 6. The original DataLoader does not provide the sampling assumptions of a standard subsampled-Gaussian accountant

The original loader instantiates `DataLoader(train_data, batch_size=batch_size)`
without randomized/Poisson sampling. A privacy accountant must match the actual
sampling scheme. A DP library may replace the loader with Poisson sampling, or the
analysis must use a guarantee appropriate to the implemented sampler. Simply adding
Gaussian noise to the original optimizer and plugging the batch fraction into a
Poisson-subsampling accountant would be unjustified.

Source: https://github.com/ethanfetaya/NRI/blob/master/utils.py

## Positive implementation finding

Apart from the BatchNorm layers, the encoder/decoder message passing mixes **objects
within a simulation**, not simulations with each other. The minibatch NLL and KL are
also separable across simulations. Therefore the current evidence points to
DP-compatible architectural surgery being feasible; the project is not blocked by an
intrinsically cross-trajectory NRI computation.

## OpenGU / graph-unlearning boundary

OpenGU is classified as an **adjacent privacy line, not a direct DP precedent**.

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

### OpenGU code audit notes

The current repository is useful primarily as a **taxonomy / benchmark reference**,
not as an implementation base for DP-NRI. Its code is organized around observed static
PyG-style graphs and node/edge/feature deletion requests. The method manager integrates
16 GU methods, but method support is not uniformly symmetric across all requested
task/request combinations. For example, the generic learning-based pipeline currently
disables its node MIA call with an `and False` guard and comments out edge MIA,
whereas the IF-based pipeline invokes node MIA. The public issue tracker also records
configuration ambiguity, stale/generated unlearning-request files, installation
problems, and a missing ScaleGUN propagation module.

The final NeurIPS 2025 paper reports 10 conclusions, while the current GitHub README
still says 8, indicating paper/repository drift. Treat the final paper as canonical for
scientific conclusions and the repository as an implementation artifact.

## Strongest adjacent DP precedent identified so far

Chien et al., NeurIPS 2023, **Differentially Private Decoupled Graph Convolutions for
Multigranular Topology Protection**, introduces Graph Differential Privacy (GDP) and a
`k`-neighbor-level adjacency that interpolates between edge- and node-level topology
protection while also protecting node features/labels. It protects both learned model
weights and predictions.

This is a serious adjacent precedent, but not yet a direct match:
- DPDGC starts from an **observed graph dataset** `D=(X,Y,A)`.
- NRI starts from **trajectories** and infers the interaction graph as a latent variable.
- DPDGC adjacency changes one observed node's attributes/label and up to `k` incident
  adjacency entries.
- Candidate NRI trajectory adjacency changes one entire dynamical record containing
  multiple entities over time.
- If our desired release is a private inferred graph for that record, training-time
  model DP alone is insufficient and a separate inference-time mechanism is required.

Source: https://papers.nips.cc/paper_files/paper/2023/hash/8e3db2040672d85fd12e6313945594fe-Abstract-Conference.html

## Direct-precedent status

No exact-match paper has yet been identified that simultaneously has:
1. NRI-style latent interaction-graph inference from observed trajectories,
2. a formal trajectory-record DP adjacency,
3. DP training/release of the relational model, and
4. a formal privacy guarantee for released latent relations of private trajectories.

This is **not a novelty claim**. Search is ongoing across trajectory DP, private
structure learning/causal discovery, private dynamical-system identification, DP
representation/inference, multi-agent trajectory prediction, and graph DP.

Important adjacent results already identified include trajectory-wise DP in multi-agent
RL, DP trajectory synthesis/publication, DP trajectory-prediction models, private
Markov-random-field structure learning, DP causal graph discovery, and DP inference /
private representation mechanisms. Therefore neither “trajectory-level DP” nor “DP
structure learning” is itself novel.

## Immediate next actions

1. Decide whether the primary scientific target is model/training privacy, private
   latent-graph release, or a multigranular combination. Do not merge them implicitly.
2. Search the remaining direct-precedent space, especially private latent-structure
   inference from sequential/multi-agent data.
3. Formalize the raw adjacency relation(s): complete trajectory, one agent's entire
   time series, and/or one latent/observed relation, then determine which are coherent
   for the intended application.
4. Specify DP-compatible NRI surgery: replace BatchNorm, use public/fixed normalization
   bounds, expose per-trajectory losses, use accountant-compatible sampling, and remove
   non-private validation selection.
5. Decide whether the contribution is nontrivial enough for a paper. A plain
   “NRI + DP-SGD” implementation is currently judged too weak; the strongest surviving
   angle is the privacy semantics of latent relational inference and its multiple
   release surfaces/granularities.

## Persistence rule for this run

Persist again when one of the following happens: the privacy formulation changes,
a direct precedent materially threatens novelty, a proof/implementation blocker is
resolved, or a go/no-go research decision is reached. Routine browsing is not a commit
boundary.
