# Vine Says the Listing Is Incomplete (2026-08-09)

## Status change

- **Brand Registry: APPROVED** (trademark still pending registration)
- **Vine: NOT ELIGIBLE — "listing incomplete"**

## Why this is the most useful finding so far

Amazon's own system inspected the detail page and judged it **incomplete**. That is a free
diagnosis of precisely what ~₹1,300 of clicks was going to spend a fortnight testing.

It also fits every other signal: healthy CTR (people click), zero conversion (the page does not
close), 100% buy box (nothing structural). An incomplete page produces exactly that pattern.

## What "incomplete" usually means

> **Updated after inspecting the live record — see [`listing-fixes.md`](listing-fixes.md).**
> The description is **present and substantial**, and there are **6 bullet points**. The
> empty-description theory below is disproven.

- [x] ~~Product description field empty~~ — **ruled out**, description is populated
- [x] ~~Fewer than 5 bullet points~~ — **ruled out**, 6 present
- [ ] **Too few images** ← now the leading suspect, check the Images tab
- [ ] **Not FBA / not In Stock in New condition** ← check the Offer tab
- [ ] Missing required category attributes

## The order of operations flips

**Stop ad spend. Fix completeness. Get Vine. Then advertise.**

| Route | Cost | Result |
| --- | --- | --- |
| Ads now | ~₹1,300 | *Maybe* an answer; listing still has 3 reviews |
| Vine first | ~30 units of COGS | **30 genuine reviews** and a complete page |

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

1. **Today** — find why the listing reads as incomplete. Start with the description field.
2. **This week** — enrol in Vine, send units.
3. **Hold the ads** — leave Auto paused; Exact at ₹120/day will barely spend.
4. **In 3–4 weeks** — with 30 reviews and a complete page, re-run the same Exact campaign. That
   is a real test against a listing that can actually convert.

## Still open

**COGS per 90 g unit.** Sets the Vine cost and is the last assumption in the affordable-CPC
maths.
