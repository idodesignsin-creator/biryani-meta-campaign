# Audience Targeting — Cristal Kuruva Resort, Wayanad

A **Custom Saved Audience** (manual detailed targeting), not Advantage+ Audience. This
means Advantage Detailed Targeting is switched **OFF** — Meta will not expand past the
options selected below. That's the correct choice for a premium/high-intent brief: you're
trading some reach for precision, on purpose.

## Why "custom" matters here

Advantage+ Audience is built to maximise *volume* at the lowest cost per result — it will
happily widen into cheap, low-intent clicks to hit that goal. A premium resort selling a
₹15,000–40,000+/night stay doesn't want volume, it wants the right few thousand people.
Manual targeting keeps the audience deliberately narrow and skewed toward travel intent
and spending power, even at a higher CPM.

## Locations

Set as **"People living in this location"** for the always-on prospecting audience, plus a
second **"People travelling in this location"** variant for last-minute/short-lead
bookers — Wayanad is a drive/short-haul market from three of these four states, so people
already in transit or scoping a trip are a real, distinct segment worth its own ad set.

| # | Location | Type | Suggested radius | Why |
| --- | --- | --- | --- | --- |
| 1 | Bangalore, Karnataka | City | 25 km | Largest weekend-getaway feeder market — ~290 km / ~6 hr drive from Wayanad. Highest-income, highest-frequency short-break traveller pool of the four. |
| 2 | Kochi, Kerala | City | 20 km | Kerala's affluent metro — corporate offsites, anniversary/staycation bookers, local wedding-planning market. |
| 3 | Kozhikode (Calicut), Kerala | City | 20 km | Closest major Kerala metro to Wayanad (~65 km) — local premium audience with the shortest possible trip friction. |
| 4 | Thiruvananthapuram (Trivandrum), Kerala | City | 15 km | State capital, concentrated government/corporate/professional wealth, worth a smaller share of budget. |
| 5 | Chennai, Tamil Nadu | City | 25 km | Largest Tamil Nadu feeder; further from Wayanad than Coimbatore but far larger affluent base — flight or long-drive market. |
| 6 | Coimbatore, Tamil Nadu | City | 20 km | Closest Tamil Nadu metro to Wayanad via the Gudalur route — strong weekend-drive candidate, often under-targeted vs. Chennai. |
| 7 | Mumbai, Maharashtra | City | 25 km | Fly-in market — no drive option, so this segment skews toward higher-AOV bookings: honeymoons, milestone anniversaries, longer stays. Justifies the highest per-click bid ceiling of the four. |

Two notes carried over from how this repo handles Meta location entry generally:

- **Meta lists it as "Bangalore," not "Bengaluru"** — search the old name.
- **Build this directly in Ads Manager.** You don't need a location ID to do it by hand —
  type the city name, pick it from the dropdown, then set the radius next to it.

**Exclude:** Wayanad district itself, and a wide radius around the resort (say 50 km).
You are not trying to advertise a staycation to people who already live next to it.

## Age

**28–58.** This skews older than a typical leisure-travel campaign on purpose:

- The lower bound (28) excludes most budget-conscious backpacker-age browsing that drives
  up CPM without matching the property's price point.
- The upper bound (58) still captures high-income, empty-nest travellers who are some of
  the highest-AOV guests a resort like this gets, while staying short of the age band
  where Meta usage and ad responsiveness drop off sharply.

Split into two ad sets if budget allows — **28–40** (honeymoon/milestone-anniversary,
DINK couples) and **41–58** (family/multi-generational and corporate-offsite bookers) —
because the creative and message for these two groups should differ, and blending them
in one ad set hides that in the data.

## Gender

**All.** Leisure-travel and resort bookings are typically decided jointly or by whichever
partner researches — narrowing by gender loses the researcher who isn't the one who ends
up booking. Review the delivery-by-gender breakdown after ~1 week of spend and split only
if one side is clearly cheaper at real volume, same logic as the biryani campaign's
gender call in `../targeting.md`.

