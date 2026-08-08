# Sponsored Products — Optimisation Plan (2026-08-08)

Supersedes the bid guidance in `sponsored-products-audit.md`. Data: 1–8 Aug 2026.

## What changed: Kudampuli converted

| | Biryani (3 campaigns) | Kudampuli |
| --- | --- | --- |
| Clicks | 36 | 25 |
| Spend | ₹586.19 | ₹215.66 |
| **Units** | **0** | **2** (₹407.62) |
| Conversion | 0% | **8.0%** |
| **CPC** | **₹16.28** | **₹8.63** |
| Top-of-search | `<5%` | 5.01% |
| ACOS | — | 52.9% (ROAS 1.89) |

**The account is not broken.** Same seller, same fulfilment, same week — Kudampuli converts at
8%. The biryani product pays **89% more per click** and returns nothing.

If biryani converted like Kudampuli, P(0 sales in 36 clicks) = 5.0%. Suggestive that biryani
is genuinely worse, but still not conclusive.

## Correction: "raise bids to suggested" was wrong

The earlier audit recommended raising bids toward Amazon's suggested bid. That advice does not
survive the unit economics. **Amazon's suggested bid is what it costs to win the auction, not
what the product can afford.**

**Max affordable CPC = contribution margin × conversion rate.**
At ₹199, less ~₹12 referral and ~₹40 FBA. *COGS is assumed — confirm it.*

| COGS | Margin | @5% conv | @8% | @12% |
| --- | --- | --- | --- | --- |
| ₹70 | ₹77 | ₹3.85 | ₹6.16 | ₹9.24 |
| ₹85 | ₹62 | ₹3.10 | ₹4.96 | ₹7.44 |
| ₹100 | ₹47 | ₹2.35 | ₹3.76 | ₹5.64 |

**Ceiling: roughly ₹4–9 per click. Actual: ₹16.28.**

Break-even at ₹16.28 needs 21–35% conversion. `garam masala whole` at its ₹49.61 suggested bid
would need **58%**. Bidding up would have lost money faster.

## Campaign structure — run two, not three

| Campaign | Action | Why |
| --- | --- | --- |
| **Auto** | **Keep** | Only campaign with real volume, and the discovery engine. Spent ₹558 of the ₹586 total. |
| **Broad** | **Pause** | 0.39% CTR vs Auto's 1.25% — 3x worse. 466 of 516 impressions from broad `garam masala`, a commodity head term. Discovery duplicated by Auto. |
| **Exact** | **Keep, rebuild keywords** | 11 keywords, 47 impressions, 0 clicks, ₹0 spent. |

## Exact campaign — two distinct problems

**1. 74% of impressions go to unaffordable head terms.** `garam masala whole` (21) +
`garam masala` (14) = 35 of 47 impressions, zero clicks. Commodity searches owned by Everest
and MDH at ₹60–80; a ₹199 whole-spice pack gets scrolled past.

**2. Five keywords have no search volume.** `biryani garam masala`, `whole spice garam masala`,
`khada garam masala mix`, `mix khada garam masala`, `whole garam masala mix` — all bid **at or
above** suggested, all **zero** impressions. Not a bidding failure; nobody searches those
strings. They are permutations, not queries.

### Changes

| Keyword | Impr | Action | New bid |
| --- | --- | --- | --- |
| `garam masala whole` | 21 | **Pause** — ₹49.61 suggested, unaffordable | — |
| `garam masala` | 14 | **Pause** — commodity, wrong buyer | — |
| `garam spices` | 1 | **Pause** — vague | — |
| `biryani masala whole spices` | 9 | **Keep — core term** | ₹10–12 |
| `biryani whole spice mix` | 1 | **Keep** — hit 50% top-of-search | ₹10–12 |
| `khada garam masala` | 1 | **Keep** | ₹10–12 |
| 5 zero-volume terms | 0 | Leave — cost ₹0, expect nothing | — |

Bids go **down**, not up. Still above the affordable ceiling, but they keep the ad in auctions
where the searcher wants what is actually being sold. Drop the ad group default bid from ₹10
to match.

## Do this first: the Auto Search Terms report

₹558 spent across 34 clicks with no record of what was typed. That report gives:

- real queries that convert → promote into Exact
- queries wasting spend → add as negatives
- whether those 34 clicks were even biryani-related

Everything else is guesswork until it is read.

## Negatives are on the wrong campaign

`recipe`, `instant`, `paste`, `kit`, `oil`, `powder`, `ready to cook` are well chosen but sit
on the **Exact** ad group, where exact match already restricts matching — so they do almost
nothing. **Move them to Auto**, where loose matching happens and where the spend is.

## The strategic read

Kudampuli works because it is a **niche with little competition**: cheap clicks, buyers who
know exactly what they want, no ₹70 substitute on the shelf. Biryani masala is a **commodity
category** contested by national brands.

The route is not to outbid Everest on "garam masala". It is to make biryani behave like
Kudampuli — narrow, specific, low-competition terms where "whole spices, expert ratio, Kerala"
is precisely what the searcher wants. Lower volume, affordable clicks.

If that cannot be found at ₹199/90 g, the lever is AOV, not bids: push the 180 g ₹299 pack, or
bundle. Every rupee of AOV raises the affordable CPC proportionally.

## Open input

**Confirm COGS per 90 g unit.** It is the one assumed number in the affordable-CPC table, and
it moves the ceiling by roughly 2x across the range modelled.
