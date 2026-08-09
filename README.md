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
| [`campaign/sp-optimisation-plan.md`](campaign/sp-optimisation-plan.md) | What to change in the Amazon campaigns, and the affordable-CPC ceiling |
| [`campaign/search-terms-findings.md`](campaign/search-terms-findings.md) | Search terms report — self-targeting, wasted spend, and proof the targeting is right |
| [`campaign/volume-correction.md`](campaign/volume-correction.md) | Why Exact-only cannot run the test, and why not to discount further |
| [`campaign/vine-blocker.md`](campaign/vine-blocker.md) | Vine says the listing is incomplete — the free diagnosis, and the new order of operations |
| [`campaign/listing-fixes.md`](campaign/listing-fixes.md) | Detail page audit — the title gap, and two spices named wrongly |
| [`campaign/listing-rewrite.md`](campaign/listing-rewrite.md) | **Copy-paste rewrite of every listing field, built for organic search** |
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

**Ads are on hold (2026-08-09). Work has moved to fixing the Amazon listing itself.**

**Brand Registry is APPROVED. Vine is blocked on inventory, not page content.** The enrolment
page reports *"No eligible offers — 400… no eligible offers with inventory"*. Vine draws units
from a live FBA offer and cannot find one. Two checks: whether the product is FBA at all (Vine
does not work with Easy Ship or self-ship), and that enrolment is sitting on **parent ASIN**
`B0H6TSDQ7R`, which holds no offer — a child needs live FBA stock. Every listing-content theory
is closed: description populated, 6 bullets, required attributes filled.

Fee tiers are now visible: **30 units = ₹2,600 + ~₹2,550 of product ≈ ₹5,150** for an estimated
15–24 reviews. Best cost per review of the three tiers, against the ₹15,000 Meta cycle that would
have taught nothing.

**New order of operations: FBA stock in → Vine → ~20 reviews → then advertise.** Full detail in
[`campaign/vine-blocker.md`](campaign/vine-blocker.md).

**The detail page audit found the title is the clearest problem on the listing.** It runs 63
characters of ~200 available and contains **none** of *biryani* (₹257 of ad spend), *sabut*
(₹110) or *khada* (₹83). A 171-character replacement, plus a
copy-paste rewrite of every other field, is in
[`campaign/listing-rewrite.md`](campaign/listing-rewrite.md). The audit also caught **two of the
twelve spices declared wrongly** — Sha Jeerakam and Perumjeerakam are both called "Fenugreek"
when they are caraway and fennel, and the error sits in the **structured Ingredients attribute**,
which is a legal declaration under FSSAI rather than marketing copy.

**On organic search:** the rewrite makes the listing *eligible* to rank; it does not create rank.
Amazon position is driven mainly by sales velocity and conversion, so the keyword work and the
Vine reviews have to happen together — the rewrite alone moves impressions, not orders.

---

**Meta remains on hold by agreement (2026-08-08).**

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

**Sponsored Products is already running** — three campaigns live since 3 Aug, no sales, which
is why Meta was being tried. But they have produced only **36 clicks** at **₹16.28 CPC**. Zero
sales in 36 clicks is what a healthy 5% listing looks like ~16% of the time: an unfinished
test, not a failed one. Audit in
[`campaign/sponsored-products-audit.md`](campaign/sponsored-products-audit.md).

**The encouraging number: CTR is 1.10%** (36/3,286 impressions) against ~0.3–0.5% benchmarks,
and unlike the conversion figure it rests on a large enough sample to trust. Main image, title
and price are working. The bottleneck is after the click.

**The search terms report confirmed the targeting is right** — 68% of visible spend went to
`biryani spices`, `biryani whole spices`, `biryani spices whole` and `biryani masala whole
spices`. Right query, good ad, click, no purchase. It also caught **the campaign paying to
advertise on Spiceto's own cardamom listing** (ASIN `B0FYY8TVNY`) and ₹55.91 of dead spend in
the Substitutes group. See
[`campaign/search-terms-findings.md`](campaign/search-terms-findings.md).

**Roughly ₹1,400 of properly-bid Amazon traffic settles the question that ₹15,000 of Meta
spend would leave ambiguous** — because Amazon reports the sale and Meta cannot.

⚠️ **Correction (2026-08-09):** Auto was switched off, leaving Exact alone — which delivers only
**~6 impressions/day** and so can never reach a diagnostic sample. The ₹120/day budget cannot be
spent; volume is the constraint, not money. **Auto has to come back on** with the waste cut
(negative product target `B0FYY8TVNY`, Substitutes off, `mdh`/`elaichi` phrase, `spices`/`garam
masala` exact). Also: **do not discount further** — CTR at 3x benchmark proves shoppers accept
₹199 *before* clicking, so price is not the barrier, and every rupee off lowers the affordable
CPC ceiling that is already being exceeded. Full working in
[`campaign/volume-correction.md`](campaign/volume-correction.md).

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
