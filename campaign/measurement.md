# Measurement

## The problem in one paragraph

Meta will report clicks, landing page views, CPM and CTR. It will not report a single
sale, because Amazon does not let Meta's pixel onto the detail page. If you judge this
campaign purely on Meta's dashboard, you will optimise toward cheap clicks and have no
idea whether any of them bought anything. **Set up Amazon Attribution before you spend,
not after** — it cannot backfill data for traffic that already happened.

## Amazon Attribution — the fix

Amazon Attribution gives you a tracking URL that reports, inside Amazon, what your
off-Amazon traffic actually did: detail page views, add to carts, purchases, and sales
revenue attributed to each ad.

**Eligibility:** you need Amazon Brand Registry for the Spiceto brand, and access through
Seller Central (Brand → Amazon Attribution) or the Amazon Ads console. If Spiceto isn't
Brand Registered yet, start that first — it gates Attribution, A+ Content and Sponsored
Brands, all of which you want anyway.

**Setup:**

1. Seller Central → **Brands → Amazon Attribution**
2. Create an **Advertiser** for Spiceto
3. Create a **Campaign** — name it to match your Meta campaign
   (`SPICETO | Traffic | Prospecting | IN-Metro`)
4. Add an **Ad group per Meta ad set** — `Metro Spice Buyers`, `Broad`
5. Create a **tracking tag per ad**, so A1 / A2 / A3 report separately:
   - Publisher: Facebook
   - Channel: Social
   - Product: ASIN `B0H6TP1DNS`
6. Amazon returns an attribution URL per tag. **That URL is what goes in the Meta ad's
   destination field** — not the plain `amazon.in/dp/B0H6TP1DNS`.

The tags are the whole point of the exercise. One tag for the entire campaign tells you
the campaign worked; a tag per ad tells you *which ad* worked, which is the thing you
act on.

**Granularity worth having:** one tag per ad per ad set = 6 tags for Phase 1. That's a
tedious twenty minutes and it's the difference between optimising on evidence and
optimising on vibes.

## Fill this in as you go

| Meta ad set | Meta ad | Attribution tag name | Attribution URL |
| --- | --- | --- | --- |
| Metro Spice Buyers | A1 Aroma | `metro-a1-aroma` | `{{URL}}` |
| Metro Spice Buyers | A2 Whats Inside | `metro-a2-inside` | `{{URL}}` |
| Metro Spice Buyers | A3 Kerala | `metro-a3-kerala` | `{{URL}}` |
| Broad | A1 Aroma | `broad-a1-aroma` | `{{URL}}` |
| Broad | A2 Whats Inside | `broad-a2-inside` | `{{URL}}` |
| Broad | A3 Kerala | `broad-a3-kerala` | `{{URL}}` |

## Brand Referral Bonus

Amazon pays a bonus — typically around 10% of qualifying sales — on purchases you drive
from outside Amazon using Attribution tags. Availability varies by marketplace and
changes over time, so **check the Brand Referral Bonus page in Seller Central for
amazon.in eligibility** rather than assuming it applies.

If it is available to you, it is effectively a discount on your Meta CPC, and it only
works through Attribution tags. One more reason to set them up before launch.

## KPIs and what "working" looks like

### Meta-side (available immediately)

| Metric | Watch for | Read |
| --- | --- | --- |
| CPM | ₹150–₹400 (metro, 25–54) | Above ₹450 → audience too narrow or creative fatiguing |
| CTR (link) | 0.8%–1.8% | Below 0.6% → creative isn't landing. Fix the hook first. |
| Cost per landing page view | ₹6–₹15 | Your primary Meta-side efficiency number |
| LPV / link click ratio | above 70% | Below 50% → slow page or accidental taps |
| Frequency (7d) | under 3.5 | Above → ship new creative |
| Video 3s views | maximise | Feeds the retargeting pool. Track even though it's not the goal. |

These ranges are planning estimates for Indian metro traffic on a food product, not
guarantees. **Your own week-1 numbers become the real benchmark** — record them and
compare against yourself from then on.

### Amazon-side (the numbers that matter)

| Metric | Where | Read |
| --- | --- | --- |
| Detail page views | Attribution report | Should roughly track Meta's LPVs. A big gap means click loss in the redirect. |
| Add to cart rate | Attribution report | Under ~10% → listing or price problem, not a traffic problem |
| Purchase rate | Attribution report | The number that decides whether the channel works |
| Attributed sales ₹ | Attribution report | Against ad spend = your real ROAS |
| Cost per acquisition | spend ÷ attributed purchases | Compare to gross margin per pack |

### The one calculation that decides everything

```
Break-even CPA = gross margin per pack (after Amazon referral fee,
                 FBA/shipping, GST, and packaging)
```

If your break-even CPA is ₹120 and you're acquiring at ₹300, the channel is losing money
at current creative and needs fixing — or the product needs a higher AOV through bundles.
If you're acquiring at ₹80, scale hard.

Work this number out **before launch**. Everything else in this document is instrumentation
for it.

## Reporting cadence

**Don't touch anything for the first 72 hours.** Ad sets are in the learning phase and
early numbers are noise. The most common way small campaigns fail is an advertiser
optimising on day 2 data.

| When | Look at | Do |
| --- | --- | --- |
| Day 3 | Delivery status, spend pacing, any rejections | Fix blockers only. No optimisation. |
| Day 7 | CPLPV by ad, by ad set, **by gender**, **by age**, by city | Pause clearly losing ads. Decide the gender question. |
| Day 14 | Full Meta + first meaningful Attribution data | Cut bottom cities. Pick the winning angle. Plan round 2 creative. |
| Day 21 | Attributed sales, CPA vs break-even | Scale, restructure, or stop |
| Weekly after | Frequency, creative fatigue, new creative into rotation | Routine |

## Recording results

Add a `results/` directory and log week-by-week — Meta's reporting window shifts as
attribution matures, so a contemporaneous record is the only reliable history you'll have.

```
results/
  week-01.md   Meta metrics + first Attribution pull
  week-02.md   Decisions made and why
  ...
```

Write down the *decision* and the *reason* each week, not just the numbers. In six weeks
you won't remember why you cut Lucknow, and the reasoning is what compounds.
