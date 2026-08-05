# Campaign Structure

## The core constraint

You're driving traffic to `amazon.in/dp/B0H6TP1DNS`. That means:

- **No Meta pixel on the destination.** Amazon doesn't allow third-party pixels on
  product pages. Meta cannot see purchases, so it cannot optimise toward them.
- **Meta's reporting stops at the click.** Everything after — detail page view, add to
  cart, purchase — is measured on Amazon's side through Amazon Attribution.
- **You're buying qualified visits, not sales.** The Amazon listing does the closing. If
  the listing is weak — thin images, no A+ content, few reviews — no amount of ad spend
  fixes that. Audit the listing before you spend (see `launch-checklist.md`).

Everything below follows from those three facts.

## Objective and optimisation

| Setting | Choice | Why |
| --- | --- | --- |
| Objective | **Traffic** | The Sales objective needs a pixel-trackable conversion event. Without one it quietly degrades into an unoptimised link-click buy — same result, worse reporting. |
| Optimisation event | **Landing page view** | Optimising for *link clicks* rewards curiosity taps that bounce before Amazon finishes loading. LPV costs 20–40% more per unit but the visits are real people who saw your product. |
| Bid strategy | **Highest volume**, no cap | Bid caps starve delivery before you have the data to set one intelligently. Add a cost cap only once you know your baseline CPLPV. |
| Attribution window | 7-day click, 1-day view | Meta's default. Only affects Meta's own reporting, which is directional here regardless. |

**When to move to the Sales objective:** once you put the Meta pixel on spiceto.in and
route traffic through an intermediate page, you can fire a real conversion event and
optimise on it. Worth doing above roughly ₹2,000/day. Below that, the extra click in the
path costs you more visitors than the better optimisation wins back.

## Architecture — Phase 1 (Test)

One campaign, campaign budget optimisation, two ad sets, three ads each.

```
CAMPAIGN: SPICETO | Traffic | Prospecting | IN-Metro
├─ Budget: ₹500/day  (CBO on)
├─ Objective: Traffic  ·  Optimisation: Landing page views
├─ Status: PAUSED
│
├── AD SET A — Metro Spice Buyers | 25-54 | All genders
│   ├─ 12 cities with radii (see targeting.md)
│   ├─ Interest stack, narrowed by online-shopping behaviour
│   ├─ Placements: Advantage+ (automatic)
│   ├── AD A1 — Aroma          · video 15s · 9:16 + 1:1 + 4:5
│   ├── AD A2 — What's Inside  · static    · 4:5
│   └── AD A3 — Kerala Origin  · static    · 1:1
│
└── AD SET B — Broad | 25-54 | All genders
    ├─ Same 12 cities, no detailed targeting, Advantage+ Audience on
    ├─ Placements: Advantage+ (automatic)
    └── Same three ads (A1 / A2 / A3)
```

### Why two ad sets, not five

Meta needs roughly **50 optimisation events per ad set per week** to exit the learning
phase. At a realistic ₹6–12 cost per landing page view in Indian metros, ₹250/day buys
you 20–40 LPVs a day — comfortably past the threshold.

Split the same ₹500 across five ad sets and each gets ₹100/day, or 8–16 LPVs. Every ad
set sits permanently in "Learning limited", which degrades delivery *and* leaves the data
too noisy to draw any conclusion from. Two is the floor for a real A/B read at this
budget.

If you want a cleaner read still, run Ad Set B alone with the full ₹500 and test
audiences in week 2 instead.

### Why identical creative in both ad sets

You're testing two variables — audience (A vs B) and creative (A1 vs A2 vs A3). Holding
creative constant across ad sets makes any A-vs-B difference attributable to targeting.
Meanwhile Meta naturally concentrates spend on the winning creative *inside* each ad set,
so you get the creative answer for free.

Expect audience overlap — Broad contains the metro interest audience. That's fine in a
test; you're comparing efficiency, not running a clean-room experiment. Check Audience
Overlap in Ads Manager after a week. If it's above ~40% and B is winning, just turn A off.

## Architecture — Phase 2 (Scale), week 3+

Build this only after Phase 1 produces a clear winner.

```
CAMPAIGN 1: SPICETO | Traffic | Prospecting | IN-Metro
├─ Budget: 3-5x the winning ad set's effective daily spend
├─ Winning audience + winning creative + 2 new creative tests
└─ Add: an Advantage+ Audience ad set as a scaling lane

CAMPAIGN 2: SPICETO | Traffic | Retargeting | IN
├─ Budget: ~20% of prospecting
├─ Audience: Video Viewers 50%+ (365d) + IG/FB Engagers (365d)
└─ Creative: offer-led, review-led, "still thinking about it?"
```

Retargeting is where the Amazon constraint really bites: you can't retarget people who
viewed the ASIN, because Amazon won't tell you who they are. Your entire warm pool comes
from on-Meta engagement. **That's why the lead creative is a video** — it manufactures
the retargeting audience you'd otherwise never have. Treat video-view volume in Phase 1
as a genuine objective.

## Scaling rules

- Raise budget by **no more than 20–25% every 3 days** on a working ad set. Bigger jumps
  reset the learning phase and take the CPM you were enjoying with them.
- For a step change rather than a ramp, **duplicate** the winning ad set at the higher
  budget instead of editing it.
- **Never edit a live ad set's targeting, optimisation event, or creative.** Duplicate,
  change the copy, launch the copy, pause the original.

## Frequency

Whole spices are a considered-but-inexpensive purchase — people typically need 3–5
exposures. Past about **4.0 frequency in a 7-day window** on the same creative, CTR falls
and CPM climbs. Check frequency weekly; crossing 3.5 on prospecting is your signal to
ship new creative, not to widen targeting.

## Naming convention

Keep this consistent so the reports stay readable:

```
Campaign: SPICETO | {Objective} | {Funnel stage} | {Geo}
Ad set:   {Audience} | {Age} | {Gender} | {Optimisation}
Ad:       {Format} | {Angle} | {Aspect} | {Language} | v{n}
```

Examples:
`SPICETO | Traffic | Prospecting | IN-Metro`
`Metro Spice Buyers | 25-54 | All | LPV`
`Video | Aroma | 9x16 | EN | v1`
