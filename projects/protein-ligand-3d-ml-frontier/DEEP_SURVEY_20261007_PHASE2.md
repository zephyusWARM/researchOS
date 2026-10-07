# Phase 2 Deep Survey — 3D ML for Protein–Ligand Systems

Date: 2026-10-07
Status: durable research checkpoint; not a final topic lock.

## Executive verdict

The frontier is no longer well described as "how do we feed xyz coordinates into a GNN?" Geometry-aware representations, equivariant networks, diffusion/cofolding, and all-atom prediction have matured enough that the harder scientific questions have moved upward.

The central unresolved object is transferable molecular recognition: whether a model generalizes to genuinely new proteins, pockets, chemotypes and binding modes; predicts the ligand-conditioned receptor state rather than a dominant structural prior; represents correctly weighted conformational ensembles; connects structure to thermodynamic or kinetic observables; survives apo/predicted/docked input structures; and supports inverse design under experimentally meaningful evaluation.

A useful formal object is a conditional distribution

p(X_protein, X_ligand, state, microstate | protein, ligand, environment)

rather than a single graph plus a single coordinate matrix. Binding free energy is an ensemble quantity, so a visually correct pose is not enough to establish correct molecular recognition.

## What is relatively mature

3D geometric representation is now strong infrastructure. Distances, angles, torsions, point-cloud or surface representations, geometric transformers, equivariant graph networks and equivariant generative models provide effective ways to process molecular geometry. Architecture research still matters, but inability to encode rotations is not the main bottleneck.

Static complex prediction is also strong in favorable regimes. AlphaFold 3, RoseTTAFold-All-Atom, Chai-1, Protenix, Boltz-family models, DiffDock-class systems, DynamicBind and NeuralPLexer demonstrate that deep models can generate useful protein–ligand structural hypotheses. The key question has shifted from "can deep learning dock/cofold?" to "when is the result trustworthy and mechanistically correct?"

BioEmu is important counterevidence to an overly pessimistic view of dynamics. Learned ensemble emulation can already generate many approximate equilibrium samples rapidly and reproduce some functional motions and relative free-energy behavior. The ensemble frontier is moving quickly rather than remaining untouched.

## Failure mode 1 — post-cutoff memorization and OOD generalization

Runs N' Poses evaluates leading all-atom cofolding methods on 2,600 high-resolution protein–ligand systems released after model training cutoffs. It reports substantial reuse or memorization of ligand-pose information from training distributions, limiting de novo generalization.

PoseBench reaches a compatible conclusion from a different benchmark design: blind-pocket, apo/predicted-receptor, novel-pose, uncommon-interaction and multiligand conditions remain materially harder than familiar retrospective settings.

Therefore a docking result is incomplete without auditing protein/pocket/ligand similarity, binding-mode novelty, template exposure and deposition date.

## Failure mode 2 — pose correctness is not receptor-state correctness

KinConfBench evaluates 2,225 high-quality human kinase chains. Boltz-2, Chai-1, Protenix and RoseTTAFold-All-Atom can often produce plausible complexes, yet ligand-pose geometric success does not strongly imply that the kinase conformational state is correct.

Reported failure signatures include roughly 60–80% state-classification accuracy, severe repeated-sampling mode collapse, little induced-fit structural diversity, and "apo drift" toward the ligand-free receptor state. Apo drift becomes stronger on post-cutoff complexes.

This motivates a stronger research hypothesis: modern cofolding models can encode a powerful receptor structural prior without reliably learning the causal response of receptor state to the specific ligand.

## Failure mode 3 — affinity benchmarks can reward similarity and memorization

PDBbind CleanSplit shows substantial train–test structural overlap between historical PDBbind/CASF usage. Similarity-based heuristics can be surprisingly competitive before filtering, and representative affinity models lose performance after de-leaking, while GEMS retains stronger generalization under the stricter setup.

Leak Proof PDBBind independently controls protein and ligand similarity and evaluates transfer to more independent data. A 2026 preprint further raises "target mirroring" as a red-team issue: global sequence thresholds may not eliminate correlated binding behavior, and ligand-only baselines can remain unexpectedly strong. Because that result is not peer reviewed, it is retained as adversarial evidence rather than treated as settled fact.

For this project, no affinity result counts as evidence of learned 3D interaction physics without a ligand-only baseline, similarity audit, retrieval baseline, and hard OOD or temporal split.

## Failure mode 4 — benchmark-to-deployment structure shift

