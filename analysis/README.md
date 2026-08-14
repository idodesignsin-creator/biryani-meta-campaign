# Semantic similarity analysis — mestahotel.com

**Run:** `python3 title-similarity.py` (pure stdlib, no dependencies)
**Date:** 14 August 2026

---

## What this is, and what it is not

There is no way to "check the vector embedding" of a website. Google, OpenAI, and
Perplexity all keep their embeddings internal — no API returns "here is how our model
represents your hotel." Anyone offering to look that up is selling something.

What *can* be done, and what this script does, is build the vectors yourself and
measure how your own pages relate to each other. That answers the question that
actually matters: **do your pages occupy distinct semantic space, or are they
collapsing into each other?**

**Method:** TF-IDF cosine similarity over the 21 indexed title tags.

**Limits, stated plainly:**
- This is **lexical**, not neural. It measures rare-word overlap, not meaning. A real
  transformer embedding would know "budget hotel" ≈ "affordable stay" with zero shared
  words; TF-IDF does not.
- It runs on **title tags only** — the site was never crawled, so body content is not
  included. Full-content analysis would be more reliable.
- Therefore these numbers **understate** true semantic similarity. The real overlap is
  worse than what is shown below.

---

## Result 1 — a perfect 1.000 collision

```
1.000  /rooms-pride.php
       /luxury-balcony-rooms-wayanad.php
```

Cosine similarity of exactly 1.0 means the two vectors are **identical**. Not similar
— identical. Both pages carry the title "Best Hotels in Wayanad | Best Budget Hotels
in Wayanad", so no retrieval system, lexical or vector-based, has any basis for
telling them apart.

This is the quantified version of the finding in the audit, and it explains why
`Best Budget Hotels In Wayanad` is stuck on page 2 in the July report. Two pages,
one identity, split signal.

### Other high-similarity pairs

| Score | Pages | Problem |
| --- | --- | --- |
| **1.000** | `/rooms-pride.php` ↔ `/luxury-balcony-rooms-wayanad.php` | Identical. Retire one. |
| **0.756** | `/` ↔ `/about.php` | Homepage and About are near-interchangeable |
| **0.614** | `/4-star-hotels-in-wayanad.html` ↔ `/restaurants.html` | A restaurant page 61% identical to a hotel category page |
| 0.566 | `/4-star-hotels-in-wayanad.html` ↔ `/gallery.html` | Gallery has no identity of its own |
| 0.484 | `/about.php` ↔ `/contact-mesta-hotel-wayanad.php` | — |
| 0.422 | `/rooms-pride.php` ↔ `/restaurants.php` | Rooms vs food, still 42% overlap |

Rule of thumb: **anything above 0.60 between two pages you want ranking for different
terms is a problem.** Above 0.85 they are effectively one page.

---

## Result 2 — the money pages are the least distinctive on the site

This is the finding worth acting on, and it is the opposite of what you would want.

Distance from the site's semantic centroid — **higher means more generic**:

```
0.594  ###################  /about.php
0.538  ###################  /rooms-pride.php
0.538  ###################  /luxury-balcony-rooms-wayanad.php
0.524  ##################   /
0.489  #################    /4-star-hotels-in-wayanad.html
...
0.248  ########             /facilities.html
0.237  ########             /blog/planning-a-wayanad-trip
0.208  #######              /offers-packages.html
0.199  ######               /things-todo.php
0.161  #####                /blog/adventure-activities
```

**Every commercial page clusters at the generic end. Every blog post sits at the
distinctive end.**

The pages meant to convert — homepage, rooms, the 4-star landing page — are the ones
saying the same thing as everything else ("best hotels in Wayanad"). The blog posts,
which were never the priority, are the only content on the site with a semantic
identity of its own.

That is exactly backwards. Money pages should be the *most* distinctive things you
publish, each owning a clearly separate patch of meaning.

---

## Why this matters more in 2026 than it used to

Retrieval in AI Overviews, ChatGPT search, and Perplexity is embedding-based. That
changes the cost of duplication:

- **In classic keyword search**, two near-identical pages were merely inefficient —
  you might still rank one of them.
- **In vector retrieval, near-duplicates are actively discarded.** A retriever pulling
  the top-k most relevant chunks has no reason to return two vectors pointing the same
  direction. One gets picked; the other is dead weight.

So the keyword-stuffed title strategy — repeating "best hotels in Wayanad" across
eight pages — is not just outdated. It is **specifically counterproductive** for the
systems that are increasingly mediating hotel discovery.

Worth noting too: `/restaurants.html` returns a **404**, so it contributes nothing to
any index, vector or otherwise, while still holding a title tag in Google's results.

## What actually improves your position in embedding-based retrieval

1. **One distinct topic per page** — the fix already specified in the keyword plan.
2. **Specific, concrete facts** — "290 sq ft with a private balcony, 2 km from Sulthan
   Bathery bus stand" embeds far more usefully than "best hotels in Wayanad".
3. **Entity clarity via structured data** — the `schema/` directory in this repo.
4. **Question-shaped content** — the four keyword groups in the plan (banquet,
   landmark proximity, restaurant, seasonal) each occupy their own semantic space.
5. **Third-party corroboration** — your Tripadvisor and Goibibo presence already helps
   here; `sameAs` in the schema ties it together.

---

## Re-run this after fixing the titles

The script is the verification step. Rewrite the title tags per the keyword plan, edit
the `pages` dict in `title-similarity.py`, and re-run.

**Target:** no pair above 0.60, and the commercial pages spread *away* from the
centroid rather than clustered at it.

To do this properly on full page content rather than titles, the site needs to be
crawlable from this environment (currently blocked), or a content export provided.
