# Coverage

Official 500盤 2026 universe: **314 awarded restaurant slots**.

## Full Tier-1 completion

| Tier-1 bucket | Count | Meaning |
|---|---:|---|
| SURVIVE_CONFIRMED | 14 | Strong survivor into Tier 2; may still have freshness/policy gaps |
| SURVIVE_TO_T2 | 96 | Plausible / insufficient evidence to safely exclude |
| SURVIVE_SHARED_RISK | 70 | Shared-format trap; solo path must be proven |
| DROP_HARD | 21 | Current/recent evidence supports >500 or incompatible mandatory format |
| DROP_T1_SIGNAL | 111 | Reversible high-price/course-format screen-out signal |
| OPERATIONAL_WATCH | 1 | Temporarily unavailable |
| CORPUS_GAP | 1 | Official image-only/unresolved two-pan slot |
| **Total** | **314** | **Complete Tier-1 disposition** |

Full restaurant membership for every bucket is stored in `data/tier1-screen-20260924.json`.

## Strong Tier-1 survivors

### Taipei core
- 都一處（仁愛店）
- 鼎泰豐
- ZAC ZAG 一樂炸雞
- 天下三絕
- 春水堂（中正店）
- 孫麵店
- 新采粵式小館
- 醇一拉麵
- 穆記牛肉麵
- 蘇杭點心店

### National travel queue
- 小喬新疆羊肉串
- Bebu 春嬌粄條
- 來一片
- 阿財牛肉湯

## Hard exclusions captured at Tier 1

Chaud Doux; Restaurant A; 山海樓; impromptu; KOUMA日本料理小馬; 台北亞都麗緻大飯店 巴賽麗廳; 小小樹食; aMaze 心宴; Solo Pasta; yuu 肉割烹ゆう; 三六食府; 春韭（晴光店）; 榕居; Clover Bellavita; Miacucina（南西店）; Sugar Pea; Wok by O'BOND; 佐佧義式窯烤披薩屋; 金豬食堂; 驢子餐廳（賦樂旅居店）; 自在天昆布水つけ麵.

## Adversarial rules now locked

1. A cheap single dish is not a qualifying meal.
2. Every unavoidable service/minimum/set/seat/water/tax charge counts.
3. Shared restaurants cannot qualify by per-person division of a multi-person bill.
4. Old prices never override current price/policy evidence.
5. Closure is tracked separately from affordability.
6. `DROP_T1_SIGNAL` is reversible and must not be mislabeled as a hard budget fact.
7. Restaurant affordability and award-dish affordability are separate questions.
8. The official corpus text has a one-name extraction gap in the two-pan tier; preserve the gap instead of fabricating the 314th name.

## Tier-2 survivor depth

For survivors only: latest first-party menu/policy, concrete solo order <=500, portion sufficiency, current hours/open status, queue/reservation/sell-out friction, payment friction if material, recent negative evidence, award-dish identity/price/availability when discoverable, and a falsification condition.

## Stop condition

Tier 1 is complete. The next durable milestone is reached when all surviving Taipei-core candidates have either (a) current first-party budget proof + usability/red-team evidence, or (b) are demoted/excluded with current attributable evidence.