A 2026 JCIM study evaluates five reproducible structure-based affinity pipelines using experimental co-crystals, docked holo receptors, docked apo receptors, predicted receptors and AlphaFold3-cofolded structures. Performance is highest with experimental structures and generally degrades as structural uncertainty enters the pipeline.

This separates two tasks that are often conflated: scoring a near-native complex and building an end-to-end system from realistic inputs.

## Failure mode 5 — ML and physics have complementary errors

A 2026 unseen-GPCR benchmark shows that Boltz can predict receptor backbones well while retaining ligand-pose errors consequential enough to damage downstream free-energy calculations. Physics-based refinement corrects many local errors and restores downstream behavior toward native-structure performance.

A 2026 physical-chemistry perspective gives the conceptual reason: physics-based simulation is expensive and imperfect but is tied to energy landscapes and statistical mechanics; learned generative models are fast and expressive but do not automatically enforce thermodynamic consistency.

This makes ML-versus-physics the wrong framing. The frontier is how to allocate compute and information between learned proposals, uncertainty, refinement, sampling and physical validation.

## Failure mode 6 — "many conformations" is not yet an ensemble solution

Protein ensemble modeling should be separated into three targets:

1. conformational coverage: which states can exist;
2. thermodynamic weighting: what probability each state should receive;
3. kinetics: how rapidly states interconvert and along which pathways.

Many current methods advance the first target. BioEmu and related systems make progress toward the second. General transferable kinetics remains substantially less mature.

For drug discovery this maps naturally onto pose/state generation, affinity/selectivity through free-energy differences, and residence-time or mechanism questions through transition barriers and rates.

## Failure mode 7 — physical microstate and environment remain partly latent

Protein–ligand recognition depends on protonation and tautomer state, hydrogens and charge assignment, structural waters, ions/cofactors, solvent and pH, side-chain or loop rearrangements, desolvation and entropy.

This survey supports their mechanistic importance but does not yet establish benchmark-grade attribution of how much each factor explains current SOTA model failures. The project therefore keeps this as an evidence gap rather than prematurely ranking "water" or "protonation" as the top bottleneck.

## Failure mode 8 — 3D generation can optimize proxies without solving medicinal chemistry

MolGenBench, published 1 October 2026, evaluates 17 leading structure-based generative methods across de novo design and lead optimization. It reports persistent weak virtual-screening performance, limited coverage of target-specific bioactive space, high-risk structural motifs, weak target awareness, and poorer generalization to unseen proteins. Better 3D conformation generation does not automatically produce active molecules.

Independent 2025 benchmarking similarly finds structural-validity and realistic-conformation failures in deep 3D generators. Positive counterexamples exist: CMD-GEN reports wet-lab validated selective PARP1/2 inhibitor design. The balanced conclusion is therefore not that prospective generation never works, but that field-wide prospective validation remains much thinner than in-silico publication volume.

## Data and evaluation may be the bottleneck

Target 2035 explicitly identifies fragmented/non-standardized public bioactivity data and weak inactive supervision as constraints on hit-finding ML. Its roadmap emphasizes standardized positive and negative binding data, experimental metadata, orthogonal confirmation and iterative prediction-to-experiment cycles.

PLINDER attacks the structural-evaluation side with hundreds of thousands of protein–ligand systems, extensive pocket/protein/ligand similarity annotations, linked apo and predicted structures, and test splits stratified by novelty. Its design is directly aligned with the anti-memorization questions of this project.

## Task ladder

| Layer | Core question | 2026 assessment |
|---|---|---|
| Chemical validity | Is the structure chemically and physically plausible? | improved, not guaranteed |
| Geometric representation | Can a model process 3D symmetries and stereochemistry? | relatively mature infrastructure |
| Static pose | Can protein and ligand be placed plausibly? | strong in-distribution; hard OOD remains |
| Ligand-conditioned state | Does the receptor move into the correct functional state? | clearly open |
| Ensemble weights / thermodynamics | Are state probabilities and free energies right? | active frontier |
| Kinetics | Are pathways, barriers and rates right? | immature |
| Inverse design | Are generated molecules target-aware, active, selective and synthesizable? | rapidly advancing but proxy-heavy |
| Trustworthy evaluation | Do gains survive similarity, time and deployment shift? | foundational open problem |

## Red-team rules

