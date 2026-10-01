# Case Study — Incorrect RDP Proof in Concurrent Composition

## Event

Salil Vadhan and Wanrong Zhang's work on concurrent composition for differential privacy had an earlier claimed proof for a Rényi-DP concurrent-composition theorem that contained an error. Xin Lyu identified the flaw; Lyu independently proved the RDP result, and the later Vadhan–Zhang version gives a corrected treatment and credits Lyu.

Important distinction:

- **Incorrect:** 'the RDP concurrent-composition theorem was false.'
- **Correct:** the earlier **proof/claim as presented was flawed**, while the theorem itself was later established correctly.

Primary references:
- Vadhan & Zhang, *Concurrent Composition Theorems for Differential Privacy*, STOC 2023 / arXiv 2207.08335.
- Xin Lyu, *Composition Theorems for Interactive Differential Privacy*, NeurIPS 2022.

## What this incident teaches us

### 1. Authority cannot substitute for proof audit

A famous privacy researcher, elite institution, strong coauthor, top venue, citation count, or polished theorem statement does not upgrade a claim from 'published' to 'verified'.

Our evidence ladder is:

1. **Author claim** — the paper says it.
2. **Published proof** — a proof appears in the paper.
3. **Independent corroboration** — another argument or later work supports it.
4. **Research-OS verified** — we have reconstructed the proof obligations relevant to our use case.

Only level 4 should justify language like 'we verified'.

### 2. A wrong proof and a false theorem are different events

When a proof breaks, do not automatically conclude the theorem is false.

Required response:
- locate the exact failed step;
- determine whether the theorem was repaired, reproved, weakened, or actually refuted;
- track version history;
- separate 'proof invalid' from 'claim false'.

### 3. Version history is part of the scientific object

For DP theory, arXiv v1, conference version, camera-ready version, erratum, follow-up proof, and code may materially differ.

Every theorem-level source record should include the version/date actually audited.

### 4. Interactive/adaptive composition is a high-risk zone

Conditioning, adversarial adaptivity, random transcripts, mixtures, post-processing, and divergence composition can create steps that look intuitive but are not automatically valid.

For these proofs, we must explicitly track:
- whose randomness is conditioned on;
- what distribution each induction step refers to;
- whether a privacy bound survives conditioning;
- whether the divergence or tradeoff-function property used is valid under the relevant mixture/post-processing operation;
- whether the adversary's adaptive choices change the hypothesis needed by the next step.

### 5. DP definitions are unforgiving about quantifiers

Small changes in:
- adjacency;
- ordered-pair direction;
- 'for all' versus 'there exists';
- conditioning events;
- alpha range;
- support assumptions;
- adaptivity;

can change the theorem.

Therefore every important proof is rewritten from the quantified definition before algebra begins.

### 6. Conversion theorems deserve independent re-derivation

RDP <-> approximate DP, composition, amplification, and limits such as alpha -> infinity are not bookkeeping.

For every conversion used in our work, record:
- exact theorem source/version;
- assumptions;
- parameter convention;
- range of alpha;
- adjacency convention;
- optimization step;
- whether equality, implication, or sufficient upper bound is being used.

### 7. Our job is not to trust or distrust papers; it is to know verification status

The lesson is not 'papers are unreliable'. The lesson is to maintain calibrated epistemic states.

Allowed statuses:
- published claim;
- proof present but unaudited;
- partially audited;
- independently corroborated;
- verified for our assumptions;
- disputed / broken step;
- corrected / superseded.

### 8. DP project rule created from this case

No theorem-level DP claim may enter the Research OS as 'supported' merely because it appears in a paper abstract or theorem statement.

For claims we rely on mathematically, record at minimum:

**definition -> adjacency -> mechanism -> quantified guarantee -> proof dependency -> version -> open concern**.

## One-line permanent lesson

> In differential privacy, 'published' is a bibliographic status; 'verified' is a mathematical status.
