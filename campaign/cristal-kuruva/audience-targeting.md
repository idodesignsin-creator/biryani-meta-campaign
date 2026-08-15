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
- **Location keys below are placeholders.** I could not resolve live Meta location IDs
  because the Adspirer API quota is exhausted this period (see the folder README). In
  Ads Manager you don't need an ID to build this by hand — type the city name, pick it
  from the dropdown, set the radius. The IDs only matter for the API path in
  `audience-spec.json`, and that file is marked `null` until they're resolved.

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

## The honest limit on "high-profile / high-converting"

Meta does not expose direct household-income or net-worth targeting for India (that
option only exists for a handful of countries, the US chief among them). There is no
"high-profile" or "premium" interest to select. What follows is the closest available
proxy, built the same way the biryani campaign's Ad Set A was built — a broad relevant
layer, narrowed by a spend/travel-behavior layer:

### Layer 1 — travel & resort intent (include ANY of)

Search and verify each against the live catalogue before building — some may not exist
in India's inventory, same caveat as "no biryani interest exists" in the sister campaign:

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

### Layer 2 — narrow by spending-power proxy (must ALSO match ANY of)

| Interest / behavior to search | Category | Why it's a proxy |
| --- | --- | --- |
| Frequent travelers | behavior | Meta's standard high-travel-frequency segment — the single best India-available proxy for disposable income spent on trips |
| Business travelers | behavior | Corporate offsite / MICE booking signal, and generally higher personal spend |
| Luxury goods | interest | Broad but real premium-brand affinity signal |
| Online spenders / Engaged shoppers | behavior | Meta's proxy for people who transact online frequently, i.e. comfortable completing a high-value booking on a phone |
| Small business owners | behavior | Household income proxy where direct income targeting doesn't exist |

### Layer 3 — optional: job title / employer targeting (advanced, smaller reach)

Meta India does support job-title and employer targeting. This is the most direct
"high-profile" lever available, at the cost of a much smaller, more expensive-to-fill
audience — treat it as a separate, smaller-budget test ad set rather than the main
prospecting engine:

- Job titles: "Founder", "CEO", "Director", "Vice President", "Chief Executive Officer",
  "Managing Director"
- Employers: large IT/tech employers concentrated in Bangalore and Chennai (worth
  resolving specific company names once quota resets and matching them to the two Tamil
  Nadu/Karnataka locations above)

**Advantage detailed targeting:** OFF — that's the definition of "custom" here. Accept
the smaller, slower-filling audience as the cost of precision.

## Ad set structure — recommended split

| Ad set | Locations | Targeting | Purpose |
| --- | --- | --- | --- |
| A — Kerala Premium | Kochi, Kozhikode, Trivandrum | Layer 1 + Layer 2 | Local high-intent, shortest booking friction, likely cheapest CPL |
| B — Bangalore/TN Weekend Drive | Bangalore, Chennai, Coimbatore | Layer 1 + Layer 2 | Largest volume opportunity, drive-market messaging (weekend, short-lead) |
| C — Mumbai Fly-In Premium | Mumbai | Layer 1 + Layer 2, optionally add Layer 3 | Smallest but highest-AOV segment — justifies a richer creative (video, longer stay packages) and a higher bid ceiling |
| D — Executive (optional) | All four | Layer 3 only | Small-budget test of job-title/employer targeting; expect high CPM, judge on booking value not cost-per-click |

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
5. Under **Detailed Targeting**, add the Layer 1 terms as "Must Match at least ONE of the
   following" (Meta's default OR grouping), then click **Narrow Audience** and add the
   Layer 2 terms as the second, ANDed group.
6. Leave **Advantage Detailed Targeting toggled OFF.**
7. Name it clearly per ad set, e.g. `Cristal Kuruva | Bangalore-TN | Premium Travel Intent`,
   and save — a Saved Audience can be reused across future ad sets without rebuilding it.

## What to do once Adspirer quota resets (2026-09-04)

1. Run `search_meta_targeting` for each location and each Layer 1/2/3 term above to
   resolve real IDs and confirm each one actually exists in Meta's India catalogue —
   don't assume; the biryani campaign found several category-specific interests simply
   don't exist.
2. Fill the resolved IDs into `audience-spec.json`.
3. Either hand that file to me to attach directly to a new ad set, or use it to double-check
   the manually-built Saved Audience above matches.
