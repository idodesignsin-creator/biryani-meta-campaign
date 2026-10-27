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

The ₹599 100 g is the worst unit to advertise.

## Live listing and market (checked 27 Oct 2026)

Listing prices are GST-inclusive: 50 g ₹395 · 75 g ₹490 · 100 g ₹599 · 200 g ₹1,399
(₹736/100 g). Rating 4.3 from 29 ratings. The search-term sales figures are ex-GST:
₹570.48 = ₹599, ₹475.24 = ₹499, ₹380 = ₹399, ₹1,332.38 = ₹1,399 — so at least one 200 g
order exists, and the 100 g price has moved over time (₹646.67 and ₹665.72 match ₹679 and
₹699).

Competitor 100 g prices incl. GST: Go Vegan 8 mm ₹395, GreenFinity 8 mm ₹419, Kitchen
Jungle ₹439 (8 mm ₹549), Idukki Spices ₹494, Vedaka ₹519 (3.4K ratings), Astree ₹649
(1 rating). Spiceto 100 g at ₹599 is at the top of the range, so **do not raise the 100 g
price** (the earlier ₹729 idea is withdrawn). Review counts (29 vs hundreds/thousands)
limit conversion more than price does.

The cost sheet row for 200 g used ₹1,299; the live price is ₹1,399, so profit is higher
than the ₹298.70 shown (≈ ₹390 if fees scale). Break-even CPC ≈ ₹27 at 7% CVR.
Caution: at ₹736/100 g the 200 g is the priciest per gram in the category; test, don't assume.
Listing issues to fix: title says **190g**, size selector says **200 g**; MRP ₹1,999 with
"30% off" draws ASCI scrutiny if the price never sells near MRP.

## Why not Exact-first

Agreed with your experience, and it matches the garam masala campaign
(`volume-correction.md`): Exact starves on impressions, and the converting terms here
are long-tail one-offs you can't predict. So: **discovery in Auto/Phrase, ASIN targeting
for the cheap conversions, Exact only as a late "graduate" layer.**

## Fresh structure

**Bids are set from the ₹6 break-even CPC at ₹599, not from Amazon's ₹17–50
suggestions.** Expect low impressions at these bids — the honest trade is volume for not
losing money. To buy volume at ₹10+, first fix the unit: advertise the 200 g child ASIN (profit ≈ ₹390)
and/or a 2×100 g bundle, not the ₹599 100 g. Re-set bids from the new
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

The 200 g child ASIN (listing is a size variation family).

Note: placement multipliers were on at max 25%, which explains the ₹13 recent CPC on a
₹10 bid; the older ₹16–18 means earlier bids were higher.

## Step-by-step setup (Amazon Ads console)

**Before you start:** open the old campaign and note its negatives and settings. Don't
delete it yet. Pause it only when the new Auto is live, so you don't double-pay on the
same searches.

### Campaign 1 — Card-Auto-v2 (₹130/day)
1. Campaigns → **Create campaign** → Sponsored Products.
2. Name `Card-Auto-v2`. Add **only B0FYY8TVNY** (not the 8mm++ or 50 g listings).
3. Targeting: **Automatic targeting**. Daily budget **₹130**. Start date today, no end date.
4. Bidding strategy: **Dynamic bids – down only**. Placement adjustments: Top of search
   **0%**, Product pages **0%**.
5. Ad group `Card-Auto`. Default bid ₹4.5. Set per group: Close match **₹4.5**,
   Substitutes **₹4**, Loose match **off**, Complements **off**.
6. Negative keywords: add the "Add" list from the **Negatives** section below
   (exact and phrase as shown). Do **not** copy the old `green cardamom`, `cardamom green`,
   `green elaichi`, `fresh`, or `spiceto` negatives.
7. Negative product targeting: add your own other listings (`B0HG3KYTWR`, `B0HMFQ5M5Z`)
   so you don't bid against yourself.
8. Launch.

