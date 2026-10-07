# SNAPSHOT

Updated: 2026-10-07 19:16 +08:00

## State

Frontier-survey milestone reached. Broad problem discovery is mature enough to stop expanding the bibliography for now. The next phase is **research-oriented data audit / EDA**, whose purpose is to determine which surviving questions are actually supported by the course dataset before any serious modeling.

## Dataset identity

Course dataset:
- Taiwan MJ Health longitudinal health-examination cohort, 1996–2016
- 62,660 participants
- 160,650 longitudinal records
- 219 fields in the course description; user also has a 138-parameter grouped view
- 18,959 incident ultrasound-defined NAFLD cases
- repeated clinical, laboratory, lifestyle and demographic variables
- residential PM2.5, NO2 and CO exposure
- time-to-event / censoring structure
- target field: `NAFLD2_1()`

Direct source paper:
- Chen YC et al., *International Journal of Epidemiology* (2025), long-term ambient air pollution and incident NAFLD.

## What the survey changed

Do **not** frame the project as:
- baseline ML / nomogram / TyG prediction
- LSTM or Transformer for NAFLD
- generic “does longitudinal history help?”
- generic trajectory / cumulative burden association
- generic pollution × lifestyle interaction
- mixture modeling for its own sake
- “use interval Cox / joint model” as novelty

Those spaces already have direct or close precedents.

The dataset's potentially valuable information is the coupling of:
1. repeated metabolic state,
2. irregular observation / visit timing,
3. ultrasound-based disease detection,
4. longitudinal environmental exposure,
5. long calendar span.

The key conceptual distinction is that **first ultrasound-positive detection is not the same as exact biological onset**. Observed disease history is generated jointly by the disease process and the observation process.

## Five exploration lines

1. **History decomposition**
   - After current state is known, does past history add information?
   - If yes, is the gain from long-term level, change, variability, temporal ordering, or visit pattern?
   - Do not claim novelty from “history vs latest” alone.

2. **Observation / detection process**
   - How much do irregular visits, interval-censored onset, dropout and informative follow-up affect incidence estimates and dynamic prediction?
   - Core question: are we modeling disease progression, or partly when disease gets observed?

3. **Pre-detection trajectories**
   - Before first ultrasound-positive NAFLD, when do BMI, waist, TG, FPG, ALT/GGT, uric acid, BP, etc. diverge from comparable controls?
   - Frame as a pre-detection temporal signature, not mechanism.

4. **Environmental reversibility**
   - When PM2.5/NO2/CO decline over time, does incident NAFLD risk decline?
   - If post-event ultrasound visits exist, does fatty liver persistence/regression change?
   - Highest-risk/highest-reward direction; first require exposure-variation and calendar-confounding feasibility checks.

5. **Causal identifiability**
   - Define which causal estimands are defensible before attempting mediation.
   - In particular, test whether pollution → metabolic change → NAFLD is identifiable under time-varying confounding and observation-process assumptions.
   - If not, downgrade to association/prediction rather than forcing causal language.

Temporal generalization / dataset shift across 1996–2016 is a **validation axis across projects**, not a main standalone topic.

## Current priority

Tentative exploration priority:
1. Observation process ≈ pre-detection trajectories
2. History decomposition
3. Environmental reversibility
4. Causal identifiability

Environmental reversibility has the highest upside if the required exposure panel and post-event outcome history exist.

## Immediate next step: Research-oriented Data Audit

Before training models, answer these GO / NO-GO questions:

1. What exactly is one row: visit, start-stop interval, or processed record?
2. Are patient ID and exact visit dates available?
3. What is the distribution of total visits per person?
4. Among incident cases, how many have ≥2 / ≥3 / ≥4 / ≥5 **pre-event** visits?
5. What exactly generates `NAFLD2_1()`?
6. Are raw ultrasound states retained at every visit?
7. Are visits after first positive NAFLD retained?
8. How often do 0→1→0 or 1→0 transitions occur?
9. Is pollution available as an annual panel, visit-specific rolling summaries, or only 1/3/5-year aggregates?
10. What fraction of pollution variation remains after separating township and calendar-year effects?
11. What is the provenance of missingness, censoring, migration and loss to follow-up?
12. How do participant mix, NAFLD detection, visit frequency, pollution, BMI and missingness change across calendar years?

First deliverable: a **Data Audit Report** that kills or upgrades each of the five exploration lines.

## Research rule

**Problem first. Information second. Method last.**

Do not choose LSTM, Transformer, XGBoost, joint models, causal methods, or other machinery until the data audit establishes what temporal information actually exists.

## Top-conference runway

The path to a top ML/biomedical-ML venue is unlikely to be “a better NAFLD predictor on one private cohort.” The stronger path is:

**MJ reveals a general longitudinal-data failure mode → formalize the problem → develop/justify a method → validate on MJ + public longitudinal datasets.**

Potential general seed:
**dynamic disease-risk learning under irregular and informative observation processes.**

## Return cue

If resuming after several days with little context:

> **Start here: do not survey broadly and do not train a model. Reconstruct the Data Audit checklist above, obtain the real data dictionary/sample rows, and run the GO/NO-GO audit for the five exploration lines.**
