# Coverage

Minimum coverage before project selection:

- **Privacy unit:** edge/relation, node/entity, attributes/features, topology, whole graph, multigranular definitions.
- **Learning/release surface:** message-passing and decoupled GNNs, graph diffusion, node/link tasks, relational learning, text-attributed graphs, pretrained/LLM fine-tuning, graph pre-trained/foundation models, dynamic graphs, synthetic graph release.
- **Attacks/auditing:** membership inference, link stealing, attribute/property inference, topology reconstruction/model inversion, white-box vs black-box assumptions.
- **Defenses:** DP-SGD/clipping, aggregation perturbation, topology perturbation, diffusion-specific privatization, relation/entity-aware clipping/sampling, federated/cryptographic approaches.
- **Unlearning:** edge/node/feature deletion, approximate vs certified unlearning, scalability, post-unlearning leakage.
- **Evaluation validity:** degree sensitivity, propagation radius, coupled sampling, amplification assumptions, matched utility/privacy units, matched attack targets, code/data/compute feasibility.
- **NRI bridge:** privacy when the latent interaction graph itself is sensitive; privacy–identifiability tradeoff; leakage from released relation posteriors.

## Adversarial checks

1. Formal DP does not automatically answer every graph-privacy attack.
2. Epsilon values under different adjacency definitions are not directly comparable.
3. Attack results are meaningful only when the leakage target matches the claimed protected unit.
4. Do not over-center Eli Chien's lab merely because it is course-relevant.
5. Red-team novelty against 2025–2026 work.
6. Check whether homophily, degree, or train/test construction artificially creates attack signal.

## Stop condition

Stop the survey phase only when the taxonomy is stable under new searches and at least two project hypotheses survive novelty, reproducibility, compute, and falsifiability checks.