### Campaign 2 — Card-Manual (₹100/day)
1. Create campaign → Sponsored Products → name `Card-Manual`, product **B0FYY8TVNY**.
2. Targeting: **Manual**. Daily budget **₹100**. Same bidding strategy and 0% placements as above.
3. **Ad group 1 `Phrase`**: Keyword targeting → add manually, match type **Phrase**, bid ₹5:
   `green elaichi`, `green cardamom`, `elaichi green 100g`, `cardamom 8mm`, `hari elaichi`,
   `cardamom in jar`, `idukki cardamom`, `इलायची`.
4. **Ad group 2 `ASIN`**: Product targeting → Individual products → paste the competitor
   ASINs from the search-term report (`b0fbj7k1w7`, `b0h98vdr7k` first, then the rest;
   skip `b0fyy8tvny`). Bid ₹4.5.
5. Campaign negatives: copy the same "Add" list as Campaign 1.
6. Launch.

### Campaign 3 — Card-Brand (₹20/day, optional)
Manual, Exact keywords `spiceto`, `spiceto cardamom`, bid ₹3–4. Skip until brand
searches appear in the report.

### After launch
- **Day 1:** confirm all campaigns say Delivering; no policy flags; placements at 0%.
- **Day 3:** if spend is far under budget, raise bids ₹0.5 (max ₹6). Don't judge ACOS yet.
- **Day 7:** search-term report. Terms at 20+ clicks and 0 orders → negative exact. Terms
  with 1+ orders in Auto → add to Card-Manual as Phrase.
- **Day 14:** Placement report, ACOS vs the 15% break-even (see Profit check). Pause the
  old CArdamom AUTO campaign if not already done.

## Goal changed: temporary rank-push for the 100 g (supersedes profit-based bids)

Context from the seller: ~2 months ago the 100 g listing sat on the second row and did
10–20 orders/day. Ads were stopped, it held for a week, then stock ran low, the price was
raised, sales fell and the listing slid to page 2. Ads are **not** meant to be permanent:
they restart sales velocity on targeted searches, organic rank recovers, ads are tapered.

So the ₹6 break-even CPC and the ₹4.5 bids no longer apply. Ads are an **investment with
a cap**: ~₹100/order loss at today's CPCs. Expected cost of a 21-day push at ₹250/day
≈ ₹2–3k net loss (plus any coupon). Judge it on rank and organic orders, not on ACOS.

What actually moves organic rank for a keyword: orders on that keyword, conversion rate,
price vs competitors, stock. Ad spend by itself does nothing; the **orders** it creates do.

### Honest volume check
₹250/day at ₹12 CPC ≈ 20 clicks ≈ 1.4 orders/day at 7% CVR. Previously 10–20/day. Ads
alone will not rebuild that; they are the spark. Two ways to get more orders from the same
money: raise conversion (coupon / price back near the old level) or raise the budget.
A ₹50–100 Amazon **coupon** on the 100 g costs less per order than the ~₹190 ad cost
per order, lifts CTR and CVR, and shows a badge in search.

### Setup (₹250/day, 21 days, one ASIN B0FYY8TVNY, down only, placements 0%)

| Campaign | Daily | Targets | Bid |
| --- | --- | --- | --- |
| **Rank-Push** | ₹150 | Exact **and** Phrase on the terms you want to rank for: `green cardamom`, `cardamom green`, `green elaichi`, `elaichi green 100g`, `hari elaichi`, `cardamom 8mm`, `idukki cardamom`, `cardamom in jar` | ₹12 |
| **Auto** | ₹60 | Close ₹6, Substitutes ₹5; keep the junk negatives; add the rank terms as negative exact so they don't compete with Rank-Push | per group |
| **ASIN** | ₹40 | `b0fbj7k1w7`, `b0h98vdr7k` (Exact) | ₹6 |

- In Rank-Push, **do not** carry over the old negatives on `green cardamom`,
  `cardamom green`, `green elaichi` — those are now the target terms.
- Bids of ₹12 are what it takes to win impressions (Amazon suggests ₹17–50). Down only
  means actual CPC stays ≤ bid.
- Keep stock above ~14 days of sales. Running out again resets the rank.

