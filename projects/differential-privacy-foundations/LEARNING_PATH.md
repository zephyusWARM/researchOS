# Learning Path — provisional v1

## Source roles

**Single-source spine:** Cynthia Dwork & Aaron Roth, *The Algorithmic Foundations of Differential Privacy* (2014).

**If "one paper" literally means one journal/conference article:** Cynthia Dwork, *A Firm Foundation for Private Data Analysis* (2011).

**Stage-0 conceptual primer:** Wood et al., *Differential Privacy: A Primer for a Non-Technical Audience* (2018). Keep it; do not use it as the sole rigorous source.

**Modern DP-ML bridge:** Ponomareva et al., *How to DP-fy ML* (2023).

## Mastery gates

A learner should be able to:
1. define neighboring datasets and explain why adjacency matters;
2. interpret the DP probability inequality as output-distribution indistinguishability;
3. compute global sensitivity for simple queries;
4. derive the Laplace mechanism privacy argument;
5. explain post-processing and composition before using formulas;
6. distinguish pure from approximate DP and connect Gaussian noise to the latter;
7. explain what privacy accounting tracks under repeated/adaptive computation;
8. explain DP-SGD as clipping + randomized aggregation + composition/accounting;
9. say what epsilon/delta do and do not mean operationally;
10. recognize RDP/zCDP/f-DP/PLD as modern representations/accounting tools and understand their relation to the core guarantee.

## Next milestone

Map the post-2014 accounting lineage and design derivation exercises that expose slogan-level misunderstandings.
