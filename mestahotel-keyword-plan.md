# Mesta Hotel — Steps for Improving the Keywords

**Source:** `Mesta Hotel — SEO Report, July 2026` (35 tracked keywords + GMB data, Feb–Jul 2026)
**Companion doc:** [`seo-audit-mestahotel.md`](seo-audit-mestahotel.md) — the technical audit
**Date:** 14 August 2026

---

## The finding hiding in the July report

Sort the 35 tracked keywords by which location word they contain, and the result is
stark:

| Keyword contains | Ranks page 1 | Ranks page 2 | Not ranking |
| --- | --- | --- | --- |
| **"Sulthan Bathery"** | **8 / 8** | 0 | 0 |
| "Wayanad" + qualifier (family, budget, couple, premium) | 5 | 6 | 2 |
| **"Wayanad" alone** (head terms) | **0** | 0 | **4** |

Every single Sulthan Bathery keyword ranks page 1. Every single unqualified Wayanad
head term — `Hotels In Wayanad`, `Wayanad Hotels`, `Luxury Hotels In Wayanad`,
`Hotel Booking In Wayanad` — fails to rank at all.

**This is not a failure. It is a map.** The site has genuine authority at town level
and none at district level. Wayanad district head terms are owned by OTAs
(Tripadvisor, Goibibo, Agoda, Hotels.com) and by 40+ resorts with far more links.
Chasing them is the most expensive, least winnable thing on the list — and six of the
35 tracked keywords are spent doing exactly that.

The strategy should be: **stop attacking the district head terms, and instead spend
that effort on the long tail where the town-level authority already converts.**

---

## What's wrong with the current keyword set

### 1. "1st Page / 2nd Page" is not a measurement

Position 1 and position 9 are both "1st Page" and differ by roughly 10× in
click-through. The report cannot distinguish a keyword that earns traffic from one
that earns nothing. There is also no search volume, no difficulty, no trend, and no
traffic or conversion attached to any of the 35 terms.

**A keyword ranking #1 with 20 searches a month is worth less than one ranking #7
with 2,000.** Right now there is no way to tell those apart.

### 2. The list has no branded keywords at all

Not one of the 35 terms is `mesta hotel`, `mesta hotel wayanad`, or `mesta hotel
sulthan bathery`. These are the highest-converting queries a hotel has — the searcher
already decided. And per the technical audit, **the brand SERP is currently occupied
by Tripadvisor, Goibibo, EaseMyTrip, Trivago, Klook, and Adani One**, every one of
them taking a commission on a guest who was already looking for you by name.

This is the single most valuable untracked keyword group.

### 3. The positioning contradicts itself

The same list tracks `5 star hotels in sulthan bathery`, `Premium Accommodation In
Wayanad`, `Budget Hotels In Wayanad`, and `Affordable Family Hotels In Wayanad`.

You cannot be the 5-star option and the budget option simultaneously. This muddies
what Google understands the property to be — and it matches the category mismatch
found in the audit, where Tripadvisor lists Mesta as **#1 of 44 B&Bs/inns** while the
site sells itself as 4-star business class. Pick a lane.

### 4. Real assets have zero keyword coverage

The property has these, each with a page already built, and **not one tracked
keyword** pointing at any of them:

| Asset | Tracked keywords |
| --- | --- |
| Banquet hall — 1,000 sq ft, 100 guests, AV + projectors | **0** |
| Two restaurants — Montana, Jubilee, buffet breakfast | **0** |
| Swimming pool | 1 (unranked) |
| 2 km from Sulthan Bathery bus stand | **0** |
| Five published Wayanad travel guides | **0** |

Banquet and conference terms are commercially valuable, locally scoped, and face
almost none of the OTA competition that blocks the hotel terms. They are the easiest
unclaimed wins available.

### 5. One page-1 ranking is the wrong intent

`honeymoon destinations in wayanad` ranks page 1 — but that is someone asking *where
to go*, not *where to stay*. It brings traffic that does not book. The commercial
version is `honeymoon hotels in wayanad` / `honeymoon resorts in wayanad`, which
isn't tracked.

### 6. Two page-2 keywords are stuck because two pages fight for them

From the technical audit: `/rooms-pride.php` and `/luxury-balcony-rooms-wayanad.php`
**ship the identical title tag** — "Best Hotels in Wayanad | Best Budget Hotels in
Wayanad". That exact phrase is tracked keyword #9, and it sits on page 2.

Two pages targeting one term means Google splits the signal and ranks neither.
`Best Budget Hotels In Wayanad` will not move to page 1 until one of those two pages
stops competing. Same story for `Couple Friendly Hotels In Wayanad`, which is
currently carried by `/facilities.html` — a facilities page trying to rank for an
accommodation query.

