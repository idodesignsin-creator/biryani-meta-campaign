# Sponsored Products Audit — 2026-08-08

> **⚠️ The bid guidance in this file is superseded by
> [`sp-optimisation-plan.md`](sp-optimisation-plan.md).** "Raise bids to Amazon's suggested
> bid" does not survive the unit economics — the affordable CPC for a ₹199 product is ₹4–9,
> while suggested bids on the head terms run ₹27–50. The delivery diagnosis below still
> stands; the prescription does not.

Reviewed after the question *"there is already ongoing promotion in Amazon but zero result …
that's why we're trying a Meta ad."*

**Finding: the Amazon campaigns have not failed. They have barely run.** Roughly 41 clicks
and ₹600 of spend is not a conversion test, and the inference "Amazon didn't work, so move to
Meta" is not supported by this data.

## What is actually running

Account `ENTITY2H428B54YSDWE`, three biryani campaigns live since 3 Aug 2026 plus one for a
different product.

| Campaign | Type | Budget | Impressions | Clicks | Spend | Purchases |
| --- | --- | --- | --- | --- | --- | --- |
| BIRIYANI-New-Auto 2.0 | SP Auto | ₹150/day | 2,724 (Aug 1–8) | ~36 | ₹558.64 | **0** |
| BIRIYANI-New-Broad 2.0 | SP Manual | ₹130/day | 512 | ~1–5 | ~₹15–90 | **0** |
| BIRIYANI-New-Exact 2.0 | SP Manual | ₹120/day | ~45 | **0** | **₹0** | **0** |
| Kudampuli Exact Tire 1.0 | SP Manual | ₹50/day | 302 | 5 | ₹44.16 | 0 |

Biryani totals: **~41 clicks, 0 purchases.**

## Why delivery is starved: bids sit under Amazon's suggested range

| Target | Bid | Suggested (range) | % of suggested | Impressions |
| --- | --- | --- | --- | --- |
| Exact — `garam masala whole` | ₹20.00 | ₹49.61 (₹42.76–59.66) | **40%** | 21 |
| Broad — `garam masala` | ₹15.00 | ₹27.13 (₹20.35–33.91) | **55%** — below the floor | 466 |
| Auto — default | ₹12.00 | ₹16.90 (₹5.71–36.93) | 71% | 2,724 |

**Top-of-search is `<5%` on essentially every keyword.** The impressions being won are
bottom-of-search and product-detail placements, which convert far worse than top-of-search.

Two confirmations that this is a bid problem, not a budget problem:

- **Exact has spent ₹0** in six days — 13 impressions, no clicks. It is not running.
- **Auto spent ₹93/day against a ₹150 budget.** Raising budgets would change nothing.

## 41 clicks cannot answer the conversion question

| If true conversion were | P(0 sales in 41 clicks) | |
| --- | --- | --- |
| 15% | 0.1% | ruled out |
| 10% | 1.3% | unlikely |
| **5%** | **12%** | **plausible** |
| 3% | 29% | plausible |
| 2% | 44% | plausible |

Zero sales in 41 clicks is what a **healthy 5% listing** looks like a good fraction of the
time. The 95% upper bound from SP alone is 7.0% — *weaker* than the Business Report's 3.4%,
and not independent evidence either, since these clicks are already inside those 138 sessions.

## The reliable signal: CTR is strong

**1.57% CTR** (18 clicks / 1,149 impressions) against Amazon SP benchmarks commonly quoted at
0.3–0.5% — roughly 3x. Measured across 1,149 impressions, so unlike the conversion figure
this estimate is trustworthy.

**The main image, title and price are working.** Shoppers searching for biryani masala see the
product and click at an above-average rate. The bottleneck is not search-results presentation;
it is either downstream of the click (3 reviews, no A+ content) or simply unmeasured.

## Why Meta does not solve this

| | Amazon SP | Meta |
| --- | --- | --- |
| Cost per visit | ₹13.71 CPC | ₹6–12 CPLPV |
| Visitor intent | typed "biryani masala", wallet out | scrolling Reels, not shopping |
| Sale measurable? | **yes, natively** | **no** — no Attribution, UTMs dead on Amazon |

Similar cost per visit, far colder traffic, and no way to observe the outcome. If a
high-intent searcher will not buy, an interrupted scroller will not either.

Meta's one legitimate edge — creating demand among people who do not know whole-spice mixes
exist — is a brand-building play needing sustained budget and patience. It is not a fix for an
unconverted listing and not something ₹500/day delivers.

## On premium pricing

₹199/90 g is roughly 2.5–3x mass-market powder. Defensible, but a premium price must be
justified **on the page**, and the page currently offers 3 reviews and no A+ content. A
shopper comparing against a ₹70 packet sees a higher price and less proof. The premium is not
the problem; the missing justification is.

The Kudampuli campaign also shows 0 sales — far too small a sample to conclude from, but it
does not point to a biryani-specific issue.

## Actions

### 1. Fix the bids, then run the test

- Raise the money Exact keywords — `biryani masala whole spices`, `khada garam masala`,
  `biryani whole spice mix`, `whole garam masala mix` — to **at least Amazon's suggested bid**.
- Push **top-of-search bid adjustment** well above the current 5–15%.
- Pause `garam masala` broad. Generic, expensive, and those shoppers want powder.
- Leave budgets alone. They are not the constraint.

### 2. Buy enough clicks to actually know

| Goal | Clicks needed | Cost @ ₹14 CPC |
| --- | --- | --- |
| Rule out 5% conversion | ~58 | ~₹800 |
| Rule out 3% | ~98 | ~₹1,400 |
| Usable point estimate | 200–300 | ~₹3,000–4,000 |

Currently 41 clicks in. **~₹1,400 more of properly-bid Amazon traffic settles what ₹15,000 of
Meta spend would leave ambiguous.**

### 3. In parallel — Brand Registry

A+ content and Vine reviews are what a premium price needs, and are required regardless of
which channel eventually runs.

## Also noted

Campaign names read **"BIRIYANI"**, the same misspelling the video QC caught in the creative.
Internal-only, no customer impact, but it suggests the spelling should be standardised
wherever it is set once.
