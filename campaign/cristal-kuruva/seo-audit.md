# SEO Audit — crystalkuruva.com

Audit of [Crystal Kuruva Nature Resort & Spa](https://www.crystalkuruva.com/), Pakkom,
Wayanad. Supersedes parts of [`seo-comparison.md`](seo-comparison.md) — see *Corrections*
at the end.

---

## What this audit is and isn't

**I could not crawl the site.** This environment's network policy blocks
`crystalkuruva.com` (403 at the egress proxy), and Google Search Console is not connected
to Adspirer. So this is a **rankings-and-index audit**, not a technical crawl.

**What's verified here:** which queries the site does and doesn't rank for, who beats it,
indexed URL structure, and title tags as they appear in results.

**What is NOT covered and still needs checking** — every one of these requires either
browser access or Search Console:

| Unchecked | How to check |
| --- | --- |
| Meta descriptions, H1/H2 hierarchy, word counts | View source, or Screaming Frog |
| Schema markup (Hotel, LocalBusiness, FAQ, Review) | [Google Rich Results Test](https://search.google.com/test/rich-results) |
| Core Web Vitals, page speed, mobile usability | [PageSpeed Insights](https://pagespeed.web.dev/) |
| Canonical tags, robots.txt, XML sitemap | Fetch `/robots.txt` and `/sitemap.xml` directly |
| Image alt text and file sizes | View source / Lighthouse |
| Actual impressions, clicks, average position | Search Console |
| Backlink profile | Ahrefs / Semrush free tier |

**To unlock a full technical audit**, easiest first: connect Search Console in Adspirer
Settings → Connections, or paste me the homepage HTML source, or run PageSpeed Insights
and share the score.

One methodology caveat: Google rewrites title tags in results roughly half the time, and
I observed the same URLs showing **different titles across searches**. Titles below are
what Google displayed, which may not be the raw `<title>` in the HTML.

---

## Headline finding

**The site ranks for its brand and its island. It does not rank for what people actually
search when they're ready to book.**

Tested against real queries:

| Query tested | Does crystalkuruva.com rank? | Who wins instead |
| --- | --- | --- |
| "resorts near Kuruva Island Wayanad" | ✅ Yes — homepage | OTAs above it (Trivago, Booking, EaseMyTrip, Agoda, Tripadvisor) |
| "best luxury resorts in Wayanad private pool villa" | ❌ **No** | Mountain Shadows' dedicated pool-villa page; listicles from Stride, Groowynd, visit-wayanad |
| "treehouse resort Wayanad" | ❌ **No** | Vythiri Resort's dedicated treehouse page; Holidify, Iris Holidays, visit-wayanad listicles |

The resort **has** a Private Pool Villa (850 sq ft) and a Tree House (450 sq ft). It sells
both. It ranks for neither. Meanwhile its homepage title literally reads *"Luxury Resorts
in Wayanad | Pool Villa in Wayanad"* — it is **bidding for a keyword it does not rank
for, using a page not built for it.**

That's the whole audit in one sentence: **inventory exists, pages don't.**

---

## Issue 1 — No commercial landing pages (critical)

Every room type lives inside one generic `/cottages.php`: Deluxe Cottage, Premium Cottage,
Family Twin Cottage, Premium Family Duplex, Premium Villa with Tub, Tree House, Private
Pool Villa.

Competitors that outrank it did the opposite. Mountain Shadows built
`private-pool-villa-resort-wayanad-kerala.php`. Vythiri built `/stay/tree-house.html`.
Both rank. Both have keywords in the URL, the title, and presumably the H1.

**Build these pages**, priority order:

| Page | Target query | Competitive read |
| --- | --- | --- |
| `/pool-villa-resort-wayanad` | "private pool villa wayanad" | Contested — Mountain Shadows, Vythiri Village, Vistara, Indeevara all have pages. But the homepage already claims this term with nothing behind it, so this is fixing a self-inflicted gap. |
| `/resorts-near-kuruva-island` | "resorts near Kuruva Island", "Kuruvadweep stay" | **Highest relevance, lowest competition.** Already ranks with just a homepage — a dedicated page should hold position 1. |
| `/treehouse-resort-wayanad` | "treehouse resort wayanad" | Harder than I previously said — see Corrections. Vythiri, Wayanad Treehouse, Tranquil, Green Magic are established. Still worth building; expect a slower climb. |
| `/honeymoon-resorts-wayanad` | "honeymoon resorts wayanad" | High AOV, matches Ad Set C in the Meta audience plan. Currently only a blog post serves this. |
| `/family-resorts-wayanad` | "family resorts wayanad" | Two family room types already exist, buried. |

Each page needs: keyword in URL, title, and H1; 600+ words of genuine content; real photos
with descriptive alt text; a visible booking CTA; and internal links from related blog posts.

---

## Issue 2 — The "Kuruva" name collision (newly found, important)

Searching Kuruva Island accommodation surfaces **three different properties** with
near-identical names:

1. **Crystal Kuruva Nature Resort & Spa** — the client
2. **Kuruva Island Resort & Spa** (by Kabini Breeze), Mananthavady — listed on
   [Kerala Tourism's official site](https://www.keralatourism.org/resorts/kuruva-island-resort-spa/5108), Agoda, Booking
3. **Kuruva Isles – Jungle Resort** — [kuruvaisles.com](https://kuruvaisles.com/)

This is a real brand-confusion risk, and it revises the "uncontested geographic moat"
framing in the comparison doc. The moat is *strong* but **not empty**.

**What to do:**
- Always use the full name **"Crystal Kuruva"** — never "Kuruva" alone — in titles, meta
  descriptions, schema `name`, OTA listings, and ad copy.
- Get listed on **Kerala Tourism's official directory** like competitor #2 is. A
  `keralatourism.org` listing is a high-authority, government-domain citation.
- Ensure NAP (name, address, phone) is byte-identical everywhere — Google Business Profile,
  Tripadvisor, Booking, MakeMyTrip, Agoda, Trivago, EaseMyTrip.

---

## Issue 3 — OTAs outrank the site on its own terms

On the Kuruva Island query, Trivago, Booking.com, EaseMyTrip, Agoda and Tripadvisor all
appear alongside or above the resort's own homepage.

This is normal in hotel SEO and not fully fixable — but it's expensive, since every OTA
booking carries 15–25% commission where a direct booking carries none.

**Mitigations, in order of impact:**
1. **Hotel schema markup** with room types, price range, amenities and aggregate rating —
   this is what earns rich results and helps the official site stand out. (Unverified
   whether any schema exists — check first.)
2. **Google Business Profile fully populated** — photos, rooms, amenities, Q&A, posts.
   For "near me" and branded searches this outranks everything.
3. **A visible best-rate guarantee** on the site, so brand searchers who land on an OTA
   still have a reason to come direct.

---

## Issue 4 — Listicles own the category, and the site is barely in them

Every high-intent query returned aggregator listicles above any individual resort:
Holidify's "10 Best Tree Houses in Wayanad", visit-wayanad's "16 Best Resorts With Private
Pool" and "9 Handpicked Tree House Resorts", Groowynd, Stride Hotels, Iris Holidays.

Crystal Kuruva has [one visit-wayanad profile page](https://visit-wayanad.com/crystal-kuruva-nature-resort-spa/),
but did not appear in the pool-villa or treehouse listicles those same sites publish.

**Outreach to get included in those roundups is likely higher ROI than trying to outrank
them.** It's cheap, it builds backlinks, and it puts the property in front of exactly the
comparison-stage traveller. Start with visit-wayanad (already has a relationship),
Holidify, Groowynd, Iris Holidays.

---

## Issue 5 — Technical hygiene

Ordered by effort-to-impact:

1. **Broken title tag.** `/blogs/explore-the-natural-charm-of-kuruva-island` shows
   `Crystalkuruva` — a bare fallback with no keywords, on a post about the resort's most
   valuable geographic asset.
2. **Duplicate blog URLs.** `/blog-details.php?id=7` and `/blogs/{slug}` both serve blog
   content and both are indexed — a half-finished migration. 301-redirect the legacy
   pattern and set canonicals.
3. **Both www and non-www indexed.** Pick one, 301 the other, set the canonical host.
4. **Homepage title has no brand name.** Brand searches convert best; the homepage should
   compete for them. Suggested: `Crystal Kuruva | Luxury Pool Villas & Treehouses near Kuruva Island, Wayanad`
   — though at 76 characters that will truncate, so trim to ~60:
   `Crystal Kuruva | Luxury Resort near Kuruva Island, Wayanad` (58).
5. **`/contacts.php` is keyword-stuffed.** It showed the title *"Best 5 Star Resort with
   Pool Villas & Tree Houses in Wayanad"* — no mention of contact. Someone searching
   "crystal kuruva contact number" sees nothing matching their intent. Make it
   `Contact Crystal Kuruva | Bookings & Directions, Wayanad`.

---

## Strength worth protecting: the blog

At least 9 indexed posts on clean, descriptive slugs. **Mountain Shadows has no blog at
all.** This is the site's clearest structural advantage.

Its weakness right now is that blog authority has nowhere to flow — the commercial pages
those posts should link into don't exist yet. Build the pages in Issue 1, then link every
relevant post into them. The romantic-escapes post → honeymoon page. Both Kuruva Island
posts → the Kuruva Island page. The village-life and forest-stay posts → the relevant
room pages.

---

## Priority order

**Week 1 (hours of work, immediate):** fix the broken blog title; fix `/contacts.php`;
rewrite the homepage title with the brand in it; set canonical host; 301 the legacy blog URLs.

**Weeks 2–4 (highest ROI):** build `/resorts-near-kuruva-island` and
`/pool-villa-resort-wayanad`; add Hotel schema; complete Google Business Profile.

**Month 2:** treehouse, honeymoon and family pages; internal links from blog to commercial
pages; listicle outreach; pursue the Kerala Tourism directory listing.

**Ongoing:** keep publishing blog content — the main competitor isn't contesting it.

---

## Corrections to `seo-comparison.md`

Two claims in the earlier doc were wrong or overstated, now that ranking data exists:

1. **"Treehouse is uncontested"** — wrong as written. It's uncontested *versus Mountain
   Shadows*, but Vythiri Resort, Wayanad Treehouse, Tranquil Resort and Green Magic all
   compete, and Vythiri has a dedicated ranking page. Still worth building; not the easy
   win I described.
2. **"Kuruva Island is a geographic moat"** — overstated. Two similarly-named properties
   compete for the same term, one of them listed on Kerala Tourism's official site. The
   moat is strong but requires actively defending the *Crystal* half of the name.

---

## Sources

- [crystalkuruva.com](https://www.crystalkuruva.com/) · [Mountain Shadows](https://www.mountainshadows.in/private-pool-villa-resort-wayanad-kerala.php) · [Vythiri treehouse page](https://www.vythiriresort.com/stay/tree-house.html)
- [Kuruva Island Resort & Spa on Kerala Tourism](https://www.keralatourism.org/resorts/kuruva-island-resort-spa/5108) · [Kuruva Isles](https://kuruvaisles.com/)
- [Crystal Kuruva on visit-wayanad](https://visit-wayanad.com/crystal-kuruva-nature-resort-spa/) · [on Tripadvisor](https://www.tripadvisor.com/Hotel_Review-g21046163-d25272746-Reviews-Crystal_Kuruva_Nature_Resort_Spa-Pakkom_Wayanad_District_Kerala.html) · [on Booking.com](https://www.booking.com/hotel/in/crystal-kuruva-nature-resort-amp-spa.html)
- [visit-wayanad treehouse listicle](https://visit-wayanad.com/tree-house-resorts-in-wayanad/) · [Holidify treehouse listicle](https://www.holidify.com/hotel-collections/tree-houses-in-wayanad)
