# Pre-Publish Review — Ad `Static | The Ratio | 1x1 | EN | v1`

Reviewed 2026-08-08 against the draft in Ads Manager (campaign
`SPICETO | Traffic | Prospecting | IN-Metro`, ad set `Metro Spice Buyers | 25-54 | All | LPV`).
Draft state: **In draft**, all edits saved, not yet published.

## Blockers — do these before Publish

### 1. Baseline the ASIN

Seller Central → Reports → Business Reports → **Detail Page Sales and Traffic by Child
ASIN**. Export 14 days of daily sessions and units for `B0H6TP1DNS`.

The only irreversible item on the list. It cannot be reconstructed once spend starts, it
takes ten minutes, it needs no Brand Registry — and with no Attribution in place it is the
only number available in week 1.

### 2. Confirm the campaign and ad set toggles are off

The ad's own toggle is on. Publishing activates whatever is not switched off above it. The
spec launches everything **PAUSED**; verify at campaign and ad set level, not just here.

### 3. Nothing in this build measures a sale

No Amazon Attribution URL (blocked on Brand Registry) and UTMs report nothing on an Amazon
destination — both expected and documented in `measurement.md`, but the combined effect is
that the day-14 and day-21 review gates in `campaign-spec.json` have no data to run on.

Cheapest working fix: a Seller Central promo code advertised **only** in these ads.
Redemptions are a countable floor on Meta-driven sales. It has to go into the copy before
publish, or the first cycle runs blind by choice rather than by accident.

## Fix in the ad

| Item | Finding | Action |
| --- | --- | --- |
| **Description** | Set to `12 hand-weighed Whole Spice Mix` — 31 chars against a 30-char cap. The preview already clips it to *"12 hand-weighed Whole Sp…"*. | Revert to the documented `12 hand-weighed spices` (22 chars). |
| **Preview warnings** | A ⚠ **2** badge sits next to the preview format tabs, unopened. | Open and resolve. Usually placement-level asset problems — see the ratio item below. |
| **Aspect ratio** | Ad is named `1x1`. `creative-brief.md` records a 1:1 being **rejected outright** by Instagram Explore home (requires 4:5–9:16), and 9:16 Reels/Stories carries most delivery. | Open all three placement rows under Media. Confirm the "Stories, Status, Reels" row holds a re-composed 9:16 asset, not a letterboxed 1:1. |
| **9:16 safe zone** | Image headline sits at the top of frame; top 250 px is profile-name and UI overlay in Stories/Reels. | Check against the Stories preview specifically. |
| **AI disclosure** | "Ad includes media created or edited with AI" is unchecked. | Tick it if the creative was AI-generated or AI-edited. Meta labels it on detection anyway; self-declaring is safer. |

## Verify at ad set level

Not visible in the ad-level view:

- [ ] All 12 cities present — **Chennai, Indore and Ahmedabad keys were unresolved** in the spec
- [ ] Location type is "People living in this location", not "recently in"
- [ ] Optimisation is genuinely **Landing page views** (the ad set name says LPV; confirm the setting)
- [ ] Age 25–54, all genders
- [ ] CBO ₹500/day, and **no end date** on the schedule
- [ ] The UTM string actually landed in **Tracking** after Meta moved it out of the URL field

## Scope divergence — a deliberate call, not an error

Built: **one ad set, one ad.** Spec: two ad sets × three ads.

What that gives up:

- **Round 1 tests nothing.** The round-1 design varies angle (A1 Ratio vs A2 Whole-or-Ground
  vs A3 Value). With one ad there is no comparison — day 7 gives a CPLPV with no read on
  whether another angle would halve it.
- **No Broad ad set** means no read on whether the interest stack is earning its constraint.

Shipping A1 as a **static rather than the specced 15s video is correct for now** — video QC
found `HAND-WELGHED`, an inconsistent `BIRIYANI`, a 16:9-only export and an end card that
never states price or where to buy. Fix those before the video runs.

## Campaign score — decline all of it

The score (55) is not a quality grade. It measures how much of the campaign has been handed
to Meta's automation, which is why nearly every recommendation broadens targeting or removes
a control. Standing decision: **do not apply these**, and re-read this section rather than
re-litigating each prompt.

| Recommendation | Verdict |
| --- | --- |
| **"Reach people interested in your selected cities or regions"** (+5, *"lower cost per result by 6.7%"*) | **No.** Expands from *living in* the 12 cities to *interested in* them from anywhere in India. Contradicts the deliberate "People living in this location" setting — travellers and enthusiasts don't stock a home kitchen. See below for the deeper reason. |
| **"Use both videos and images"** (+11) | **No, for now.** Points at the video with the unfixed typos, 16:9-only export and price-less end card. Revisit after the video is re-cut. |
| **"Add products or site links"** | **No.** Extra link tiles add nothing for a single-ASIN Amazon destination. |
| **Five text / headline variants** ("Not optimised") | **No.** Multiple variants confound the angle test the campaign exists to run. |

### Why the location one is the dangerous one

"Cost per result" here is cost per landing page view. Broadening an audience reliably makes
clicks cheaper — it is the easiest metric in advertising to improve and the least meaningful.
Normally the tradeoff surfaces downstream when the cheaper traffic fails to convert.

**It cannot surface here.** With no Amazon Attribution URL and no promo code, there is no
mechanism that would ever reveal that the cheaper visits bought worse. A 6.7% CPLPV
improvement is unfalsifiable in this setup, which is precisely when a proxy-metric
optimisation should be refused.

Third cost: the day-7 and day-14 plan reads the **city breakdown** and cuts the bottom
performers. Delivery that is no longer city-bound makes that breakdown unreadable, which
removes what `targeting.md` calls the single highest-leverage optimisation available in
week 2.

**Reconsider only** once Attribution or a promo code is live — at that point cost per *sale*
becomes visible and a targeting expansion can be judged on evidence instead of on Meta's
modelled estimate.

### Open question

The "+11 points" card reads "using both videos and images **for 2 ad sets**", while the
campaign nav shows one. Either Meta's copy is templated or a second ad set exists outside
this view. Confirm — it changes the scope note above.

## Verified correct

- Campaign and ad set names match `campaign-spec.json` exactly
- Primary text matches `ad-copy.md` → Ad A1 → English, word for word
- Headline `The Ratio Is The Recipe` — 22 chars, inside the 40 cap
- CTA `Shop Now`; destination `amazon.in/dp/B0H6TP1DNS?th=1` — correct ASIN and variation selector
- Identity: Page `Spiceto.in`, Instagram `spiceto.in`
- Multi-advertiser ads off; Manual upload; Single image or video
- "Optimise text per person" disabled, single text and headline option — correct for a
  controlled angle test
- Copy passes the `ad-copy.md` compliance table: 12 spices, 50+ servings, no health claims,
  no discount-percentage framing, no Amazon trademark in creative

## Noted, not blocking

The kadai shows **chicken** while the pack carries the green veg mark. Already queued as
round-4 test item 2 in `creative-brief.md`.