**Keyword work and the URL cleanup are the same job.** Several of these rankings are
capped by the duplicate-page problem, not by content quality.

---

## The steps

### Step 1 — Re-baseline the measurement (do this first, ~1 day)

Nothing else can be prioritised without this.

1. Move rank tracking off "1st Page / 2nd Page" onto **numeric positions** (Semrush,
   Ahrefs, or SE Ranking — any of them).
2. Attach **monthly search volume** to all 35 existing keywords via Google Keyword
   Planner, filtered to India / Kerala.
3. Connect **Search Console** and pull the actual query report — this shows what the
   site *already* ranks for, which is almost always wider than the tracked list.
4. Split reporting into **branded vs non-branded**.
5. Add **conversions**, not just rankings: booking-engine starts, phone taps, contact
   form submissions.

> ⚠️ I have not assigned volume estimates to any keyword below, because I have no
> access to a keyword tool from this environment and inventing numbers would be
> worse than leaving them blank. Validate every suggestion in Keyword Planner before
> committing budget. The **priority** column reflects competition and commercial
> intent, which can be reasoned about without volume data.

### Step 2 — Cut the six unwinnable head terms

Drop from active targeting: `Hotels In Wayanad`, `Wayanad Hotels`, `Luxury Hotels In
Wayanad`, `Top Budget Hotels In Wayanad`, `Hotel Booking In Wayanad`, `Hotels With
Swimming Pool In Wayanad`.

Keep them in the tracker as a **watch list** — they are useful as a long-run authority
signal — but stop building pages and copy around them. They have produced nothing in
what appears to be a long tracking period, and the competition is structural.

Exception: `Hotels With Swimming Pool In Wayanad` is worth **one** attempt, because
it is an amenity filter with real intent and the hotel genuinely has the pool. Give
it a proper section on the facilities page with images and an `amenityFeature` schema
entry. If it hasn't moved in 90 days, drop it.

### Step 3 — Claim the branded SERP (highest ROI on this list)

Add and track: `mesta hotel`, `mesta hotel wayanad`, `mesta hotel sulthan bathery`,
`mesta hotel booking`, `mesta hotel wayanad contact`, `mesta hotel price`.

Then act on them:
- Add `Hotel` JSON-LD schema to the homepage — `name`, `address`, `telephone`,
  `starRating`, `priceRange`, `aggregateRating`, `amenityFeature`, `image`.
- Fix the brand-name casing, which currently appears in the index as "mesta Hotel",
  "Mesta Hotel", "mesta HOTEL", and "Mesta Hotels". Pick one.
- Run brand-defence paid search on `mesta hotel` variants. OTA commission (typically
  15–20% of booking value) almost always exceeds the CPC on a brand term.
- Add a visible **book-direct / best-rate-guarantee** message above the fold.

### Step 4 — Fix keyword-to-page mapping (blocks Step 5)

One keyword, one page. This requires the duplicate-URL fix from the technical audit.

| Page | Single primary keyword | Currently |
| --- | --- | --- |
| `/` | mesta hotel wayanad *(brand)* | competing on generic head terms |
| `/4-star-hotels-in-wayanad` | 4 star hotels in wayanad | ok |
| `/rooms/pride` | balcony rooms in wayanad | duplicate title with luxury-balcony page |
| `/rooms/blossom` | budget rooms in sulthan bathery | title has a live typo (`:wayanad`) |
| `/rooms/opus-family` | family rooms in wayanad | — |
| `/rooms/signature` | luxury suite rooms in wayanad | already p1 — protect it |
| `/restaurants` | restaurants in sulthan bathery | titled about *budget hotels* |
| `/banquets` | banquet hall in sulthan bathery | untracked |
| `/facilities` | hotels with swimming pool in wayanad | miscast as couple-friendly |
| `/offers-packages` | wayanad hotel packages | already p1 — protect it |

**Retire `/luxury-balcony-rooms-wayanad.php`** — 301 it into `/rooms/pride`. That
single redirect should be enough to move `Best Budget Hotels In Wayanad` off page 2,
because the two pages will stop splitting the signal.

### Step 5 — Add the four missing keyword groups

These are where the growth is. All of them are locally scoped, which is exactly where
the site already demonstrates authority.

**A. Banquet & events — highest priority, zero current coverage**

`banquet hall in sulthan bathery` · `conference hall in wayanad` ·
`wedding venues in sulthan bathery` · `meeting rooms in wayanad` ·
`corporate event venue wayanad` · `party hall sulthan bathery`

Low OTA competition, high booking value, page already exists.

**B. Landmark & proximity — matches how people actually search Wayanad**

