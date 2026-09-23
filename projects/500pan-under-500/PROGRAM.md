# Program — 500盤 2026 <= NT$500

## Mission
Find 2026 500盤 restaurants where a student can **actually eat a normal solo meal for an unavoidable bill <= NT$500**, without cheap-item, shared-bill, stale-price, or hidden-charge loopholes.

Canonical universe: the official 2026 500盤 complete list, reported as 314 awarded restaurants.

## Two affordability questions
1. **restaurant_budget_path** — can one person eat a normal meal at this awarded restaurant for <=NT$500 all-in?
2. **award_dish_budget_path** — is the actual 500盤-recognized dish, when identifiable and currently sold, itself accessible within <=NT$500?

Passing (1) does not imply passing (2).

## Hard budget rule
Count minimum spend, mandatory service, required set menus, cover/seat fees, compulsory drink/water, and tax if not included.

Reject appetizers/desserts that are not a meal; delivery-only promotions as baseline; multi-person per-capita arithmetic when a solo diner cannot order that way; and historical prices presented as current.

## Status taxonomy
- **QUALIFIED** — defensible current solo meal <=500; hidden-charge check passed.
- **QUALIFIED / FRESHNESS WATCH** — strong affordability evidence; exact latest first-party menu/policy still needs refresh.
- **BORDERLINE** — plausible, but meal sufficiency, hidden charges, solo ordering, or current price unresolved.
- **OPERATIONAL WATCH** — budget may qualify, but closure/availability blocks a go-now recommendation.
- **EXCLUDED** — unavoidable solo meal >500 or format incompatible.
- **STALE** — only old evidence available.

## Pipeline
**Tier 0 — Corpus lock.** Use the official 2026 complete list; preserve its warning that text names are keyword aids and image lists are authoritative.

**Tier 1 — High-recall triage.** Prioritize noodles, rice, dumplings, casual pizza/pizza-by-slice, skewers, cafés, casual Taiwanese/Hakka, and other plausible solo formats. Rapidly exclude obvious tasting-menu/omakase/hotel-fine-dining floors when current evidence is far above 500.

**Tier 2 — Budget proof.** Capture current attributable menu pricing, hidden charges, and one concrete normal solo order.

**Tier 3 — Student usability.** Check portion sufficiency, solo ordering, hours, payment, booking/walk-in friction, queues, sell-out risk, and closures.

**Tier 4 — Red team.** Seek price rises, shrinkflation, inconsistency, service problems, low-spend traps, discontinued dishes, and temporary closure.

## Geography
- **Taipei core** — deeper priority because it is immediately actionable.
- **National travel queue** — retain high-signal candidates elsewhere without mixing travel cost into the food-price rule.

## Evidence hierarchy
1. Official menu / booking / restaurant-controlled announcement
2. Restaurant-managed ordering platform
3. Current major delivery menu for price corroboration
4. Current structured business/menu data
5. Recent independent visit with photographed/menu-backed prices
6. Old reports only as historical evidence

Search snippets are discovery aids, not high-confidence proof.

## Persistence
GitHub/main is durable truth; conversation is disposable compute. Batch Source -> Evidence -> Claim changes only after a semantic/epistemic delta. Preserve contradictions and freshness gaps. Revalidate volatile price/policy evidence before concrete visit recommendations.