### Exit rule
Search each target term logged-out, once a day, and note the 100 g's organic position.
When it shows on page 1 organically for 3+ target terms **and** organic orders are 5+/day
for 3 days, cut ad budgets 50% every 3 days to zero (not an abrupt stop). If after 14
days orders from ads are under 1/day, the problem is conversion (price, reviews, images),
not traffic — fix that before spending more.

### Need from the seller
Current stock and price, the price when it did 10–20/day, and the terms it ranked on then.

### Seller update (27 Oct 2026)
Stock 20 kg ≈ 200 × 100 g units. Old price ₹499 (when it did 10–20 orders/day), now ₹599
because raw cardamom cost rose (climate); price stays. Oct 2026 harvest, fresh; listing is
non-returnable.

- Stock cover: 10–20 orders/day = 10–20 days. Set a reorder trigger at ~5 kg left; a
  stock-out resets the rank.
- Bring the **effective** price back to ₹499 with a **₹100 Amazon coupon on the 100 g
  only** (list price stays ₹599, no MRP/price-history damage). Coupon order ≈ break-even
  (₹92.51 profit − ₹100 + small redemption fee) versus ≈ −₹100 per ad order. It also lifts
  organic conversion, not just ad clicks. Run it for the same 21 days, then end it with
  the ads.
- Use "Oct 2026 Fresh Harvest" in the title/bullets (the pasted note says "2006" — typo).

### Positioning: quality, not price (seller decision, 27 Oct 2026)
Do not compete with Vedaka / ZOFF-type mixed-grade listings. Spiceto's differentiator:
Idukki, 7–8 mm, Oct 2026 harvest, **black seeds inside the pods**, jar pack.

- **Rank-Push terms (quality-led only):** `8mm cardamom`, `cardamom 8mm`, `bold green cardamom`,
  `idukki cardamom`, `idukki elaichi`, `export quality cardamom`, `cardamom in jar`,
  `elaichi green 100g`. Head terms (`green cardamom`, `cardamom`, `elaichi`) go to Auto only,
  at the low bid, where price shoppers cost little.
- **ASIN targets:** premium / 8 mm / Idukki competitors only (e.g. Astree, ArtOspices,
  Idukki Spices, Orika, 8 mm jar brands). **Exclude Vedaka and ZOFF.** Keep
  `b0fbj7k1w7` and `b0h98vdr7k` — they converted. Seller to paste the ASINs from the pages.
- **Negatives:** keep `vedaka` (phrase); add `zoff`, `keya`, `choti`, `small`.
- **Coupon is optional** under this positioning. If used, keep it small (₹50) and short, framed
  as launch pricing; otherwise rely on the creative below.
- **Creative (lifts conversion without a discount):** a macro image of a split pod showing
  black seeds, with a short line stating what that means — only claims the seller can stand
  behind (matured, fresh Oct 2026 harvest). Pod-size photo with a ruler (7–8 mm). Don't name
  or disparage other brands in images or copy.

### The black-seed claim (seller, 27 Oct 2026)
The seed inside the pod is the product. Fully matured pods have **black seeds**; less
mature pods have golden/pale seeds. Spiceto's pods are black-seeded.

Copy that stays accurate:
- Image headline: **"BLACK SEEDS INSIDE = FULLY MATURED"** (or "Open one pod. Black seeds, not golden.")
- Bullet: "Fully matured green pods — black, aromatic seeds inside, not pale or golden. Idukki,
  7–8 mm, Oct 2026 harvest, aroma-sealed jar."
- Image set: split pod macro (black seeds) beside a golden-seed pod from the mix, no brand
  names; 7–8 mm ruler shot; jar shot.
- Avoid "best cardamom in India" / "No. 1" (unprovable superlative, ASCI/Amazon risk) —
  say "fully matured" instead.

Keyword trap: **never target or say "black cardamom"**. That is badi elaichi, a different
spice, and it is already (correctly) a negative. Keep the existing negatives `black`,
`black cardamom`, `seed(s)`, `cardamom seeds` so ads don't serve to black-cardamom or
loose-seed shoppers. Write it as "black seeds in green pods", never "black cardamom".
