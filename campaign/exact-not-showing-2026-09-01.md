# "The Ad Isn't Showing" — BIRIYANI-New-Exact 2.0 (2026-09-01)

Ad group `BIRIYANI-New-Exact 2.0`, 10 enabled keywords, date range 28 Jun – 1 Sep 2026.
Reported totals: **1,108 impressions, ₹55.30 cost, Top-of-search `<5%` on every keyword,
all 10 Delivering.**

---

## First, the correction: it is showing. It is showing at the bottom.

1,108 impressions is not zero. Every keyword reads **Delivering**, which rules out the whole
list of reasons an ad genuinely does not serve — campaign paused, out of budget, end date
passed, product not the featured offer, listing suppressed. None of those apply here.

What the table actually says is **`<5%` top-of-search on all 10 keywords**. The ad is winning
only the leftover slots: down-page rest-of-search, page 2 and beyond, and product detail pages.
That is invisible in every way that matters to a shopper, but it is not "not showing" — it is
"showing where nobody looks", and the two have completely different fixes.

## Why you personally didn't see it

Three separate reasons, all of them normal:

1. **Exact match fires on the literal string only.** These 10 keywords are the only queries
   this ad group can serve on. Search `garam masala whole spices 100g` or `best khada masala`
   and nothing runs — by design, not by fault (`exact-impressions-2026-08-18.md`).
2. **`<5%` top-of-search.** Even on the 10 exact strings, the ad is almost never in the top
   block. You would have to scroll well down, or to page 2.
3. **Self-searching is an unreliable test, and a mildly harmful one.** Results are personalised,
   and repeatedly searching a term and not clicking the ad teaches Amazon your ad is a poor
   answer to it. Use the **placement report** and the top-of-search column to check visibility —
   not your own eyes.

## The mechanical cause: 8 of 10 bids sit below the suggested range

| Keyword | Bid | Suggested (range) | Bid vs range floor | Impr | Cost |
| --- | --- | --- | --- | --- | --- |
| biryani masala whole spices | ₹8.00 | ₹11.98 (7.44–14.98) | **inside** | 36 | — |
| biryani spices whole | ₹8.00 | ₹8.84 (5.53–11.05) | **inside** | 13 | — |
| khada masala sabut | ₹7.00 | ₹10.57 (7.04–13.21) | −₹0.04 | 104 | ₹13.63 |
| garam masala | ₹10.00 | ₹14.61 (10.96–18.26) | −₹0.96 | 201 | — |
| garam masala sabut | ₹9.00 | ₹16.84 (12.63–19.42) | −₹3.63 | 27 | — |
| whole garam masala | ₹9.00 | ₹25.06 (13.46–31.32) | −₹4.46 | 19 | — |
| sabut garam masala | ₹10.00 | ₹25.35 (15.67–31.68) | −₹5.67 | 76 | ₹10.10 |
| khada garam masala | ₹9.00 | ₹22.81 (16.08–28.52) | −₹7.08 | 13 | — |
| garam masala whole mix | ₹12.00 | ₹34.48 (25.86–43.10) | −₹13.86 | **588** | **₹31.57** |
| garam masala whole | ₹10.00 | ₹53.48 (40.11–66.85) | **−₹30.11** | 31 | — |

Seven of the ten keywords produced impressions and **zero clicks** — no cost at all. All ₹55.30
came from three keywords, and ₹31.57 of it from one.

## The trap: do not fix this by raising bids

The obvious move — push every bid up into its suggested range — is the exact advice
`sp-optimisation-plan.md` already corrected once, and it is still wrong.

**Amazon's suggested bid is what it costs to win the auction. It is not what the product can
afford.** At ₹199 for the 90 g pack, less referral and FBA, the max affordable CPC is
**≈ ₹4–9**, and ₹9 only in the optimistic corner of the table (₹70 COGS, 12% conversion).

Measured against that ceiling:

- `garam masala whole` needs **₹40+** to compete — 4.5x the ceiling.
- `garam masala whole mix` needs **₹26+** — 3x the ceiling. It is currently taking **53% of the
  impressions and 57% of the spend in this ad group**, on an auction the product cannot afford
  to win. This is the live leak.
- `khada garam masala`, `sabut garam masala`, `whole garam masala`, `garam masala sabut` all
  need ₹12–16+ to enter the range — above the ceiling, though not absurdly.

Bidding to visibility here means buying clicks at 2–5x what a click can be worth. The ad group
would stop being invisible and start losing money faster. Visibility is not the goal; profitable
visibility is.

## What to actually do

**1. Raise the three keywords that are affordable *and* winnable.** These are the only ones
where the suggested range floor sits inside the ₹4–9 ceiling:

| Keyword | ₹ now | → | Why |
| --- | --- | --- | --- |
| `khada masala sabut` | ₹7.00 | **₹8.00** | ₹0.04 under the floor. Cheapest way into the range in the whole set, and it already draws impressions and clicks. |
| `biryani masala whole spices` | ₹8.00 | **₹9.00** | Core term — the phrasing Auto converted on. Floor is ₹7.44, so this buys real position. |
| `biryani spices whole` | ₹8.00 | ₹8.00 | Already mid-range. Leave it. |

**2. Pause `garam masala whole mix`.** Biggest impression and spend line in the group, ₹26 floor
against a ₹9 ceiling, no sales. Nothing about it improves by leaving it enabled.

**3. Pause `garam masala whole` and `garam masala`.** Both were marked for pause on 8 Aug and
are live again in the 2.0 rebuild. `garam masala whole` at a ₹40 floor is unwinnable at any
affordable bid; `garam masala` is the commodity head term where a meaningful share of searchers
want **powder** — the wrong-buyer risk already flagged three times in this project.

**4. Leave the remaining four alone at their current bids.** They cost ₹10.10 between them
across two months. They are not the problem, and raising them breaks the ceiling.

## Two things to check that could change the diagnosis

- **The cost chart reads ₹0.00 flat across the whole visible August window**, while the total
  for 28 Jun – 1 Sep is ₹55.30. That suggests the spend is old and this ad group has been
  effectively dormant for weeks. **Narrow the date range to the last 14 days.** If impressions
  are near zero there, then "not showing" is literally true for recent days, and the cause is
  that CPCs have risen past these bids entirely — which strengthens the case for pausing rather
  than nursing the unaffordable keywords.
- **Check the campaign's bidding strategy and placement multipliers.** If it is set to
  *dynamic bids — down only*, Amazon lowers these bids further in auctions it does not expect to
  convert; with zero conversion history on Exact, that compounds the invisibility. A
  top-of-search placement multiplier would be the one lever that buys top slots selectively,
  but it multiplies the CPC on exactly the placement that is already unaffordable — so check it,
  do not reach for it.

## The strategic read, unchanged

Exact is not the layer that finds demand. Auto produced all 3 purchases and ₹1,187.62 in the
10 Aug week while Exact ran flat (`first-purchases-2026-08-10.md`). Exact's job is to hold the
price down on phrasings Auto has already proven convert.

If top-of-search visibility on the garam masala terms is genuinely wanted, **the lever is AOV,
not bids.** Every rupee of order value raises the affordable CPC proportionally — push the 180 g
₹299 pack or a bundle, and ₹16 clicks stop being unaffordable. Until then, bidding into a
commodity auction owned by national brands is paying for the privilege of losing.

**Still open, still the highest-value unknown: confirm COGS per 90 g unit.** It is the one
assumed number in the ceiling, and it moves the answer roughly 2x.
