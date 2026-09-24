# Snapshot

Status: **Tier-1 full-corpus milestone complete — 314/314 assigned a triage disposition; Tier-2 now restricted to survivors**

## Tier-1 result (2026-09-24)

- **314 / 314** official 2026 500盤 restaurant slots have a Tier-1 disposition.
- **14 strong survivors**: clear current/recent solo-meal affordability evidence, but some still carry freshness/policy gaps.
- **96 Tier-2 candidates**: plausible enough that they cannot be safely discarded without menu/minimum-spend proof.
- **70 shared-format risk**: potentially cheap per person, but group arithmetic is not accepted; a genuine solo order must be proven.
- **21 hard exclusions**: current/recent attributable evidence already pushes the unavoidable solo path above NT$500 or requires an incompatible format.
- **111 reversible screen-out signals**: high-price/course/omakase/fine-dining evidence makes <=500 implausible; these are not promoted to hard exclusions without exact floor proof.
- **1 operational watch**: 阿城鵝肉土城總店 is temporarily closed for renovation.
- **1 corpus gap**: official total requires 55 two-pan restaurants, but the machine-readable official text exposes only 54 names; the official image layer remains authoritative.

Canonical machine-readable ledger: `data/tier1-screen-20260924.json`.

## Taipei strong-survivor queue

**都一處（仁愛店）, 鼎泰豐, ZAC ZAG 一樂炸雞, 天下三絕, 春水堂（中正店）, 孫麵店, 新采粵式小館, 醇一拉麵, 穆記牛肉麵, 蘇杭點心店.**

These names survived Tier 1, but `SURVIVE_CONFIRMED` means “strong survivor into Tier 2,” not “all volatility closed.” Exact current dine-in minimum/service policy still needs first-party closure for some.

## Material deltas from this run

- **都一處（仁愛店） strengthened**: current menu exposes explicit one-person sets NT$280–420; a 2026 dine-in report states 10% service, keeping the highest listed one-person set at NT$462 all-in.
- **孫麵店 strengthened**: 500輯 documents two complete meal sets at NT$320, not merely a cheap side or snack.
- **穆記 strengthened operationally**: current aggregation describes adequate portions, solo suitability, and peak-time crowding; exact low-spend wording is still not treated as first-party proof.
- **Sugar Pea moved to hard exclusion under the strict complete-meal rule**: official policy is NT$300 minimum +10%, but current menu-scale bowls/salads/pasta begin above NT$500; sub-500 items are nibbles/toast rather than a defensible normal meal path.
- **驢子餐廳（賦樂旅居店） hard excluded**: current OpenTable policy requires each diner age 7+ to order a Pasta/Risotto or Grill/Pan item and lists the restaurant at NT$1,000–1,999.
- **Wok by O'BOND hard excluded**: current Michelin description identifies a seasonal tasting-menu format; current pricing evidence remains far above the student ceiling.
- **Shared-restaurant rule tightened**: restaurants such as 四海一家 / 欣葉台菜 / 六品小館 are not qualified by dividing a group meal. They stay in shared-risk until a solo fried-rice/noodle/set path is proven.

## Award-dish caveat

Restaurant-level affordability and the actual 500盤-recognized dish remain separate fields. For many 1-pan restaurants, the public machine-readable award page does not expose the exact dish and current price. Do not infer an award dish from a signature dish, special-award article, or restaurant bestseller.

## Next research boundary

Tier 1 is complete. Do **not** spend routine time deepening DROP_T1_SIGNAL restaurants. Tier 2 should now focus on surviving candidates, Taipei first, and close: current first-party menu, unavoidable charges, solo portion sufficiency, opening status, queue/reservation friction, recent negative evidence, and award-dish identity/price where publicly verifiable.
