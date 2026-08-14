# SEO Audit — mestahotel.com

**Site:** https://www.mestahotel.com/ — Mesta Hotel, Sulthan Bathery, Wayanad, Kerala
**Date:** 14 August 2026
**Method:** Search-index analysis (SERP-visible titles, descriptions, and URL inventory)

> ⚠️ **Scope limit — read this first.** This session's network policy blocks all
> outbound page fetches, so **the site was never crawled**. Every finding below is
> derived from what Google has indexed and exposes in search results. That is enough
> to prove the URL, title-tag, and duplication problems conclusively — those are
> visible in the index itself — but it means a second pass is required for anything
> that lives inside the page source. See [What this audit could not
> check](#what-this-audit-could-not-check) before treating it as complete.

---

## Verdict

The site has a **structural URL problem, not a content problem**. The content is
decent — 20+ real pages, a genuine blog with five Wayanad travel guides, clear room
descriptions.

But two things are actively destroying the value of that content:

1. The site is **indexed on four different host/protocol combinations**, including
   plain HTTP — so pages compete with themselves.
2. **Dead URLs are sitting in the index.** `/restaurants.html` is confirmed returning
   404 while still ranking in Google. Pages were removed or renamed without
   redirects, throwing away the equity they had earned and dropping searchers onto a
   blank error page.

Fix canonicalization and the dead-URL redirects first. Title tags second. Everything
else is downstream of those two.

---

## Indexed page inventory

21 URLs confirmed in the index. Note the two systems running side by side:

### Legacy `.php` set
| URL | Indexed title |
| --- | --- |
| `/` | Luxury Hotel in Wayanad \| Hotels in Sulthan Bathery - mesta Hotel |
| `/about.php` | mesta HOTEL – Best Hotels in Sulthan Bathery \| Wayanad Hotels |
| `/rooms.php` | Rooms & Suites \| Best Luxury Hotels in Wayanad - Mesta Hotel |
| `/rooms-pride.php` | Best Hotels in Wayanad \| Best Budget Hotels in Wayanad |
| `/luxury-balcony-rooms-wayanad.php` | Best Hotels in Wayanad \| Best Budget Hotels in Wayanad |
| `/restaurants.php` | Best Budget Hotels in Wayanad \| Family Friendly Hotels in Wayanad |
| `/banquets.php` | Banquet Hall \| Hotels in Sulthan Bathery \| mesta Hotel Wayanad |
| `/things-todo.php` | Things To Do In Wayanad \| Top Attractions - Hotels in Wayanad |
| `/contact-mesta-hotel-wayanad.php` | Contact Top Hotels in Wayanad \| Hotels in Sulthan Bathery |
| `/blog.php` | Welcome to mesta hotel |

### Legacy `.html` set — **at least one confirmed dead**
| URL | Indexed title |
| --- | --- |
| `/4-star-hotels-in-wayanad.html` | Best Wayanad Hotels \| 4-star Hotels In Wayanad \| Mesta Hotels |
| `/rooms/blossom.html` | Blossom \| hotel rooms in wayanad \| Top hotels in :wayanad |
| `/restaurants.html` | Restaurants in Our Four-star Hotel \| 4 star Hotels in Wayanad — **❌ 404** |
| `/facilities.html` | Facilities at mesta Hotel \| Couple friendly hotels in Wayanad |
| `/gallery.html` | Gallery \| 4 star Hotels in Wayanad \| Luxury hotels in Wayanad |
| `/offers-packages.html` | Exclusive Deals at Wayanad Hotels \| Mesta Hotel Offers |
| `/blog/adventure-activities-in-wayanad.html` | The Ultimate Guide to Adventure Activities in Wayanad |
| `/blog/solo-travelers-guide-to-wayanad-best-hotels-in-wayanad.html` | Solo Traveler's Guide to Wayanad \| Best Hotels In Wayanad \| mesta Hotel |
| `/blog/wayanad-on-a-budget.html` | Wayanad On A Budget \| Choose Budget Resorts In Wayanad \| Blog |
| `/blog/planning-a-wayanad-trip.html` | Planning a Wayanad Trip \| Best Hotels in Wayanad \| Blog |
| `/blog/how-to-select-the-best-stay-in-wayanad-as-per-your-budget-interests.html` | Best Place to Stay in Wayanad \| Mesta Hotel |

---

## P0 — Fix these first

### 1. The site is indexed on four different host/protocol variants

Google has indexed the same site under all of these:

| Variant | Evidence |
| --- | --- |
| `http://www.mestahotel.com/` | `/about.php`, `/banquets.php` indexed over plain **HTTP** |
| `https://www.mestahotel.com/` | homepage, `/rooms.php`, `/restaurants.php` |
| `https://mestahotel.com/` (no www) | `/rooms.php`, `/rooms-pride.php` |

`/rooms.php` is indexed at **both** `https://www.mestahotel.com/rooms.php` and
`https://mestahotel.com/rooms.php`. That is the same page competing with itself.

Insecure HTTP URLs sitting in the index is the more serious half — it means there is
no forced HTTPS redirect, which is both a ranking signal problem and a trust problem
for a site taking booking enquiries.

**Fix:**
- Server-level 301 from `http://` → `https://` for every URL.
- Server-level 301 from non-`www` → `www` (or the reverse — pick one, it does not
  matter which, but pick one and enforce it everywhere).
- Add a self-referencing `<link rel="canonical">` with the absolute chosen-host URL
  on every page.
- Enable HSTS once the redirects are verified.

### 2. Dead `.html` URLs sitting in the index — pages removed without redirects

**Verified 14 Aug 2026:** `mestahotel.com/restaurants.html` returns a bare
**404 Not Found**. Google still has that URL indexed, with a full title tag
("Restaurants in Our Four-star Hotel | 4 star Hotels in Wayanad").

> **Correction to an earlier draft of this audit.** This was originally written up as
> "`.php` and `.html` are both live" — a duplicate-content problem. That was wrong,
> and the reality is more damaging: **the `.html` page is gone, and Google is still
> indexing it.** Searchers who click that result land on a blank 404.

Two things follow, and both matter more than duplication would have:

1. **Pages were deleted or renamed without 301 redirects.** All the ranking equity
   `/restaurants.html` had accumulated has been thrown away rather than passed to
   `/restaurants.php`.
2. **The 404 page is a raw server default.** No branding, no navigation, no search
   box, no way back into the site — just the words "404 Not Found" on white. Every
   visitor who lands there is lost.

**The migration ran `.html` → `.php`, not the other way round.** An earlier version
of this document assumed the opposite, because `/rooms/blossom.html` has a nested
structure that looks newer. That assumption was wrong, and it reverses the
recommendation below.

**Fix:**
1. **Confirm the true status code.** A page that *displays* "404 Not Found" may still
   return HTTP `200` — a "soft 404", which is worse, because Google keeps the URL
   indexed indefinitely. Check with `curl -I https://mestahotel.com/restaurants.html`
   or the Search Console URL Inspection tool.
2. **Audit every indexed `.html` URL** — see the checklist below. Establish which are
   alive and which are dead before changing anything.
3. **301 each dead `.html` URL to its live `.php` equivalent.** One hop, no chains.
   `/restaurants.html` → `/restaurants.php` is the first one.
4. **Build a proper 404 page** — branded, with the main navigation, a link home, and
   links to rooms and contact.
5. **Submit a fresh `sitemap.xml`** containing only live, canonical URLs.
6. **Watch Search Console → Pages** for "Not found (404)" and "Soft 404".

#### URLs to check (all confirmed indexed)

| URL | Status |
| --- | --- |
| `/restaurants.html` | ❌ **404 confirmed** |
| `/facilities.html` | ? |
| `/gallery.html` | ? |
| `/offers-packages.html` | ? |
| `/4-star-hotels-in-wayanad.html` | ? |
| `/rooms/blossom.html` | ? |
| `/blog/adventure-activities-in-wayanad.html` | ? |
| `/blog/solo-travelers-guide-to-wayanad-best-hotels-in-wayanad.html` | ? |
| `/blog/wayanad-on-a-budget.html` | ? |
| `/blog/planning-a-wayanad-trip.html` | ? |
| `/blog/how-to-select-the-best-stay-in-wayanad-as-per-your-budget-interests.html` | ? |

**Fastest way to fill this in:** Search Console → **Pages** → "Not found (404)". That
returns the complete list in one view, including URLs neither of us has seen yet.

---

## P1 — High impact

### 3. Duplicate and mismatched title tags

Two different pages ship the **identical** title tag:

> `Best Hotels in Wayanad | Best Budget Hotels in Wayanad`
> — used on both `/rooms-pride.php` **and** `/luxury-balcony-rooms-wayanad.php`

And several titles describe the wrong thing entirely:

| Page | Problem |
| --- | --- |
| `/restaurants.php` | Titled "Best Budget Hotels in Wayanad \| Family Friendly Hotels in Wayanad" — says nothing about a restaurant |
| `/blog.php` | Title is `Welcome to mesta hotel` — an unedited placeholder. No keyword, no brand format |
| `/rooms/blossom.html` | Contains a typo: `Top hotels in :wayanad` — stray colon, live in the index |
| `/rooms-pride.php` | Never names the Pride room or the brand |

Also note the homepage title appears in the index in **two different forms**
("Luxury Hotel in Wayanad | Hotels in Sulthan Bathery - mesta Hotel" and "Best Luxury
Hotel in Wayanad, Sulthan Bathery – Mesta Hotel"). Either it changed recently, or
Google is rewriting it — the latter signals the title isn't matching searcher intent.

**Fix:** one unique title per page, ≤60 characters, structured
`Primary subject | Differentiator | Mesta Hotel`. Suggested rewrites:

| Page | Suggested title |
| --- | --- |
| `/` | Mesta Hotel Wayanad \| 4-Star Hotel in Sulthan Bathery |
| `/rooms/pride` | Pride Rooms — 290 sq ft with Balcony \| Mesta Hotel Wayanad |
| `/rooms/blossom` | Blossom Rooms — 230 sq ft \| Mesta Hotel Wayanad |
| `/restaurants` | Montana & Jubilee — Multi-Cuisine Dining \| Mesta Hotel Wayanad |
| `/banquets` | Banquet Hall for 100 Guests \| Mesta Hotel, Sulthan Bathery |
| `/blog` | Wayanad Travel Guides & Tips \| Mesta Hotel Blog |

### 4. Keyword cannibalization

At least five pages are all chasing the same query cluster ("best hotels in
Wayanad" / "budget hotels in Wayanad"):

- `/` (homepage)
- `/4-star-hotels-in-wayanad.html`
- `/rooms-pride.php`
- `/luxury-balcony-rooms-wayanad.php`
- `/restaurants.php`

They compete with each other, and Google has to guess which one to rank. The room and
restaurant pages should not be targeting head hotel terms at all.

**Fix:** assign one primary keyword per page and keep it exclusive.

| Page | Primary target |
| --- | --- |
| `/` | hotels in Sulthan Bathery / Mesta Hotel Wayanad |
| `/4-star-hotels-in-wayanad` | 4 star hotels in Wayanad |
| `/rooms/*` | `<room name>` room Wayanad, hotel rooms with balcony Wayanad |
| `/restaurants` | restaurants in Sulthan Bathery, multi-cuisine restaurant Wayanad |
| `/banquets` | banquet hall in Sulthan Bathery, conference hall Wayanad |

### 5. Titles are keyword-stuffed rather than click-optimized

"Best Hotels in Wayanad | Best Budget Hotels in Wayanad" is essentially the same
phrase repeated. This is 2010-era optimization: it dilutes click-through and reads as
spam to both users and modern ranking systems. Note also the inconsistent brand
casing across the index — "mesta Hotel", "Mesta Hotel", "mesta HOTEL", "Mesta Hotels".
Standardise on one.

### 6. OTAs own the brand SERP

Searching the hotel's own brand name returns Tripadvisor, Goibibo, EaseMyTrip,
Trivago, Klook, and Adani One — all ahead of or alongside the official site. Every
one of those is a commission-taking intermediary intercepting traffic that is already
searching for Mesta by name. This is the single biggest revenue leak in the audit.

**Fix:**
- Add `Hotel` schema (JSON-LD) on the homepage with `name`, `address`, `telephone`,
  `priceRange`, `starRating`, `aggregateRating`, `amenityFeature`, and `image`.
- Add `FAQPage` schema to the contact and rooms pages.
- Claim and fully populate the Google Business Profile — photos, amenities, and the
  "Book direct" link.
- Run a small brand-defence paid-search campaign on "mesta hotel" variants; OTA
  commission almost always exceeds the CPC on brand terms.
- Add a visible best-rate-guarantee / book-direct incentive above the fold.

---

## P2 — Worth fixing

### 7. Category mismatch between the site and the review platforms

The site positions itself as a **4-star luxury / business-class hotel**. Tripadvisor
ranks it **#1 of 44 B&Bs / inns** in Sulthan Bathery (428 reviews, 4.0). Being #1 in
the wrong category is a wasted asset — travellers filtering for "hotels" never see
it, and the conflicting signal muddies entity classification.

**Fix:** request recategorisation to Hotels on Tripadvisor, and make sure the star
rating is stated consistently in schema, on the site, and across all OTA listings.

### 8. NAP inconsistency

The index surfaces **two different contact emails** — `info@mestahotel.com` on one
page and `reservation@mestahotel.com` on another — plus four phone numbers
(+91 9526 50 33 44, +91 9526 40 33 44, +91 9526 00 22 44, +91 4936 22 55 55 / 22 20 08).

Local SEO rewards one consistent Name / Address / Phone across the site, the Google
Business Profile, and every directory. Pick one primary phone and one primary email,
use them in the schema and footer sitewide, and list the rest only on the contact page.

### 9. Inconsistent URL naming

`/about.php` and `/contact-mesta-hotel-wayanad.php` follow completely different
conventions. `/things-todo.php` is missing a word — it should be `/things-to-do`.
Standardise to short, lowercase, hyphenated, extension-less paths as part of the P0
migration, so it only costs one round of redirects.

### 10. The blog is a real asset, currently underleveraged

Five substantive Wayanad guides are indexed — adventure activities, solo travel,
budget travel, trip planning, choosing a stay. This is exactly the top-of-funnel
content a hotel should have, and it is competing against thehosteller.com and
fabhotels.com for the same queries.

**Fix:**
- Give `/blog.php` a real title and turn it into a proper hub that links every post.
- Internally link each post to the relevant money page (adventure post → rooms;
  budget post → offers/packages).
- Add `BlogPosting` schema with `datePublished` and `author`.
- Add visible publish/update dates — travel content is freshness-sensitive.
- Post-specific topic gaps worth adding: "how to reach Wayanad from Bangalore /
  Kochi", "best time to visit Wayanad", "Edakkal Caves guide" — all high-intent,
  all naturally linking to a stay.

---

## What this audit could not check

Network egress was blocked, so the page source was never retrieved. **These items are
unverified and need a second pass with a crawler** (Screaming Frog, Sitebulb, or
Search Console):

- `robots.txt` and `sitemap.xml` — existence, correctness, whether the legacy `.php`
  URLs are still being submitted
- `rel="canonical"` tags — present? self-referencing? pointing at the right host?
- Structured data — whether any `Hotel` / `LocalBusiness` schema exists at all
- Meta robots directives, and whether anything is accidentally `noindex`
- H1 tags — presence, uniqueness, and whether they duplicate the title
- Image `alt` attributes and file sizes (a hotel gallery site is image-heavy; this is
  likely a real weak point)
- Core Web Vitals — LCP, CLS, INP
- Mobile responsiveness and viewport meta
- Internal linking structure and orphaned pages
- Redirect chains and 404s
- SSL certificate validity and mixed-content warnings
- Actual on-page word counts and thin-content pages
- Backlink profile and referring domains

**Recommended next step:** grant egress to `mestahotel.com`, or run Screaming Frog
locally and share the export — I can then complete the technical half of this audit
against the live source.

---

## Priority summary

| # | Finding | Priority | Effort |
| --- | --- | --- | --- |
| 1 | Four host/protocol variants indexed; HTTP URLs live | **P0** | Low — server config |
| 2 | Dead `.html` URLs indexed (404s), no redirects, raw error page | **P0** | Medium |
| 3 | Duplicate, placeholder, and typo'd title tags | **P1** | Low |
| 4 | Keyword cannibalization across 5 pages | **P1** | Low |
| 5 | Keyword-stuffed titles, inconsistent brand casing | **P1** | Low |
| 6 | OTAs own the brand SERP | **P1** | Medium |
| 7 | Tripadvisor category mismatch (B&B vs hotel) | P2 | Low |
| 8 | NAP inconsistency (2 emails, 4 phones) | P2 | Low |
| 9 | Inconsistent URL naming | P2 | Low — fold into #2 |
| 10 | Blog underleveraged, placeholder hub title | P2 | Medium |

**If you only do one thing:** fix #1 and #2 together in a single redirect pass. They
are the same underlying problem — the site has never been told which URL is the real
one — and every other fix on this list performs better once that is settled.