- Never say 2D molecular ML is solved.
- Never assume 3D is automatically better than 2D.
- Equivariance is an inductive bias, not proof that physics was learned.
- Many generated structures do not constitute a thermodynamic ensemble.
- Low RMSD does not prove correct receptor state, interaction chemistry or affinity.
- High Pearson correlation does not prove affinity generalization.
- Docking-score improvements do not establish useful de novo drug design.
- Physics-based methods are also approximate; the opportunity is complementary error structure.

## Candidate research problems

| Rank | Candidate | Falsifiable question | Public entry point | Main risk |
|---:|---|---|---|---|
| 1 | Ligand-conditioned state failure / apo drift | Can we predict and correct when a cofolder ignores ligand-induced receptor-state shifts? | KinConfBench, Runs N' Poses, PLINDER apo-holo links | kinase signal may not transfer |
| 2 | What does explicit 3D add after de-leaking? | Under strict similarity/time controls, where does 3D beat ligand-only, sequence and retrieval baselines? | CleanSplit, LP-PDBBind, PLINDER | benchmark space is crowded |
| 3 | Uncertainty-gated ML-to-physics refinement | Can a cheap gate identify complexes where targeted refinement has high value? | GPCR OOD benchmark + open refinement tools | proprietary FEP+ cannot be the only validator |
| 4 | Ensemble-aware docking value map | Which flexible targets actually benefit from receptor ensembles? | BioEmu/other ensemble generators + apo-holo data | ensemble validity and compute |
| 5 | Functional-failure confidence | Can uncertainty predict state/interaction failure rather than only geometry? | KinConfBench and OOD docking sets | could collapse into generic calibration |
| 6 | Protonation/water/tautomer robustness | Does marginalizing plausible microstates improve robustness more than a larger architecture? | curated sensitive subsets | clean ground truth is hard |
| 7 | Hard-OOD target-aware generation | Can target awareness improve without sacrificing synthesis feasibility? | MolGenBench | proxy gaming and high cost |
| 8 | Binding kinetics | Do ensemble/transition features transfer to residence-time prediction? | public kinetic datasets | sparse heterogeneous labels |

## Preliminary top three

### 1. Ligand-conditioned state failure / apo drift

This currently ranks first because the benchmark is extremely recent, the failure is deeper than pose RMSD, released model outputs and interpretable state labels make analysis tractable, and the question connects directly to induced fit, selectivity, allostery, ensemble modeling and hybrid physics.

The sharp form is:

> When a ligand should move a receptor away from its dominant apo prior, can we predict when a cofolding model will ignore that shift, and can a lightweight state-aware or ensemble-aware correction rescue it?

### 2. The incremental value of 3D under leakage-resistant affinity evaluation

The contribution should not be another affinity GNN. The useful question is:

> Under temporal plus protein/pocket plus ligand/series controls, in which regimes does explicit 3D provide information beyond molecular identity, sequence and nearest-neighbor retrieval?

A rigorous negative result would still be scientifically useful.

### 3. Uncertainty-gated hybrid ML plus physics

Physics refinement can help; the research question is whether we can predict when the expensive step is worth paying for. A useful system would recover most of the downstream benefit using refinement only on high-risk cases.

## Intentionally deprioritized

A new equivariant architecture is low priority unless a documented failure cannot be handled by existing representations. A full prospective wet-lab generative project has high upside but depends on synthesis/assay access. A general protein-dynamics foundation model is too broad for an initial thesis project. A protonation/water-first project remains scientifically plausible but needs a cleaner benchmark-level failure signal before promotion.

## Reading spine

The current minimum serious reading sequence is: AlphaFold 3; PoseBusters/PoseBench; Runs N' Poses; KinConfBench; CleanSplit and LP-PDBBind; the computed-input affinity robustness paper; BioEmu plus the 2026 ensemble reviews; the GPCR ML-plus-physics benchmark plus the 2026 physics/AI perspective; MolGenBench; Target 2035 and PLINDER.

## Evidence gaps before topic lock

The next checkpoint must resolve: quantitative protonation/water/ion sensitivity; an open-source physics-refinement path and realistic compute; cross-family state-collapse evidence beyond kinases; a prospective small-molecule generation hit-rate audit; exact accessibility of strong baselines; and a reproducible KinConfBench pilot.

## Decision rule

Do not lock a thesis because a method is fashionable. Promote a candidate only after the failure is reproduced on public data, strong baselines cannot explain it away, the metric corresponds to a real decision, the contribution remains informative even if the proposed fix fails, and the experiment fits realistic compute and data access.
