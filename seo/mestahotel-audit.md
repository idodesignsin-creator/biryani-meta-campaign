# mestahotel.com — SEO Audit

**Site:** https://www.mestahotel.com/ — Mesta Hotel, Main Road, Sulthan Bathery, Wayanad, Kerala 673592
**Date:** 2026-08-14

---

## Method, and what this audit can and cannot claim

**The site could not be crawled from this environment.** `www.mestahotel.com` is blocked by the
network egress policy on this session — both `curl` and the fetch tool return `403` at the proxy,
and `robots.txt` and `sitemap.xml` were unreachable for the same reason. This is a restriction on
my side, not a fault on the server.

Everything below is therefore derived from **search-engine index data**: the URLs Google has
indexed for this domain, and the `<title>` tags it recorded for them. That is a narrower instrument
than a crawl, but it is not a weak one — the index is the search engine's own view of the site,
which is exactly the thing an SEO audit is about. Duplicate URLs, duplicate titles, protocol and
host splits, and encoding bugs are all fully visible in it, and all of them are present here.

**What is verified** (observed directly in the index): the URL inventory, the title tags, the
`http`/`https` and `www`/non-`www` splits, the duplicate-title pairs, the URL encoding bug.

**What is not verified** and must be checked on-page before acting — listed with instructions in
[§7](#7-still-to-verify-on-page): canonical tags, redirects, `robots.txt`, XML sitemap, H1s,
meta descriptions, structured data, internal linking, image alt text, Core Web Vitals, mobile
rendering.

Where I say "verify", I mean it — do not action those items on my word alone.

---

## Executive summary

The site is running **two complete generations of itself at the same time**. An older `.php` site
and a newer `.html` site are both live, both crawlable, and both indexed. Nothing appears to
redirect the old to the new.

The result is that every important page on this site exists at **two to four different URLs**, and
Google has indexed all of them. For a single 4-star hotel in a small town — a site that should be
perhaps 15 pages — the index holds **at least 26 distinct URLs covering roughly 10 unique subjects.**

This is the single highest-impact finding in the audit, and almost everything else is downstream of
it. Ranking signals that should accumulate on one rooms page are being split across eight. Two
pages carry **byte-identical title tags**, which is the most direct evidence of duplication there is.

Three findings are outright defects rather than optimisation opportunities:

1. A live blog URL contains `%EF%BF%BD` — the **Unicode replacement character**, the artefact you
   get when text is decoded with the wrong encoding. An apostrophe in "Wayanad's" was corrupted and
   then baked into a permanent URL.
2. A live, indexed package page has the title **"Soulmate Special Honeymoon Package by mesta - Copy"**.
   A CMS "duplicate this record" artefact has reached production and been indexed.
3. Pages are indexed over **plain `http://`**, meaning HTTPS is not being enforced site-wide.

Priority order: fix the duplication (P0), fix the defects (P0/P1), then rewrite titles (P1).
Do not start with title rewriting — rewriting titles across duplicate URLs is wasted work.

---

## 1. P0 — Duplicate site: two generations live simultaneously

### 1.1 The rooms cluster — 9 URLs for one set of rooms

| # | URL | Indexed `<title>` |
|---|---|---|
| 1 | `https://www.mestahotel.com/rooms.php` | Rooms & Suites \| Best Luxury Hotels in Wayanad - Mesta Hotel |
| 2 | `https://mestahotel.com/rooms.php` **(non-www)** | *(same page, second host)* |
| 3 | `https://www.mestahotel.com/hotel-rooms-wayanad.php` | Rooms & Suites \| Best Luxury Hotels in Wayanad - Mesta Hotel |
| 4 | `https://www.mestahotel.com/rooms-pride.php` | Best Hotels in Wayanad \| Best Budget Hotels in Wayanad |
| 5 | `https://www.mestahotel.com/luxury-balcony-rooms-wayanad.php` | Best Hotels in Wayanad \| Best Budget Hotels in Wayanad |
| 6 | `https://www.mestahotel.com/budget-friendly-rooms-wayanad.php` | Budget Hotels in Wayanad \| Budget Hotels in Sulthan Bathery |
| 7 | `https://www.mestahotel.com/family-friendly-hotels-wayanad.php` | Family Rooms In mesta Hotel \| Family Friendly Hotels In Wayanad |
| 8 | `https://www.mestahotel.com/rooms/bliss.html` | Bliss \| Best Stay in Wayanad \| best hotel rooms in wayanad |
| 9 | `https://www.mestahotel.com/rooms/grandiose-suite.html` | Grandiose Suite \| Best Stay in Sulthan Bathery \| Mesta hotel |

Two pairs here are conclusive:

- **#1 and #3 carry the identical title tag.** `rooms.php` and `hotel-rooms-wayanad.php` are the
  same page at two addresses.
- **#4 and #5 carry the identical title tag** — and the Pride Room is described elsewhere on the
  site as *"290 sq. ft., features a private balcony"*. `rooms-pride.php` and
  `luxury-balcony-rooms-wayanad.php` are near-certainly **the same room**, once under a product
  name and once under a keyword phrase.

Note the two naming conventions, which is the tell for the two generations: keyword-phrase `.php`
files in the root (`luxury-balcony-rooms-wayanad.php`) versus clean product-named `.html` files in
a subdirectory (`/rooms/bliss.html`). The `.php` set is the old site.

### 1.2 The same split across every other section

| Section | Old (`.php`) | New (`.html`) | Notes |
|---|---|---|---|
| Packages | `/packages.php`, `/wayanad-tour-packages.php` | `/offers-packages.html`, `/packages/…html` | The two `.php` URLs share an identical title |
| Restaurants | `/restaurants.php` | `/restaurants.html` | Different titles, same subject |
| Banquets | `/banquets.php` **(http://)** | `/banquets.html` | |
| Contact | `/contacts.php` **(non-www)**, `/contact-mesta-hotel-wayanad.php` | — | The two `.php` URLs share an identical title |
| About | `/about.php` **(http://)** | — | |
| Blog index | `/blog.php` | `/blog.html` | |

**Five identical-title pairs across the site.** Identical titles on distinct URLs is not a
subtle signal — it is the clearest duplicate-content evidence available without a crawl.

### 1.3 The blog has three URL patterns for the same posts

The Jubilee Restaurant post is indexed **twice**, under two different schemes:

```
https://mestahotel.com/blog-details.php?url_title=jubilee-restaurant-launches-jubery-resto-cafe-wayanad%EF%BF%BDs-bun-craze-begins
https://www.mestahotel.com/blog-details/jubilee-restaurant-launches-jubery-resto-cafe
```

And a third pattern exists for other posts:

```
https://www.mestahotel.com/blog/adventure-activities-in-wayanad.html
https://www.mestahotel.com/blog/how-to-select-the-best-stay-in-wayanad-as-per-your-budget-interests.html
```

Three schemes — `blog-details.php?url_title=`, `/blog-details/slug`, `/blog/slug.html` — for one
blog. The query-string version is the worst of the three and should not be reachable at all.

### Fix

1. **Decide the canonical generation.** The `.html` set is the better structure — clean paths,
   product names, logical subdirectories. Treat it as the destination.
2. **301-redirect every old URL to its new equivalent**, one-to-one, never to the homepage.
   Mass-redirecting to `/` is treated as a soft 404 and throws away the link equity you are trying
   to preserve.
3. **Add a self-referencing `rel="canonical"`** to every surviving page.
4. **Retire the keyword-phrase duplicates** (`luxury-balcony-rooms-wayanad.php`,
   `hotel-rooms-wayanad.php`, `budget-friendly-rooms-wayanad.php`, `wayanad-tour-packages.php`,
   `contact-mesta-hotel-wayanad.php`) into their product-named equivalents.
5. **Kill the query-string blog URLs** — redirect `blog-details.php?url_title=*` to the clean slug.
6. Submit a clean XML sitemap containing **only** canonical URLs, and re-submit in Search Console.

---

## 2. P0 — HTTPS is not enforced, and www/non-www is not consolidated

Both variants are in the index, which means both resolve:

| Problem | Evidence |
|---|---|
| Plain HTTP indexed | `http://www.mestahotel.com/about.php`, `http://www.mestahotel.com/banquets.php` |
| Non-www indexed | `https://mestahotel.com/rooms.php`, `https://mestahotel.com/contacts.php`, `https://mestahotel.com/blog-details.php?…` |

With `http`/`https` × `www`/non-`www`, **one page can exist at four addresses** before the
`.php`/`.html` duplication in §1 even applies. Combined, a single rooms page could be served at
well over a dozen URLs.

An unsecured `http://` page is also a direct trust problem on a site that takes bookings, and
browsers will mark it "Not secure".

### Fix

- Force `301` → `https://www.` at the **server level** for all four variants, in a single hop.
  Avoid redirect chains (`http://` → `https://` → `https://www.`); make it one jump.
- Add **HSTS** (`Strict-Transport-Security`) once the redirects are confirmed working.
- Set the canonical host consistently in `rel="canonical"` and in the sitemap.
- Verify **all four** property variants in Google Search Console, or use a Domain property, so you
  can see what is actually indexed under each.

---

## 3. P0/P1 — Three production defects visible in the index

### 3.1 Character-encoding corruption baked into a live URL

```
…/blog-details.php?url_title=jubilee-restaurant-launches-jubery-resto-cafe-wayanad%EF%BF%BDs-bun-craze-begins
                                                                                  ^^^^^^^^^
```

`%EF%BF%BD` is the UTF-8 encoding of **U+FFFD, the Unicode replacement character** — what you get
when a byte sequence is decoded with the wrong character set. The apostrophe in *"Wayanad's"* was
mangled at some point in the pipeline and the corrupted result was written into a permanent URL.

The same corruption appears in the recorded title — **"Jubilee Restaurant Launches Jubery Resto Caf    ..."**,
where "Café" has broken apart. The clean URL renders it correctly as
*"Wayanad's Bun Craze Begins!"*, which confirms the bug is in the **old `.php` slug generator**, not
in the source content.

**Fix:** set `UTF-8` end to end — database/table/column collation (`utf8mb4`), the PHP connection
charset, and the `Content-Type` header/meta. Strip apostrophes and non-ASCII characters during
slug generation rather than URL-encoding them. Redirect the corrupted URL to the clean one.

### 3.2 A CMS artefact is live and indexed

```
Title: Soulmate Special Honeymoon Package by mesta - Copy | mesta Hotel
URL:   /packages/romantice-getaway-signature-room-package---2-nights-3-days.html
```

Two separate problems in one page:

- **" - Copy"** in the title tag is a CMS *duplicate-this-record* artefact that reached production
  and has been indexed. It appears in search results exactly as written.
- The URL contains **`romantice`** — a misspelling of "romantic" — plus a **triple hyphen** (`---`).

Also note the URL says *romantic getaway / signature room* while the title says *Soulmate Special
Honeymoon Package*. The URL and the title describe different products, which suggests the page was
duplicated from another and only partly re-edited. **Check the body copy for leftover content from
the source package.**

**Fix:** correct the title, fix the slug to `/packages/romantic-getaway-signature-room-2n3d.html`,
301 the old URL, and audit the page body for copy that belongs to a different package.

### 3.3 The blog index has no real title

`/blog.php` is indexed as **"Welcome to mesta hotel"** — a placeholder that names neither the page
nor a search term. Its `.html` counterpart uses "Blog | mesta Hotel", which is thin but at least
accurate. Whichever survives §1 needs a real title.

---

## 4. P1 — Title tags: keyword stuffing and cannibalisation

Title *lengths* are fine — nearly all land in the 57–64 character range and will not truncate. The
problem is what is inside them.

**Almost every page targets the same head term.** Some form of *"Hotels in Wayanad"* appears in
essentially every title on the site:

| Page | Title | Problem |
|---|---|---|
| Gallery | Gallery \| 4 star Hotels in Wayanad \| Luxury hotels in Wayanad | Two near-identical head terms stacked on a *gallery* page |
| `/4-star-hotels-in-wayanad.html` | Best Wayanad Hotels \| 4-star Hotels In Wayanad \| Mesta Hotels | Three variants of one term; competes head-on with the homepage |
| Facilities | Facilities at mesta Hotel \| Couple friendly hotels in Wayanad | "Couple friendly" is unrelated to facilities |
| Restaurants | Restaurants in Our Four-star Hotel \| 4 star Hotels in Wayanad | Should target *dining*, not *hotels* |
| `/rooms-pride.php` | Best Hotels in Wayanad \| **Best Budget Hotels** in Wayanad | See below |

Two consequences:

**Cannibalisation.** When ten pages target *"hotels in Wayanad"*, Google picks one and it may not
be the one you want. `/4-star-hotels-in-wayanad.html` is a keyword-targeted landing page competing
directly against the homepage for the term the homepage should own.

**A positioning contradiction.** The Pride Room — a 290 sq ft room with a private balcony, on a
property marketed throughout as *four-star premium* — is titled **"Best Budget Hotels in Wayanad"**.
The site simultaneously sells itself as luxury and as budget, and the budget framing sits on one of
the better rooms. Whatever the intent, this undercuts rate positioning in the SERP, which is where
the guest forms their first price expectation.

### Fix

Give each page **one** primary intent, and let the brand carry the location:

| Page | Suggested title |
|---|---|
| Home | Mesta Hotel Wayanad \| 4-Star Hotel in Sulthan Bathery |
| Rooms index | Rooms & Suites \| Mesta Hotel, Sulthan Bathery |
| Bliss | Bliss Room — 200 sq ft \| Mesta Hotel Wayanad |
| Pride | Pride Room — 290 sq ft with Private Balcony \| Mesta Hotel |
| Grandiose | Grandiose Suite — 450 sq ft \| Mesta Hotel Wayanad |
| Opus Family | Opus Family Room — Sleeps 5 \| Mesta Hotel Wayanad |
| Restaurants | Montana & Jubilee Restaurants \| Dining at Mesta Hotel |
| Banquets | Prados Banquet Hall — 100 Guests \| Events in Sulthan Bathery |
| Facilities | Pool, Gym & Facilities \| Mesta Hotel Wayanad |
| Packages | Wayanad Stay & Tour Packages \| Mesta Hotel |
| Gallery | Photo Gallery \| Mesta Hotel Wayanad |
| Contact | Contact & Directions \| Mesta Hotel, Sulthan Bathery |

Concrete specifics — *290 sq ft*, *private balcony*, *sleeps 5*, *100 guests* — earn clicks that
repeated head terms do not, and they differentiate the room pages from one another, which is
exactly what stops them cannibalising each other.

**Also fix brand casing.** The index currently holds *"mesta Hotel"*, *"Mesta Hotel"*,
*"mesta HOTEL"*, and *"Mesta Hotels"* (plural). Pick one written form and apply it everywhere. This
matters for brand-entity consolidation, not just tidiness.

---

## 5. P1 — NAP consistency

Two different contact emails are published across the site:

- `info@mestahotel.com`
- `reservation@mestahotel.com`

And four phone numbers appear in various combinations: `+91 9526 50 33 44`, `+91 9526 40 33 44`,
`+91 9526 00 22 44`, `+91 4936 22 55 55 / 22 20 08`.

Name/Address/Phone consistency is a direct local-ranking factor. Having several numbers is fine —
a hotel legitimately has a reservations line and a reception line — but **the same primary number
and email must appear identically on every page, in the schema markup, and in the Google Business
Profile.** Pick one primary pair; treat the rest as secondary and format them consistently
(`+91 95265 03344`, not `+91 9526 50 33 44`).

---

## 6. P1 — Structured data (could not be verified; near-certainly a gap)

I could not read the pages, so I cannot confirm what markup exists. But for a hotel this is the
highest-leverage item after the duplication fix, so it is listed regardless — **verify first**.

Required:

- **`Hotel`** schema on the homepage — `name`, `address` (full `PostalAddress`), `geo`,
  `telephone`, `email`, `starRating` (4), `priceRange`, `checkinTime`/`checkoutTime`,
  `amenityFeature` (pool, Wi-Fi, restaurant, banquet, parking), `image`.
- **`HotelRoom`** on each room page — `occupancy`, `floorSize` (the sq ft figures are already
  written), `bed`, `amenityFeature`.
- **`Restaurant`** for Montana and Jubilee — `openingHours` (Montana buffet 08:00–10:30, Jubilee
  08:00–22:30 are already published as prose), `servesCuisine`.
- **`BreadcrumbList`** sitewide.
- **`FAQPage`** where genuine Q&A exists.
- **`Article`** on blog posts, with `datePublished` and `author`.

Do **not** self-serve `AggregateRating` — Google ignores self-declared review scores for the
business itself, and it can trigger a manual action. Reviews live on the TripAdvisor/Google
listings.

---

## 7. Still to verify on-page

I could not fetch the site, so none of the following was checked. Each line includes how to check it.

| # | Item | How to check |
|---|---|---|
| 1 | `robots.txt` | Load `/robots.txt` — confirm it is not blocking crawl, and that it declares the sitemap |
| 2 | XML sitemap | Load `/sitemap.xml` — confirm it exists, lists **only** canonical URLs, and contains no `.php` duplicates |
| 3 | Canonical tags | View source on any room page — is there a `rel="canonical"`, and does it self-reference? |
| 4 | Redirects | `curl -I http://mestahotel.com/about.php` — confirm a **single** 301 to `https://www.…` |
| 5 | H1 tags | One `<h1>` per page, matching page intent — the title problems in §4 usually repeat in H1s |
| 6 | Meta descriptions | Present, unique, 140–160 chars, with a call to action; duplicate titles usually mean duplicate descriptions |
| 7 | Core Web Vitals | PageSpeed Insights on mobile — hotel sites are typically LCP-bound on hero imagery |
| 8 | Image optimisation | Alt text on room and gallery images; WebP; lazy-loading below the fold |
| 9 | Mobile rendering | Most Wayanad hotel search is mobile — check tap targets and the booking flow |
| 10 | Internal linking | Do the `.html` pages link to `.php` pages? If so the old generation is being actively fed |
| 11 | Booking engine | If it sits on a subdomain or third-party host, check it is `noindex` and not competing |
| 12 | Orphan `.php` pages | Crawl with Screaming Frog to find old pages nothing links to but Google still has |
| 13 | Package page bodies | Per §3.2 — check for content copied from another package and not re-edited |
| 14 | Thin content | The two blog posts found are real articles; check whether the room pages have enough unique copy to differentiate |

---

## 8. Recommended order of work

**Phase 1 — stop the bleeding (week 1)**

1. Force HTTPS + `www` at server level, single-hop 301s (§2).
2. Map every old `.php` URL to its `.html` equivalent and 301 one-to-one (§1).
3. Add self-referencing canonicals sitewide (§1).
4. Fix the " - Copy" title and the `romantice` slug (§3.2).
5. Fix the `%EF%BF%BD` blog URL and the underlying UTF-8 config (§3.1).
6. Publish a clean sitemap; submit in Search Console.

**Phase 2 — consolidate (weeks 2–3)**

7. Rewrite all titles per §4; fix brand casing.
8. Retire or merge the keyword-phrase duplicate pages.
9. Resolve the "budget vs 4-star" positioning conflict.
10. Standardise NAP sitewide (§5).

**Phase 3 — build (weeks 4+)**

11. Add `Hotel` / `HotelRoom` / `Restaurant` schema (§6).
12. Work through the §7 verification list and fix what it surfaces.
13. Core Web Vitals and image optimisation.
14. Resume blog publishing on the single surviving URL pattern.

Phase 1 is the one that matters. Phases 2 and 3 are ordinary optimisation and will underperform
badly if run before the duplicate site is collapsed — you would be optimising pages that are
competing with their own copies.

---

## Appendix — full indexed URL inventory

26 distinct URLs observed in the search index, covering ~10 unique subjects.

```
https://www.mestahotel.com/
https://www.mestahotel.com/rooms.php
https://mestahotel.com/rooms.php
https://www.mestahotel.com/hotel-rooms-wayanad.php
https://www.mestahotel.com/rooms-pride.php
https://www.mestahotel.com/luxury-balcony-rooms-wayanad.php
https://www.mestahotel.com/budget-friendly-rooms-wayanad.php
https://www.mestahotel.com/family-friendly-hotels-wayanad.php
https://www.mestahotel.com/rooms/bliss.html
https://www.mestahotel.com/rooms/grandiose-suite.html
https://www.mestahotel.com/packages.php
https://www.mestahotel.com/wayanad-tour-packages.php
https://www.mestahotel.com/offers-packages.html
https://www.mestahotel.com/packages/romantice-getaway-signature-room-package---2-nights-3-days.html
https://www.mestahotel.com/restaurants.php
https://www.mestahotel.com/restaurants.html
http://www.mestahotel.com/banquets.php
https://www.mestahotel.com/banquets.html
https://mestahotel.com/contacts.php
https://www.mestahotel.com/contact-mesta-hotel-wayanad.php
http://www.mestahotel.com/about.php
https://www.mestahotel.com/facilities.html
https://www.mestahotel.com/gallery.html
https://www.mestahotel.com/4-star-hotels-in-wayanad.html
https://www.mestahotel.com/blog.php
https://www.mestahotel.com/blog.html
https://mestahotel.com/blog-details.php?url_title=jubilee-restaurant-launches-jubery-resto-cafe-wayanad%EF%BF%BDs-bun-craze-begins
https://www.mestahotel.com/blog-details/jubilee-restaurant-launches-jubery-resto-cafe
https://www.mestahotel.com/blog/adventure-activities-in-wayanad.html
https://www.mestahotel.com/blog/how-to-select-the-best-stay-in-wayanad-as-per-your-budget-interests.html
```

This is what the index exposed, not necessarily the complete site — a full crawl will likely find
more `.php` orphans.