## The real "high-profile" lever: Household Income (India)

Meta rolled out direct household-income targeting for India — confirmed live on this
account under **Detailed Targeting → Demographics → Household income → India**. This is
the actual filter to use, not a proxy. Data source is third-party-modelled ("high-quality
data sources," per Meta's own banner), so treat it as directionally right rather than
verified-to-the-rupee — but it's a real income percentile, not an interest guess.

| Bracket | Est. India population |
| --- | --- |
| Top 10% | 228.6M – 268.8M |
| Top 11%–20% | 117.3M – 137.9M |
| Top 21%–30% | 111.8M – 131.5M |
| Top 31%–40% | 85.9M – 101.0M |
| Top 41%–50% | 74.2M – 87.2M |
| Lower than 50% | 556.9M – 654.9M |

**Layer 1 — Household income (required, this is the primary filter):**

Default recommendation across all ad sets: select **Top 10%** and **Top 11%–20%**
together (i.e. top quintile nationally). These sizes are national, not city-level — the
location targeting below is what narrows a 100M+ nationwide bracket down to a usable
audience in each city.

- **Ad Set C (Mumbai Fly-In Premium):** Top 10% only. Smallest, richest segment; the
  fly-in market can bear the tightest income cut.
- **Ad Sets A and B (Kerala / Bangalore-TN):** Top 10%–20%, extend to **Top 21%–30%** if
  delivery is thin in the smaller cities (Kozhikode, Coimbatore, Trivandrum) — three
  brackets is still a meaningful premium cut, and these markets have less population to
  draw from than Bangalore, Chennai or Mumbai.

### Layer 2 — narrow by travel & resort intent (must ALSO match ANY of)

Income alone selects wealthy people generally, not people currently in a travel-buying
mindset — narrow with interest to keep the audience relevant. Search and verify each
against the live catalogue before building; some may not exist in India's inventory, same
caveat as "no biryani interest exists" in the sister campaign:

| Interest / topic to search | Category |
| --- | --- |
| Luxury travel | interest |
| Resort | interest |
| Boutique hotel | interest |
| Ecotourism | interest |
| Wildlife tourism | interest |
| Honeymoon | interest |
| Kerala tourism | interest |
| Wellness tourism / Ayurveda | interest |
| Bed and breakfast | interest |
| MakeMyTrip / Yatra / Booking.com / Airbnb | interest (OTA usage as travel-booking proxy) |

### Layer 3 — optional further narrow (behavior proxies, use only if reach is still too broad)

With income + travel intent already in place, this layer is now a backup, not the core
mechanism it was before income targeting was available:

| Interest / behavior to search | Category | Why it's a proxy |
| --- | --- | --- |
| Frequent travelers | behavior | High-travel-frequency segment |
| Business travelers | behavior | Corporate offsite / MICE booking signal |
| Luxury goods | interest | Premium-brand affinity signal |
| Online spenders / Engaged shoppers | behavior | Comfortable completing a high-value booking on a phone |

### Layer 4 — optional: job title / employer targeting (advanced, smaller reach, Ad Set D only)

A second, independent way to confirm "high-profile" alongside modelled income — worth
running as its own small test rather than stacking onto the main ad sets, since combining
income + job title + interest narrows the audience to almost nothing:

- Job titles: "Founder", "CEO", "Director", "Vice President", "Chief Executive Officer",
  "Managing Director"
- Employers: large IT/tech employers concentrated in Bangalore and Chennai — type
  specific company names into the Employer field in Ads Manager and add whichever
  resolve, matching them to the two Tamil Nadu/Karnataka locations above

**Advantage detailed targeting:** OFF — that's the definition of "custom" here. Accept
the smaller, slower-filling audience as the cost of precision.

## Ad set structure — recommended split

| Ad set | Locations | Income (Layer 1) | Targeting | Purpose |
| --- | --- | --- | --- | --- |
| A — Kerala Premium | Kochi, Kozhikode, Trivandrum | Top 10%–20% (extend to 30% if thin) | + Layer 2, optionally Layer 3 | Local high-intent, shortest booking friction, likely cheapest CPL |
| B — Bangalore/TN Weekend Drive | Bangalore, Chennai, Coimbatore | Top 10%–20% | + Layer 2, optionally Layer 3 | Largest volume opportunity, drive-market messaging (weekend, short-lead) |
| C — Mumbai Fly-In Premium | Mumbai | Top 10% only | + Layer 2 | Smallest but highest-AOV segment — justifies a richer creative (video, longer stay packages) and a higher bid ceiling |
| D — Executive (optional) | All four | Top 10% | + Layer 4 (job title) instead of Layer 2/3 | Small-budget test of income + job-title stacked; expect very high CPM, judge on booking value not cost-per-click |

Splitting by geography rather than one blended audience lets each region's cost-per-result
be compared directly — Bangalore and Mumbai will not perform the same, and blending them
hides which one is actually carrying the budget, the same lesson the biryani campaign
learned the hard way city-by-city.

## Retargeting — build these from day 1

Same reasoning as the sister campaign: they take weeks to fill, so start them at launch
even if week 1's budget doesn't use them yet.

| Audience | Source | Window |
| --- | --- | --- |
| Website Visitors — All | resort website (needs Meta Pixel installed) | 180 days |
| Website Visitors — Booking/Enquiry page | resort website, booking or contact-form URL | 90 days |
| Video Viewers 50%+ | resort video ads | 365 days |
| Instagram Engagers | resort Instagram account | 365 days |
| Facebook Page Engagers | resort Facebook Page | 365 days |

**Lookalike:** once Website Visitors (or a completed-booking Custom Audience, if a
conversion pixel event exists) passes roughly 300–1,000 people, build a 1–3% India
lookalike from it — this is likely to outperform every interest-based ad set above once
it has enough seed data, because it learns from people who actually engaged rather than
from guessed interests.

## Building this by hand in Ads Manager today (no API needed)

1. Ads Manager → **Audiences** → **Create Audience** → **Saved Audience**.
2. Under **Locations**, add each city from the table above individually, set its radius,
   and add Wayanad district as an exclusion.
3. Set **Age** to the chosen band (28–58, or split into 28–40 / 41–58 per ad set).
4. Leave **Gender** as All.
5. Under **Detailed Targeting**, search "household income" and add the bracket(s) for
   this ad set from **Demographics → Household income → India** (Layer 1) — these
   combine as OR with each other automatically.
6. Click **Narrow Audience**, then add the Layer 2 travel/resort interest terms as the
   next, ANDed group ("Must Match at least ONE of the following").
7. Optional: **Narrow Audience** again and add Layer 3 behavior terms as a third ANDed
   group only if the audience size is still larger than needed.
8. Leave **Advantage Detailed Targeting toggled OFF.**
9. Name it clearly per ad set, e.g. `Cristal Kuruva | Bangalore-TN | Top20% + Travel Intent`,
   and save — a Saved Audience can be reused across future ad sets without rebuilding it.

Watch the audience-size estimate in the right-hand panel as you stack layers — income
brackets alone run into the hundreds of millions nationally, so it's the location +
interest layers doing the real narrowing down to a usable city-level number. If a
combination collapses to a very small size (this is likely for Ad Set D with income +
job title stacked), that's expected — it's a small, expensive, high-precision test, not
the main prospecting engine.

As you type each Layer 1/2/3 term into Detailed Targeting, Ads Manager's own autocomplete
tells you in real time whether it exists in the live catalogue and shows its audience
size — treat that as the verification step. Some terms above may not resolve; the biryani
campaign found several category-specific interests simply don't exist in Meta's India
inventory, so don't be surprised if a few of these don't either. Drop whichever don't
resolve and keep the rest — the layers don't depend on every single term existing.
