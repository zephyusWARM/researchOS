# Program — Taichung–Changhua Awarded Eats 2026

## Mission
Build the most reliable practical food research line for Taichung and Changhua using two current award systems: **500碗 2026** and **MICHELIN Bib Gourmand 2026**.

This is not a one-shot recommendation list. It is a recoverable evidence system that can answer: what exactly was awarded, whether the place/dish still exists now, what it costs, how difficult it is to eat, and what evidence contradicts the hype.

## Units are different
- **500碗** is stored as a **dish + venue award observation** with bowl count and the selected dish from the official image.
- **Bib Gourmand** is stored as a **venue-level distinction**. Michelin does not award one canonical dish.
Never flatten these into a fake common score.

## Geography
- Taichung: 500碗 + Bib Gourmand.
- Changhua: 500碗.
- MICHELIN Taiwan 2026 covers Taipei, Taichung, Tainan, Kaohsiung, New Taipei City, Hsinchu City and Hsinchu County — not Changhua. Changhua's lack of Bib entries is therefore **out-of-scope**, not evidence of lower quality.

## Pipeline
**P0 — Corpus lock.** Capture every current award observation from authoritative sources, including exact 500碗 selected dishes.

**P1 — Entity resolution.** Resolve aliases, branches, moves, same-name collisions and cross-award overlaps. Do not merge solely on similar names.

**P2 — Venue/dish cards.** For each resolved venue record address, district/township, cuisine, award history, exact selected dish, signature alternatives and source provenance.

**P3 — Current reality.** Verify operation, latest menu and price, whether the awarded dish is still sold, opening hours, payment, solo usability, booking/walk-in, queue and sell-out risk.

**P4 — Red team.** Seek closure/move signals, stale prices, quality inconsistency, portion shrinkage, tourist-hype effects, mandatory sharing/minimum spend and recent negative reports.

**P5 — Decision views.** Only after adequate coverage, derive practical clusters such as station-accessible, breakfast, late-night, low-friction solo meal, local-specialty route and award-overlap route.

## Evidence hierarchy
1. Award-system official page/image
2. Restaurant-controlled current menu/announcement
3. Government/local tourism source
4. Current ordering/booking platform
5. Recent independent visit with menu/photo evidence
6. Search snippets only as discovery aids

## Status taxonomy
- **CORPUS_LOCKED** — official award observation captured
- **ENTITY_RESOLVED** — venue/branch identity established
- **CURRENT_VERIFIED** — current operations + menu/price checked
- **FRESHNESS_WATCH** — likely valid but volatile evidence needs refresh
- **OPERATIONAL_WATCH** — closure/move/sell-out/availability uncertainty
- **CONFLICT** — sources disagree
- **STALE** — only old operational evidence remains

## Known bootstrap data-quality issue
The 500碗 2026 article explicitly says the image list is authoritative. Its text line for Changhua concatenates “吳頂釣魚場” and “社口水煎包”; the official images show two separate entries with separate selected dishes. Canonical corpus therefore keeps **29** Changhua observations, not 28.

## Persistence
GitHub/main is durable truth. Batch changes only after a semantic/epistemic delta. Preserve contradictions rather than silently overwriting them.
