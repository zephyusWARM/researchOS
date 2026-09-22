# Program — Graph Privacy

## Mission

Build a durable, primary-source-backed map of **privacy in graph and relational machine learning**, then turn it into experimentally tractable final-project hypotheses for NTU's *AI Privacy: Theory and Practice*.

The program keeps four questions separate:
- **what is protected** — edge/relation, node/entity, attributes, topology, or whole graph;
- **what is released** — parameters, embeddings, predictions, diffusion outputs, synthetic graphs, or an unlearned model;
- **what the adversary wants** — membership, links, attributes, topology, or reconstructed structure;
- **what guarantee is claimed** — formal DP, certified unlearning, cryptographic confidentiality, or empirical attack resistance.

## Core questions

- Why does graph dependence make ordinary i.i.d. privacy reasoning fail or become loose?
- How do edge/relation-level and node/entity-level adjacency definitions change sensitivity and utility?
- Which stages create coupling: message passing, aggregation, graph diffusion, relation sampling, pretraining, or fine-tuning?
- When do formal guarantees line up with empirical leakage under a matched threat model?
- How should certified graph unlearning be evaluated relative to membership/link/reconstruction attacks?
- Does privacy of a **latent or inferred graph** create a useful bridge to relational-structure inference / NRI?
- Which graph pre-trained/foundation-model privacy questions are genuinely new?

## Course objective

Team membership is due 2026-10-05. The near-term goal is therefore a defensible problem formulation plus a reproducible experiment plan before the instructor discussion.

## Source and persistence policy

Prefer original proceedings/papers and first-party repositories. Surveys are coverage checks, not substitutes for primary evidence. GitHub is durable state, not a browsing log: persist coherent epistemic deltas only.
