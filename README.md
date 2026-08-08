# Spiceto Biryani Whole Spices — Meta Ads Campaign

Meta (Facebook/Instagram) traffic campaign driving to the Amazon.in detail page for
**Spiceto Biryani Whole Spices — Khada Garam Masala**.

## Product

| Field | Value |
| --- | --- |
| Brand | Spiceto — Premium Kerala Spices Online |
| Product | Biryani Whole Spices · Khada Garam Masala |
| Format | **Whole spices, ready to grind** — usable whole or ground |
| Spices | **12**, hand-weighed: cardamom, black pepper, cinnamon, cloves, bay leaf, nutmeg, mace, star anise, khus khus, jeerakam, sha jeerakam, perumjeerakam |
| Ratio | Developed with biryani experts in Kerala |
| Origin | Idukki, Kerala |
| Price | **₹199 / 90 g** (MRP ₹425) · ₹299 / 180 g |
| Servings | 50+ per pack → **under ₹4 per biryani** |
| Rating | 5.0 from 3 ratings |
| ASIN | `B0H6TP1DNS` |
| Landing page | https://www.amazon.in/dp/B0H6TP1DNS?th=1 |
| Seller | Spiceto Trading Company, Ernakulam, Kerala 682306 |
| FSSAI | Lic. 11325999D0868 |
| Facebook Page / Instagram | Spiceto.in / spiceto.in |
| Ad account | I DO Designs Ad account (`387266110719612`) |

Still needed before launch: creative assets, and an Amazon Attribution URL
(see `campaign/measurement.md`).

## What's here

| File | Covers |
| --- | --- |
| [`campaign/structure.md`](campaign/structure.md) | Campaign architecture, budget, objective, scaling rules |
| [`campaign/targeting.md`](campaign/targeting.md) | The 12 cities with radii, **the gender question**, age, interests |
| [`campaign/ad-copy.md`](campaign/ad-copy.md) | Ad copy — English + Hinglish, all three angles |
| [`campaign/creative-brief.md`](campaign/creative-brief.md) | Asset specs, shot list, video scripts |
| [`campaign/measurement.md`](campaign/measurement.md) | Amazon Attribution, KPIs, benchmarks |
| [`campaign/ads-manager-walkthrough.md`](campaign/ads-manager-walkthrough.md) | **Click-by-click manual setup in the Ads Manager UI** |
| [`campaign/launch-checklist.md`](campaign/launch-checklist.md) | Pre-flight + first 14 days |
| [`campaign/pre-publish-review.md`](campaign/pre-publish-review.md) | Review of the built draft in Ads Manager — blockers before Publish |
| [`campaign/baseline-2026-08-08.md`](campaign/baseline-2026-08-08.md) | **Pre-launch ASIN baseline — and why the launch is on hold** |
| [`campaign/sponsored-products-audit.md`](campaign/sponsored-products-audit.md) | The Amazon SP campaigns — why "zero results" isn't the finding it looks like |
| [`campaign/sp-optimisation-plan.md`](campaign/sp-optimisation-plan.md) | **What to change in the Amazon campaigns, and the affordable-CPC ceiling** |
| [`campaign/campaign-spec.json`](campaign/campaign-spec.json) | Machine-readable spec for API creation |

## The two decisions you asked about

**Gender: don't go female-only.** Run all genders for the first 7 days, then narrow on
real data. Full reasoning in [`campaign/targeting.md`](campaign/targeting.md) — short
version: on Amazon India the account holder and payment method skew male, biryani
specifically over-indexes with male home cooks, and halving your audience at ₹500/day
damages delivery more than the precision helps. Meta reports a gender breakdown for
free; buy the answer for one week instead of guessing.

**Age: 25–54.** Grinding your own masala is a more involved cook than the average, which
argues older; but 25–34 has materially cheaper CPMs on Instagram and Reels, which argues
younger. 25–54 covers both and lets the delivery system find the edge. Review the age
breakdown at day 7 alongside gender.

## Defaults chosen

- **Objective:** Traffic, optimising for **landing page views** — Amazon won't host your
  Meta pixel, so conversion optimisation isn't available. LPV filters out accidental taps.
- **Budget:** ₹500/day campaign-level (CBO).
- **Launch state:** `PAUSED` — nothing spends until you review it in Ads Manager.
- **Geo:** the 12 cities and radii you specified.

## Status

