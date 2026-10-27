# Cardamom (B0FYY8TVNY) — Sponsored Products recheck and fresh setup

Data: Ad, Target, Search-term and Ad-group-negative exports dated 27 Oct 2026, plus the
lifetime screenshot of ad group **CArdamom AUTO**. Window of the CSVs is not stated; they
total ₹2,488 against ₹24,476 lifetime, so they are a recent slice. Confirm the dates.

## What the data says

| Finding | Evidence |
| --- | --- |
| One listing does all the work | B0FYY8TVNY: 164 clicks, 12 orders, ₹6,756, ACOS 32%, ROAS 3.1. The 8mm++ listing (B0HG3KYTWR) got 15 clicks / 1 order; the 50 g listing (B0HMFQ5M5Z) got **0 impressions**. Three ASINs in one group — Amazon picks the favourite and starves the rest. |
| 74% of search-term spend bought nothing | 61 of 72 terms, ₹1,667 of ₹2,258, 139 clicks, 0 orders. |
| Size-only queries are the leak | `elaichi 100gm` (₹618, 50 clicks), `elaichi 50gm`, `elaichi 500gm`, `elaichi 200gm`: ₹856 / 68 clicks / 0 orders. At ~7% CVR, 50 clicks with no sale happens ~3% of the time — real, not noise. |
| `cardamom` alone leaks | 1,660 impressions, 24 clicks, ₹449, 1 order. |
| Orders come from specific "green / 8mm / jar / 100" queries and ASIN targets | `best green elaichi`, `cardamom in jar`, `elachi green 100`, `ilaichi green`, `cardamom green 8mm`, Hindi `इलायची 100g`; 3 orders from competitor ASINs for ₹183 (ROAS ~7). Mostly 1 order each — treat as hypotheses. |
| Negatives block the best terms | Phrase negative `green cardamom` kills every query containing it (`green cardamom 100g`, `best green cardamom`…). Exact negatives on `cardamom green`, `green elaichi`, `green cardamom pods/whole`, `premium green cardamom whole`, `cardamom green elaichi`, `cardamom green pods`. Phrase `fresh` blocks "fresh elaichi" while the title says Fresh Harvest. Phrase `spiceto` blocks brand searches. |
| Negatives that don't work | `500g` phrase does not catch `500gm`; `1kg` / `1 kg` / `1000g` don't catch `elaichi 1 kg`-style variants reliably. |
| Bid ₹10 vs CPC ₹16–18 lifetime | Dynamic bidding "up and down" or placement modifiers are lifting it. |

## Profit check (from the cost sheet; CSV window = last 65 days)

Live row: 100 g, 7 mm, sale ₹599. Cost ₹506.49 incl. GST → **profit ₹92.51 before ads**.

| | |
| --- | --- |
| Break-even ACOS | 92.51 / 599 = **15.4%** |
| Break-even CPC | 92.51 × CVR (6.2% lifetime, 7.3% recent) = **₹5.7–6.8** |
| Actual CPC | ₹13.3 (65 days), ₹16.4 (lifetime) — 2–2.5× break-even |
| Actual ACOS | 32% (65 days, main ASIN), 63% lifetime |
| Ad cost per order | ≈ ₹190 (65 days), ≈ ₹263 lifetime — vs ₹92.5 profit |
| Real net per order | **≈ −₹99** (65 days), **≈ −₹170** lifetime |

The sheet's "ADV COST 30" (₹30 per order, ≈5% ACOS) is far below what the ads actually
cost, so its net profit (₹62.51) is overstated. Last 65 days on the 100 g ad: 12 orders ×
₹92.51 = ₹1,110 profit vs ₹2,181 ad spend → about **−₹1,070**. Lifetime (₹24.5k spend,
93 orders) is roughly −₹15k on this basis (order values vary, so approximate).
About 90% of lifetime spend was before the last 65 days; ROAS has already improved
from 1.58 to ~3.1, but not to break-even (needs 6.5).

Other rows in the sheet:

| Pack | Sale | Profit | Break-even ACOS | Break-even CPC @7% |
| --- | --- | --- | --- | --- |
| 50 g | ₹399 | ₹109.01 | 27% | ₹7.6 |
| 75 g | ₹499 | ₹120.01 | 24% | ₹8.4 |
| 100 g | ₹599 | ₹92.51 | 15% | ₹6.5 |
| 100 g (other row) | ₹729 | ₹216.01 | 30% | ₹15.1 |
| 200 g | ₹1,299 | ₹298.70 | 23% | ₹20.9 |

The ₹599 100 g is the worst unit to advertise. The ₹729 price (and the 50 g / 75 g /
200 g packs) leaves room for the CPCs Amazon actually charges.

## Why not Exact-first