`hotels near edakkal caves` · `hotels near wayanad wildlife sanctuary` ·
`hotels near soochipara falls` · `hotels near banasura sagar dam` ·
`hotels near sulthan bathery bus stand` · `hotels near chembra peak`

Wayanad travel is attraction-led. The hotel is 2 km from the bus stand — that's a
ranking asset going completely unused. **The blog already covers every one of these
landmarks**, so the content largely exists; it needs proximity framing and internal
links to the rooms pages.

**C. Restaurant & dining — two restaurants, zero keywords**

`restaurants in sulthan bathery` · `best restaurant in sulthan bathery` ·
`multi cuisine restaurant wayanad` · `buffet breakfast in wayanad` ·
`family restaurant sulthan bathery`

Also captures non-staying local diners, and strengthens the local entity overall.

**D. Route, season & occasion**

`bangalore to wayanad hotels` · `mysore to wayanad stay` ·
`wayanad hotels in monsoon` · `honeymoon hotels in wayanad` *(replaces the
informational variant)* · `hotels in wayanad for weekend trip`

The GMB data shows demand peaking in **May and collapsing through June–July** —
the monsoon. Monsoon-season content is a direct answer to the sharpest weakness in
the annual demand curve.

### Step 6 — Resolve the positioning contradiction

Choose one identity and align keywords, on-page copy, schema `starRating`, and OTA
listings to it. Based on the evidence — 4-star claim, ₹ pricing, business-class
framing, family-heavy reviews — **"4-star family and business hotel"** is the
defensible position.

That means dropping `Budget Hotels In Wayanad` and `Affordable Family Hotels In
Wayanad` as *primary* targets. They currently rank page 1, which feels like a loss —
but budget-seekers convert poorly against a 4-star rate card and drag review scores
when expectations mismatch. Demote them to secondary; do not build new pages for them.

Also request **Tripadvisor recategorisation from B&B/inn to Hotel**. Being #1 of 44
B&Bs is invisible to everyone filtering for hotels.

### Step 7 — Report on outcomes, not positions

Restructure the monthly report around:

| Metric | Why |
| --- | --- |
| Organic sessions, split branded / non-branded | Shows whether SEO or brand is driving it |
| Booking-engine starts and completions from organic | The actual goal |
| Numeric position + volume for the top 20 | Real movement, not page bands |
| GMB → website click-through rate | Currently the weak link — see below |
| Share of voice vs OTAs on brand terms | The main revenue leak |

---

## What the GMB numbers say

Six months, Feb–Jul 2026:

| Action | Total | Monthly avg |
| --- | --- | --- |
| Direction requests | 1,528 | 255 |
| Calls | 694 | 116 |
| Website clicks | **274** | **46** |
| Booking clicks | 272 | 45 |
| Chat clicks | 69 | 12 |

**Directions outnumber website clicks 5.6 to 1.** The Google Business Profile is
doing far more work than the website — people find the listing and navigate straight
there without ever visiting the site.

Two readings, and both are actionable:

1. **Local SEO is working; the website is the weak link.** With ~2,800 profile actions
   in six months, the profile has real visibility. Only 46 people a month click
   through to the site. Improving the listing's photos, description, and booking link
   is likely cheaper per booking than any ranking work in this document.
2. **Everything peaks in May and falls through July.** Calls run ~240 in May and ~85
   in July; directions ~470 down to ~155. That is the monsoon, and it is why keyword
   group **D** matters — right now there is no content addressing the half of the
   year when demand drops.

Worth noting: the report contains a "Google Analytics" section header with no data
behind it. **Organic sessions and conversions are the numbers that would make every
other number in the report interpretable**, and they are missing.

---

## Sequencing

| Order | Step | Effort | Impact |
| --- | --- | --- | --- |
| 1 | Re-baseline measurement (Step 1) | 1 day | Unblocks everything |
| 2 | Branded keywords + Hotel schema (Step 3) | 2–3 days | **Highest** |
| 3 | Fix URL duplication + page mapping (Step 4) | 1 week | High — unblocks stuck rankings |
| 4 | Banquet & events keywords (Step 5A) | 1 week | High — uncontested |
| 5 | Landmark & proximity (Step 5B) | 2 weeks | High — content mostly exists |
| 6 | Restaurant keywords (Step 5C) | 1 week | Medium |
| 7 | Drop head terms, fix positioning (Steps 2, 6) | Ongoing | Medium — frees effort |
| 8 | Route/season/occasion (Step 5D) | Ongoing | Medium — fixes seasonality |

**If you do only one thing:** track and defend the branded keywords. Guests searching
"mesta hotel" by name are currently being handed to Tripadvisor and Goibibo, who
charge 15–20% for a booking the hotel had already earned. That is the most expensive
gap in the current keyword strategy, and it is not on the list at all.
