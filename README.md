# Spiceto Biryani Whole Spices — Meta Ads Campaign

Meta (Facebook/Instagram) traffic campaign driving to the Amazon.in detail page for
**Spiceto Biryani Whole Spices — Khada Garam Masala**.

## Product

| Field | Value |
| --- | --- |
| Brand | Spiceto — Premium Kerala Spices Online |
| Product | Biryani Whole Spices · Khada Garam Masala |
| Format | **Whole spices, ready to grind** — 12+ items |
| ASIN | `B0H6TP1DNS` |
| Landing page | https://www.amazon.in/dp/B0H6TP1DNS |
| Seller | Spiceto Trading Company, Ernakulam, Kerala 682306 |
| FSSAI | Lic. 11325999D0868 |
| Site | www.spiceto.in |
| Ad account | I DO Designs Ad account (`387266110719612`) |

Still needed before launch: `{{PRICE}}`, `{{PACK_SIZE}}`, `{{FB_PAGE_ID}}`,
`{{IG_ACCOUNT_ID}}`, and an Amazon Attribution URL (see `campaign/measurement.md`).

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

**Nothing has been created in the ad account.** Planning artefacts plus live-resolved
targeting IDs.

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
