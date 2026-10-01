# Snapshot

Status: **bootstrap complete; latest-2026 census defined; live verification and historical recurrence backfill pending**

Cutoff: **2026-09-24**

## Current answer

The latest-2026 discovery universe is already large enough to justify a dedicated research line:

- **500碗 2026:** 33 Taichung winners + 29 Changhua winners = **62 award entries**.
- **MICHELIN Bib Gourmand 2026:** **23 Taichung establishments**.
- Changhua is outside MICHELIN Guide Taiwan 2026's geographic coverage.
- One obvious cross-list entity is **東勢牛稼莊 / 牛稼莊**.
- Therefore the current union is **provisionally 84 unique establishments** after that obvious alias merge; exact entity resolution remains open.

The 500碗 official text rendering has at least one parsing trap: it visually concatenates **吳頂釣魚場** and **社口水煎包** in the Changhua text list even though the regional count is 29. The project therefore treats award-page text as evidence requiring entity normalization, not as a clean machine-readable table.

## Highest-information first pass

Research priority, not a final food ranking:

1. **金饌脆皮烤鴨** — Taichung's sole 3-bowl winner in 2026.
2. **日棧飯糰** — 2 bowls.
3. **合作街大麵羹** — 2 bowls.
4. **牛稼莊 / 東勢牛稼莊** — obvious 2026 cross-guide overlap (500碗 + Bib Gourmand).
5. **東沐。食在** — the new Taichung Bib Gourmand entrant in 2026.
6. **阿洲蛤仔麵** — high logistical fragility; a 2026 500輯 Changhua guide reports roughly a one-hour daily service window.
7. **魚市爌肉飯** — worth early operational verification because the 2026 Changhua guide notes special cuts can sell out and are easier to obtain near opening.

## Current task

`task-census-and-verify-central-tw-food-radar`

## Next action

1. Finish exact entity resolution and aliases for all 84 provisional current candidates.
2. Backfill 2023–2025 500碗 results and prior MICHELIN retention.
3. Verify the highest-information candidates using first-party current hours/menu/dish evidence.
4. Add a deliberate negative-evidence pass before any “worth a trip” conclusion.
5. Produce geography/daypart clusters only after live verification.

## Persistence rule

Update this snapshot only when the corpus size, entity resolution, live operating status, historical-recognition signal, or trip-ready shortlist materially changes.
