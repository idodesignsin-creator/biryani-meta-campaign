# Targeting

## Locations — 12 cities with radii

Set as **"People living in this location"**, not "recently in this location". Travellers
and visitors don't stock a home kitchen.

| # | City | State | Radius | Coverage |
| --- | --- | --- | --- | --- |
| 1 | Hyderabad | Telangana | 25 km | City + suburbs |
| 2 | Delhi NCR (pin on Delhi) | Delhi | 30 km | Delhi + Gurugram + Noida + Ghaziabad |
| 3 | Mumbai | Maharashtra | 25 km | Mumbai + suburbs (incl. Thane, Navi Mumbai) |
| 4 | Bengaluru | Karnataka | 20 km | City + surrounding areas |
| 5 | Kolkata | West Bengal | 20 km | City + suburbs |
| 6 | Lucknow | Uttar Pradesh | 15 km | City proper |
| 7 | Pune | Maharashtra | 15 km | City + nearby areas |
| 8 | Kochi | Kerala | 12 km | City proper |
| 9 | Jaipur | Rajasthan | 15 km | City + suburbs |
| 10 | Chennai | Tamil Nadu | 15 km | City + nearby areas |
| 11 | Indore | Madhya Pradesh | 12 km | City proper |
| 12 | Ahmedabad | Gujarat | 15 km | City + suburbs |

### How to enter these

In Ads Manager, type the city name, select it, then click the radius dropdown next to it
and set the km value. Two practical notes:

- **The radius control snaps to preset steps** for some locations. If 12 km isn't
  offered for Kochi or Indore, take the nearest available (10 km or 15 km) — the
  difference is immaterial to delivery at this budget. Don't spend time fighting it.
- **Delhi NCR is one pin, not four.** Dropping Delhi + 30 km covers Gurugram, Noida,
  Ghaziabad and Faridabad. Adding those cities separately on top creates overlapping
  circles and inflates your reported reach without adding people.

### One thing worth flagging

Hyderabad, Lucknow and Kolkata are strong biryani cities — but they're also cities with
deeply entrenched local masala habits and neighbourhood spice shops selling loose whole
spices cheaply. Kochi is your home market (Ernakulam), so brand familiarity may be
higher but the addressable Amazon-buying population is much smaller than Mumbai's.

Watch cost-per-landing-page-view **by city** in the delivery breakdown at day 7. Expect
2–4 of these 12 to carry most of the efficient volume. Cutting the bottom performers in
week 2 is usually the single highest-leverage optimisation you'll make.

## Gender — my recommendation: All, not female-only

You asked whether to run female-only. I'd advise against it for the first week, for four
reasons:

1. **The buyer and the cook aren't always the same person.** You're advertising to an
   Amazon purchase, not a kitchen. On Amazon India the registered account holder and the
   saved payment method skew male in a large share of households — the ad can be seen by
   a woman, but the order gets placed on her husband's or son's account, and Meta credits
   whoever *clicked*. Female-only targeting suppresses reach to the person who completes
   the transaction.

2. **Biryani specifically over-indexes with male home cooks.** Everyday cooking in India
   skews female; *project* cooking — weekend biryani, dum handi, grinding your own
   masala — is one of the few categories where male participation is high and rising.
   Your product is explicitly the project-cooking version (whole spices you grind
   yourself, not a shortcut powder). That's the male-skewing end of the category.

3. **At ₹500/day, halving the audience costs you more than the precision gains.** Meta
   needs roughly 50 optimisation events per ad set per week to leave the learning phase.
   Narrower targeting means higher CPM and fewer events, so you stay in "Learning
   limited" longer, which degrades delivery *and* leaves your data too noisy to act on.

4. **Meta will tell you the answer for free in 7 days.** The gender breakdown is a
   standard delivery report. Buying that answer with one week of data beats guessing it
   at launch and never finding out you were wrong.

**So:** launch **All genders**, then at day 7 open Ads Manager → Breakdown → By Delivery
→ Gender and look at cost per landing page view. If women are meaningfully cheaper — say
25%+ better CPLPV at reasonable volume — narrow to women in week 2 and put the saved
budget behind them. If it's close, stay broad.

If you'd rather not wait, the compromise is to split Ad Set A into two identical ad sets,
one female-only and one male-only, and let them compete. Be aware that at ₹500/day across
three ad sets each one gets ~₹165/day, which is genuinely thin — you'd be buying a
cleaner gender read at the cost of a slower, noisier creative read. I'd take the
breakdown report instead.

## Age — 25 to 54

Two forces pull in opposite directions:

