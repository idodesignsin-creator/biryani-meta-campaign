# Structured Data (Schema.org) for Mesta Hotel

Ready-to-deploy JSON-LD for https://www.mestahotel.com/

**Built:** 14 August 2026
**Related:** [`../seo-audit-mestahotel.md`](../seo-audit-mestahotel.md) ·
[`../mestahotel-keyword-plan.md`](../mestahotel-keyword-plan.md)

---

## Files

| File | Goes on | Type |
| --- | --- | --- |
| [`hotel.jsonld`](hotel.jsonld) | Homepage only | `Hotel` |
| [`restaurants.jsonld`](restaurants.jsonld) | `/restaurants.php` | `Restaurant` ×2 |
| [`banquet.jsonld`](banquet.jsonld) | `/banquets.php` | `EventVenue` |
| [`breadcrumb-and-blog.jsonld`](breadcrumb-and-blog.jsonld) | Inner pages / blog posts | `BreadcrumbList`, `BlogPosting` |

## How to install

Paste each block inside a `<script>` tag in the `<head>` (or anywhere in `<body>` —
Google accepts both):

```html
<script type="application/ld+json">
{ ... contents of hotel.jsonld ... }
</script>
```

**One `Hotel` block, on the homepage only.** Do not repeat it on every page. Inner
pages reference it by its `@id` (`https://www.mestahotel.com/#hotel`), which is why
that ID appears in the restaurant and banquet files — it tells Google these are all
the same business.

---

## ⚠️ Before you deploy — two things that can earn a penalty

### 1. I deliberately left out `aggregateRating`

You have review scores — Tripadvisor 4.0 from 428 reviews, Goibibo 4.2 from 638. It
is tempting to mark those up. **Don't.**

Google's structured-data policy prohibits marking up reviews collected on third-party
platforms as if they were your own `aggregateRating`. Doing it is a common cause of
manual actions for spammy structured data, and the penalty applies sitewide, not just
to the offending page.

`aggregateRating` is legitimate **only** when the reviews are collected by you, shown
on the page, and visible to the visitor. If you want star ratings in search results,
build a real on-site review capture first, then add:

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.3",
  "reviewCount": "127",
  "bestRating": "5"
}
```

The Tripadvisor and Goibibo URLs *are* included — in `sameAs`, which is the correct
and safe way to associate your entity with those profiles.

### 2. `starRating: 4` needs to be true

The schema claims 4 stars. Your site says 4-star; **Tripadvisor lists you as a B&B /
inn**, which is the category mismatch flagged in the audit. If the 4-star rating is
not an official classification, either remove `starRating` or replace it with the
rating you can actually substantiate. A contested star rating in structured data is a
bad thing to be caught on.

### A note on FAQ markup

I have not included `FAQPage`. Google restricted FAQ rich results in August 2023 to
authoritative government and health sites — for a hotel it no longer produces a
visible rich result. It still helps AI assistants and LLM-driven search parse your
content, so it is not worthless, just not the win it once was. Add it if you want the
AI-visibility benefit; don't expect SERP real estate.

---

## Placeholders you must replace

Every one of these is marked `REPLACE_ME` in the files. **The schema will validate but
mislead if you deploy it unchanged** — I had no access to the live site, so anything I
could not verify is a placeholder rather than a guess.

| Field | File | Where to get it |
| --- | --- | --- |
| `latitude` / `longitude` | hotel, banquet | Google Maps → right-click the property → click the coordinates to copy |
| `hasMap` | hotel | Google Maps → Share → Copy link |
| `priceRange` | hotel, restaurants | Use `₹₹`–`₹₹₹₹` symbols, or a real range like `"₹3000-₹8000"` |
| `numberOfRooms` | hotel | Total keys in the property |
| `checkinTime` / `checkoutTime` | hotel | I defaulted to 14:00 / 11:00 — **verify these** |
| `urlTemplate` (ReserveAction) | hotel | Your booking engine URL. Delete the whole `potentialAction` block if you have no online booking |
| `image` URLs | all | Real paths. Use 1200px+ wide, 16:9 / 4:3 / 1:1 |
| `logo` | hotel | Real logo path |
| `datePublished` / `dateModified` | blog | Actual post dates |
| Room page `url` values | hotel | **See the warning below** |
| `slogan`, `faxNumber`, Airport Transfer | hotel | Fill in or delete the line — don't ship empty strings |

### ⚠️ The room URLs are guesses — verify them

I used `/rooms-blossom.php`, `/rooms-signature.php`, `/rooms-opus.php` in
`containsPlace`. **Only `/rooms-pride.php` is confirmed to exist.**

This matters more than usual here, because `/restaurants.html` is confirmed returning
a **404** while still indexed. Pointing schema at dead URLs actively signals low
quality. Check every `url` in the files resolves with a 200 before deploying.

---

## Contact details — pick one and use it everywhere

The site currently exposes two emails (`info@` and `reservation@`) and four phone
numbers. Structured data needs **one** primary of each, matching the Google Business
Profile exactly.

I used:
- **Phone:** `+919526503344` (E.164 format — no spaces, with country code)
- **Email:** `reservation@mestahotel.com`

The secondary landline is in `contactPoint` as the front desk. Change these if the
priority is different, but change them **everywhere at once** — site footer, schema,
GBP, and every OTA listing. Inconsistent NAP is the finding this is meant to fix.

---

## Validate before and after deploying

1. **[Schema Markup Validator](https://validator.schema.org/)** — catches syntax
   errors and invalid property names. Use this first.
2. **[Google Rich Results Test](https://search.google.com/test/rich-results)** — shows
   what Google will actually render.
3. **Search Console → Enhancements** — watch for errors for two weeks after deploying.

Expect Rich Results Test to report that `Hotel` is not eligible for a rich result.
**That is normal and not an error.** Google's hotel rich results run through Hotel
Center and paid booking feeds, not organic markup. The value of this schema is entity
clarity — helping Google connect the site, the Google Business Profile, and the OTA
listings into one confident understanding of the business, which is exactly what is
needed to win back the branded SERP.

---

## What this fixes

From the audit and keyword plan:

| Problem | How the schema helps |
| --- | --- |
| OTAs own the brand SERP | `sameAs` + consistent entity data strengthens Mesta as the authoritative source |
| Brand casing inconsistent across the index ("mesta Hotel", "Mesta Hotels", "mesta HOTEL") | `name` declares one canonical form |
| Banquet hall has zero keyword coverage | `EventVenue` with capacity and facilities makes it a distinct, findable entity |
| Restaurants have zero keyword coverage | Two `Restaurant` entities with hours and cuisine |
| NAP inconsistency (2 emails, 4 phones) | Forces a single authoritative pair |
| Category confusion (4-star vs B&B) | `starRating` + `Hotel` type states the intended category — *once you have confirmed it is accurate* |

Schema is a supporting fix, not a primary one. **The dead URLs and the four
host/protocol variants are still the P0 items** — markup pointing at a broken URL
structure will not rescue it.
