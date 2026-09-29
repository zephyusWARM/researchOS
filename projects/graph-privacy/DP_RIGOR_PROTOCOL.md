# DP Rigor Protocol

This protocol is mandatory for every differential-privacy claim, theorem, comparison, implementation, or literature summary in this project.

## Principle

Authority is not evidence. A paper may be written by excellent researchers, appear at a top venue, or be widely cited and still contain a mistake, hidden assumption, incorrect conversion, mismatched adjacency relation, or implementation/accounting gap.

Therefore no statement is accepted merely because a paper states it. Every DP claim must be reconstructed from definitions.

## 1. Define the neighboring relation first

Before writing any privacy guarantee, state exactly what D ~ D' means.

Examples that must never be conflated:
- add/remove one record;
- replace-one record;
- add/remove one node and incident edges;
- add/remove one edge;
- change one entity and all relations containing it;
- replace one whole graph in a multi-graph dataset;
- change one latent interaction edge;
- change one inference query;
- group adjacency.

If two papers use different adjacency relations, their epsilon values are not directly comparable without additional analysis.

## 2. State the randomized mechanism and release surface

Write down M explicitly. Clarify:
- what randomness is internal to the mechanism;
- what is conditioned on;
- what exactly is released;
- whether preprocessing, sampling, clipping, graph propagation, and postprocessing are inside or outside M;
- whether multiple releases occur.

Training privacy, model-release privacy, query privacy, and topology privacy are different release surfaces.

## 3. State the exact privacy definition

For (epsilon, delta)-DP, write the universal quantifiers over adjacent datasets and measurable output events.

For RDP, state:
- order alpha > 1;
- direction of the Renyi divergence;
- whether the definition is required for both ordered adjacent pairs;
- support / absolute-continuity conditions;
- convention used for D_alpha;
- whether limits such as alpha -> infinity are invoked and under what conditions.

Never silently swap pure DP, approximate DP, RDP, zCDP, f-DP, or privacy-loss random-variable formulations.

## 4. Audit every quantifier

For every theorem, rewrite:
- for all adjacent D,D';
- for all measurable S, if relevant;
- for all / some alpha;
- for all mechanism randomness;
- for all clipping-bounded inputs;
- over which sampling randomness and conditioning events.

A large fraction of privacy proof errors are hidden quantifier errors.

## 5. Check support before likelihood ratios or Renyi divergence

Before manipulating log(p(x)/q(x)) or D_alpha(P||Q), verify the relevant absolute-continuity/support assumptions.

Do not divide by zero, take a log of an undefined ratio, or move from event-wise probability bounds to pointwise density ratios without stating the condition that permits it.

For discrete and continuous outputs, keep probability-mass and density arguments distinct.

## 6. Re-derive conversions

Never quote a DP<->RDP, RDP->(epsilon,delta)-DP, zCDP->DP, or composition conversion without checking:
- parameter convention;
- adjacency convention;
- range of alpha;
- optimization over alpha;
- whether the bound is tight, asymptotic, or merely sufficient;
- whether a logarithmic term is missing;
- whether the result assumes pure or approximate DP;
- whether both directions are actually proved.

If a theorem is 'if and only if', prove both directions separately.

## 7. Composition and subsampling require their own proof obligations

Before using composition/accountants, state:
- independent/adaptive composition assumptions;
- whether the same individual/entity appears in multiple steps;
- sampling scheme: Poisson, uniform without replacement, with replacement, graph-dependent, relation-dependent;
- whether amplification-theorem assumptions match that sampling scheme;
- whether clipping is per-record, per-node, per-entity, per-edge, or per-relation;
- whether samples are independent or structurally coupled.

Do not import an iid DP-SGD accountant into relational/graph sampling without justification.

## 8. Sensitivity must match the protected unit

Write the exact sensitivity supremum over the stated adjacency relation.

For graphs, explicitly check dependence on:
- degree;
- number of incident edges;
- message-passing radius;
- graph depth;
- repeated entity frequency;
- trajectory length;
- dynamical stability/contraction;
- normalization operators.

Never assume a sensitivity bound from edge adjacency remains valid for node/entity/topology adjacency.

## 9. Distinguish formal guarantees from empirical attacks

A successful membership, inversion, topology, or property attack does not automatically refute a DP theorem if the attack target is outside the theorem's protected unit/release model.

Conversely, satisfying a formal DP guarantee does not imply resistance to every empirically interesting attack.

Every empirical audit must map protected object <-> attack target.

## 10. Verify implementation against the proof

For code, confirm:
- clipping granularity;
- noise scale and variance/std convention;
- sampling probability;
- batch-size convention;
- accountant implementation;
- number of steps/epochs;
- whether microbatching changes clipping;
- whether graph propagation was precomputed on private topology;
- whether random noise is inadvertently reused;
- independently recompute reported epsilon whenever feasible.

A correct theorem plus mismatched code is not a correct private system.

## 11. Red-team every paper

For every important paper, maintain three layers:
1. Author claim — what the paper states.
2. Verified claim — what survives reconstruction from definitions/proof/code.
3. Open concern — assumptions, gaps, ambiguous conventions, or steps not independently verified.

Use cautious labels: verified; supported but not re-derived; plausible; disputed; contradicted; unverified.

Top venue, famous lab, and citation count never upgrade verification status.

## 12. Minimal proof template

For any new DP theorem/proposal in this project:
1. Specify data domain.
2. Specify adjacency.
3. Specify randomized mechanism.
4. Specify output space.
5. State privacy definition.
6. Fix arbitrary adjacent D,D'.
7. Fix arbitrary measurable event or invoke the divergence definition.
8. Bound the likelihood ratio or divergence.
9. Check support conditions.
10. Account for all randomness.
11. Compose/amplify only with theorem assumptions verified.
12. Convert privacy notions only after re-deriving parameter mapping.
13. Check the reverse ordered pair if required.
14. Test edge cases and limiting cases.
15. Independently reproduce numerically when possible.

## 13. Graph/NRI-specific mandatory questions

Before claiming privacy in relational inference, answer:
- Is topology observed or latent?
- Is the graph fixed across examples or resampled per example?
- What is the private object: trajectory, node, entity, relation, graph, latent edge, or query?
- Is privacy about training data or inference-time input?
- Does changing one private object alter many messages/relations/trajectories?
- Does the mechanism expose an edge posterior directly?
- Does formal adjacency correspond to the attack target?
- If topology is a shared generative parameter, is record-level DP even the intended notion?

## 14. Research OS gate

No DP claim may enter a supported state solely from an abstract.

For theorem-level claims, prefer one of:
- primary proof manually reconstructed;
- primary proof plus independent reproduction;
- multiple independent sources agreeing on the same convention and result.

If not completed, mark the claim as proposed, plausible, disputed, contradicted, or unverified, and record the missing proof obligation.

The goal is not paranoia. The goal is to make every symbol in the privacy statement auditable.
