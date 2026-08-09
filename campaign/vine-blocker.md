# Vine Says the Listing Is Incomplete (2026-08-09)

## Status change

- **Brand Registry: APPROVED** (trademark still pending registration)
- **Vine: NOT ELIGIBLE — "listing incomplete"**

## What the rejection actually says

The first reading of the rejection was "listing incomplete", which pointed at page content.
Inspecting the enrolment page directly showed a different error, and it changes the fix — see
below. The listing-content theories are all closed.

## The real blocker: inventory, not content

The error on the enrolment page reads:

> **"No eligible offers — 400. We were not able to identify eligible offers with inventory for
> this product."**

**That is an offer/stock problem, not a listing-content problem.** Vine draws units from a live
Fulfilled-by-Amazon offer, and it cannot find one.

Two checks, in order:

1. **Is the product actually FBA?** Vine only works with FBA inventory. On Easy Ship or
   self-ship, Vine is unavailable regardless of how complete the listing is — units must be sent
   into FBA first.
2. **The enrolment is on the PARENT ASIN.** The page shows `B0H6TSDQ7R — Parent ASIN —
   2 variations`. Parents never hold offers; children do (`B0H6TP1DNS` = the 90 g child). At
   least one **child** needs live FBA stock before Enrol activates.

Check Manage Inventory for FBA stock on both children.

### Listing-content theories, now closed

- ~~Product description empty~~ — populated and substantial
- ~~Fewer than 5 bullets~~ — 6 present
- ~~Missing required attributes~~ — Item Name, Brand, Manufacturer, Description, Bullets,
  Serving Quantity/Unit and Ingredients are all filled
- Empty nutrition sections (Energy, Fat, Protein, Carbohydrate, Vitamins) are **not** marked
  required and are **not** the blocker — worth filling for FSSAI and display, but separately

## Cost, now that the fee tiers are visible

| Units | Fee | Product cost | Total | Likely reviews | Cost/review |
| --- | --- | --- | --- | --- | --- |
| 2 | ₹0 | ₹170 | ₹170 | 1–2 | — |
| 10 | ₹1,000 | ₹850 | ₹1,850 | 5–8 | ₹285 |
| **30** | ₹2,600 | ₹2,550 | **₹5,150** | **15–24** | **₹264** |

*COGS assumed at ₹85 — still unconfirmed. Vine reviewers typically review 50–80% of units.*

**Take 30.** Best cost per review, and it moves the listing from 3 reviews to roughly 20–27 —
past the ~10-review threshold `launch-checklist.md` identifies. ₹5,150 against the ₹15,000 Meta
cycle that would have taught nothing.

## The order of operations flips

**Stop ad spend. Get FBA stock in. Get Vine. Then advertise.**

| Route | Cost | Result |
| --- | --- | --- |
| Ads now | ~₹1,300 | *Maybe* an answer; listing still has 3 reviews |
| Vine first | ~₹5,150 all-in | **~20 genuine reviews** on the page |

Vine costs more in product than the ads cost in cash, but it buys **the fix, not the
diagnosis**. Advertising a page Amazon considers incomplete is paying to send strangers to
something already known to be unfinished. (Vine enrolment fees vary by marketplace — check the
enrolment page.)

## Negatives in Auto — done, and done correctly

Negativing the 9 harvested Exact terms in Auto is right: it stops the two campaigns bidding
against each other.

**The hard part was got right:** `spice` and `spices` are negative **exact**, not phrase. Phrase
would have blocked `biryani whole spices`, `masala whole spices`, `khada masala sabut` and most
of the good traffic. That was the one available mistake, and it was avoided.

26 negatives now in place, including `mdh`, `hotel`, `jaipur`, `badi elaichi`, plus dish-name
exacts (`khichdi`, `pilau`, `tahdig`).

## Two problems if Auto runs

1. **Close match bid is ₹19.59** — 2.2x the affordable ceiling, and higher than the ₹16.28 CPC
   already judged unaffordable. Amazon suggested it; it was applied. Drop to ~₹10 if Auto runs.
2. **All four targeting groups show status "Paused"** — Close match's toggle is on but status
   reads Paused, which usually means the campaign or ad group above is still off. Verify before
   assuming it is live.

**Structural note:** with the 9 terms negatived and Substitutes, Loose match and Complements all
off, Auto has very little left to match — and those terms were 74% of its spend. Combined with
Exact's ~6 impressions/day, total volume falls from here. Another reason the ads-first plan does
not work yet.

## Plan

1. **Today** — check FBA inventory on the child ASINs. That is what blocks Vine.
2. **This week** — get stock into FBA if it is not there, then enrol 30 units.
3. **Hold the ads** — leave Auto paused; Exact at ₹120/day will barely spend.
4. **In 3–4 weeks** — with 30 reviews and a complete page, re-run the same Exact campaign. That
   is a real test against a listing that can actually convert.

## Still open

**COGS per 90 g unit.** Sets the Vine cost and is the last assumption in the affordable-CPC
maths.