Agreed with your experience, and it matches the garam masala campaign
(`volume-correction.md`): Exact starves on impressions, and the converting terms here
are long-tail one-offs you can't predict. So: **discovery in Auto/Phrase, ASIN targeting
for the cheap conversions, Exact only as a late "graduate" layer.**

## Fresh structure

**Bids are set from the ₹6 break-even CPC at ₹599, not from Amazon's ₹17–50
suggestions.** Expect low impressions at these bids — the honest trade is volume for not
losing money. To buy volume at ₹10+, first fix the unit: raise the price toward ₹729
(sheet shows ₹216 profit) or lead with the 50 g / 200 g packs. Re-set bids from the new
break-even CPC (profit × CVR) when the price changes.

One ASIN per campaign. Start with B0FYY8TVNY. Bidding strategy **Down only** everywhere.

**Placements:** Top of search **0%**, Product pages **0%** (currently 25% max — remove).
Amazon has no "second row" setting; low base bids plus 0% top-of-search keep you in
Rest of search and out of the pricey top slots. Check the Placement report after 1–2
weeks (CPC, orders, ACOS by placement) before adding any boost, and only on a
campaign with 3+ orders at ACOS < 30%.

**Total daily budget ₹250. Two campaigns, no Exact yet** (Exact starved in your account;
add it later only for terms with 3+ orders). Four campaigns on ₹250 would each be too
small to learn from.

| # | Campaign | Daily | Targets | Bid |
| --- | --- | --- | --- | --- |
| 1 | **Card-Auto-v2** | ₹130 | Close ₹4.5, Substitutes ₹4; Loose & Complements **off** | per group |
| 2 | **Card-Manual** | ₹100 | Ad group *Phrase* (₹5): `green elaichi`, `green cardamom`, `elaichi green 100g`, `cardamom 8mm`, `hari elaichi`, `cardamom in jar`, `idukki cardamom`, `इलायची`. Ad group *ASIN* (₹4.5): the 15 competitor ASINs from the search-term report (not `b0fyy8tvny` — own); start with `b0fbj7k1w7`, `b0h98vdr7k` | per group |
| 3 | **Card-Brand** (optional) | ₹20 | `spiceto`, `spiceto cardamom`, Exact. Skip until brand searches show in the report; then take the ₹20 from Auto. | ₹3–4 |

At ₹4.5 bids, ₹250 ≈ 50–55 clicks/day ≈ 3–4 orders/day at 7% CVR, if impressions
exist. If spend runs well under ₹250 the bids are too low, not the budget too high:
raise ₹0.5 at a time, never above the ₹6 break-even CPC (₹5.6 effective if any placement
boost is left on).

Put the 8mm++ listing (B0HG3KYTWR) in its **own** campaign copy of #1 only if you want to
test it: its CTR (1.27%) is the highest, but 15 clicks proves nothing. Leave the 50 g
listing out until the 100 g listing is stable.

## Negatives

**Campaign 1 (Auto) — remove:** `green cardamom` (phrase + exact), `cardamom green`,
`green elaichi`, `green cardamom pods`, `green cardamom whole`, `premium green cardamom
whole`, `cardamom green elaichi`, `cardamom green pods`, `fresh` (phrase), `spiceto`
(phrase — move to Card-Brand instead).

**Add (negative exact):** `elaichi 100gm`, `elaichi 50gm`, `elaichi 50 gm`,
`elaichi 500gm`, `elaichi 200gm`, `cardamom`*, `akbar elaichi`, `cloudland spices`,
`velora spices`, `anardana whole`, `cardium`, `silver pearls elaichi`, `peeled elaichi`,
`long elachi`, `elaichi spices`, `elaichi box`.
Add (negative phrase): `500gm`, `200gm`, `1000gm`, `1 kg`.

\* Only in Auto and Phrase campaigns; re-test `cardamom` later in Phrase with a ₹7 bid.

**Cross-negatives:** each campaign negative-exacts the converting terms owned by another
(e.g. `elachi green 100` is owned by Card-Phrase) so they don't compete.

## Rules to run it

- Review at 20 clicks per term/target: 0 orders → negative; 1+ order → promote to Phrase.
- Graduate to Exact only terms with 3+ orders; bid at 70% of the Phrase CPC.
- Pause any ASIN target with 15 clicks and 0 orders. Raise a bid by ₹1 only after 3 orders at ACOS < 30%.
- Re-check after 14 days. Success = blended ACOS ≤ 35% (or your break-even).

## Still needed

Which listing is the ₹729 row, whether a 200 g listing exists, (placement multipliers are on at max 25%, which explains the ₹13 recent CPC on a ₹10 bid; older ₹16–18 means earlier bids were higher).