- **Older skew argument:** grinding whole spices at home is a more committed cook.
  Established kitchens, higher disposable income, more likely to pay a premium over a
  ₹60 supermarket powder.
- **Younger skew argument:** 25–34 has materially cheaper CPMs on Instagram and Reels,
  is more comfortable buying a food product from an ad, and is the demographic actively
  rediscovering from-scratch cooking.

25–54 covers both and gives the delivery system room to find where the money actually is.
Under 25 rarely holds the household grocery budget; over 54 tends to have fixed masala
loyalties that a small test budget won't shift.

Review the age breakdown at day 7 at the same time as gender. If one bracket is clearly
carrying delivery, split it into its own ad set in week 2 rather than just narrowing —
that way you keep the volume and gain the control.

## Ad Set A — Metro Spice Buyers (interest-targeted)

**Locations:** the 12 cities above · **Age:** 25–54 · **Gender:** All

**Detailed targeting — Layer 1, include ANY of:**

*Cooking & cuisine*
- Cooking
- Indian cuisine
- Biryani
- Recipe
- Food and drink
- Cooking shows / MasterChef India
- Vegetarian cuisine

*Spice-specific (check availability in the picker — Meta's catalogue shifts)*
- Garam masala
- Spice
- Herbs and spices
- Masala

**Layer 2 — NARROW by (must ALSO match ANY of):**
- Online shopping
- Amazon.in / Amazon.com
- Engaged Shoppers (behaviour)

The narrowing is the whole point. Layer 1 alone is enormous and full of people who watch
food reels but have never bought a spice online. Layer 2 alone is full of people buying
phone cases. The intersection is your buyer.

**Advantage detailed targeting:** ON. Let Meta expand past your guesses when it finds
cheaper results — at this budget, take the help.

**Languages:** leave blank. Restricting to English or Hindi cuts reach without improving
quality; your creative does the language filtering by itself.

## Ad Set B — Broad (no interests)

**Locations:** the same 12 cities · **Age:** 25–54 · **Gender:** All
**Detailed targeting:** none · **Advantage+ Audience:** ON, with the Layer 1 interests
supplied as *suggestions* (Meta treats them as a hint, not a constraint)

The hypothesis worth testing: Meta's delivery system, given good creative and a clean
optimisation signal, finds buyers better than interest guesses do. This is true more
often than most advertisers expect.

Ad Set B will almost certainly show lower CPM and often lower cost per landing page view.
**Do not declare it the winner on Meta metrics alone** — cheaper visits are only better
if they convert on Amazon, and only Amazon Attribution can tell you that.

## Exclusions

Phase 1: exclude nothing. Your audiences are too small to carve up, and Amazon gives you
no purchaser list to suppress.

Phase 2 prospecting: exclude everyone in your retargeting custom audiences.

## Retargeting audiences — create these on day 1

They take weeks to fill, so build them at launch even though you won't use them until
week 3.

| Audience | Source | Window |
| --- | --- | --- |
| Video Viewers 50%+ | All campaign video ads | 365 days |
| Video Viewers 3s+ | All campaign video ads | 365 days |
| Instagram Engagers | Spiceto IG account | 365 days |
| Facebook Page Engagers | Spiceto FB Page | 365 days |
| Website Visitors | spiceto.in (needs pixel installed) | 180 days |

**Lookalikes:** wait until Video Viewers 50% passes ~1,000 people, then build a 1% India
lookalike from it. Below that seed size the lookalike is noise.

## The structural limitation you should know about

**You cannot retarget people who viewed your ASIN.** Amazon does not share detail-page
views, add-to-carts, or purchases with Meta. Your entire retargeting pool has to be built
from on-Meta engagement — video views, page engagement, profile visits.

That's precisely why the lead creative is a video: it manufactures a retargeting audience
you would otherwise never have. Treat video-view volume in Phase 1 as a real objective,
not a vanity metric.

Ways around it, in order of effort:

1. **On-Meta engagement pools** (above) — free, immediate, lower intent.
2. **spiceto.in as an intermediate landing page** — you already own the domain. Put the
   Meta pixel on a page that showcases the product and links to Amazon. Costs ~10–20% of
   clicks in drop-off; buys real retargeting and eventually conversion optimisation.
   Worth doing above ~₹2,000/day.
3. **Amazon DSP** — retarget ASIN viewers inside Amazon's ecosystem. Separate platform,
   separate budget, needs meaningful monthly spend to justify.

## Category note

Food and spices are not a Meta special ad category, so you have full targeting available.
Keep it that way by avoiding health claims in copy — see the compliance table in
`ad-copy.md`.