**Meta is on hold by agreement (2026-08-08). Work has moved to fixing the Amazon campaigns.**

The decisive comparison came from the seller's own account: in the same week, **Kudampuli
converted at 8% on ₹8.63 clicks while the biryani product took 36 clicks at ₹16.28 and sold
nothing.** The account, fulfilment and pricing structure all work — biryani is paying 89% more
per click in a commodity category against national brands.

That reframes the whole problem as **unit economics, not traffic**: at ₹199 the affordable CPC
is ₹4–9, and the head terms cost ₹27–50. See
[`campaign/sp-optimisation-plan.md`](campaign/sp-optimisation-plan.md) for the keyword-level
plan, and note it **supersedes the bid advice** in the earlier SP audit.

---

**The Meta draft is built and unpublished — and should stay that way for now.**

The pre-launch ASIN baseline was pulled on 2026-08-08 and answered the question the campaign
was going to spend ₹15,000 to answer: **138 sessions, 1 unit — 0.72% conversion**, while
holding the buy box ~100% of the time. A second, wider pull added 19 sessions and zero
orders, which tightens the **95% upper bound on conversion to 3.39%**. Traffic is not the
binding constraint.

At ₹500/day the campaign needs **3–6% conversion just for revenue to equal ad spend**, before
COGS and Amazon's fees — it would spend roughly ₹1,000 to sell a ₹199 packet. That gap is not
reachable by tuning targeting, creative or bids. Full working in
[`campaign/baseline-2026-08-08.md`](campaign/baseline-2026-08-08.md).

**The unlock is Brand Registry**, which resolves all three blockers at once: A+ Content
(conversion), Vine (3 reviews → the ~10 where cold traffic stops bouncing), and Amazon
Attribution (the measurement the campaign otherwise lacks entirely).

**Relaunch gate:** re-pull the same report; launch at **≥5% unit session percentage** over
300+ sessions.

**Next step is Sponsored Products, not Meta** — and SP is *already running*, which changes the
picture again. Three campaigns have been live since 3 Aug and returned no sales, which is why
Meta was being tried. But they have produced only **~41 clicks**, because every bid sits below
Amazon's suggested range and top-of-search is `<5%` everywhere. The Exact campaign has spent
**₹0**. Zero sales in 41 clicks is what a healthy 5% listing looks like 12% of the time — it
is not a failed test, it is an unfinished one. Full audit in
[`campaign/sponsored-products-audit.md`](campaign/sponsored-products-audit.md).

**The encouraging number: CTR is 1.57%** (18/1,149 impressions) against ~0.3–0.5% benchmarks,
and unlike the conversion figure it is measured on a large enough sample to trust. Main image,
title and price are working. The bottleneck is after the click, or not yet measured.

**Roughly ₹1,400 of properly-bid Amazon traffic settles the question that ₹15,000 of Meta
spend would leave ambiguous** — because Amazon reports the sale and Meta cannot.

The campaign artefacts are unaffected and stay ready. The draft in Ads Manager is campaign
`SPICETO | Traffic | Prospecting | IN-Metro` → ad set `Metro Spice Buyers | 25-54 | All | LPV`
→ one ad, `Static | The Ratio | 1x1 | EN | v1`, reviewed in
[`campaign/pre-publish-review.md`](campaign/pre-publish-review.md). Note it was built as one
ad set with one ad against a spec of two × three, so round 1 as designed (angle A1 vs A2 vs
A3) would not have run.

⚠️ **Also open:** the listing title appears to have changed and **no longer contains
"biryani"** — see the last section of the baseline. Verify against the live listing.

Done:
- Connection to ad account `387266110719612` verified
- 9 of 12 Meta location keys resolved live
- All interest and behaviour IDs resolved live (see the "what doesn't exist" note in
  `campaign/targeting.md` — there is no Biryani or Spice interest in Meta's catalogue)
- Ad-account asset library inspected: 1,417 images, 884 videos, across several clients

Blocked on:
1. **A creative image.** No Spiceto asset could be identified in the shared agency ad
   account, and the asset thumbnail URLs aren't reachable from this environment. Needs a
   public image URL or a specific `image_hash`.
2. **Adspirer API quota** — 15/15 free calls used on 2026-08-05, resets 2026-09-04.
3. Chennai, Indore and Ahmedabad location keys still unresolved.

The exact creation sequence is recorded in `campaign/campaign-spec.json` under
`creation_sequence`.
