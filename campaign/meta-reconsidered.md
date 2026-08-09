# Meta Reconsidered (2026-08-09)

Prompted by a fair challenge: *"many people sell huge units per day just with a Facebook page
and reels, so your guess that people watching reels cannot buy is wrong."*

## The correction

**That criticism lands.** Earlier notes framed Meta traffic as *worse* than Amazon search. It is
not worse — it does a **different job**:

- **Amazon SP harvests** demand that already exists.
- **Meta creates** demand among people who were not looking.

And the data now argues *for* demand creation. Exact-match terms draw **~10 impressions/day** —
that is the entire harvestable pool on Amazon search for this product. No bid grows it. A reel
has no such ceiling.

"People watching reels cannot buy" was a bad line. They plainly can; that is most of Indian D2C.

## What still stands, restated properly

The brands selling volume off reels almost all sell on **their own site**, not into Amazon. The
difference is structural, not about the audience:

| | Meta → Amazon | Meta → own site |
| --- | --- | --- |
| Pixel fires | **No** | Yes |
| Optimise for purchases | **No — clicks only** | Yes |
| Know which ad sold | **No** | Yes |
| Retarget cart abandoners | **No** | Yes |
| Own the customer data | **No** | Yes |
| Bundle / upsell at checkout | **No** | Yes |

Routing Meta traffic to Amazon is the hard version. Meta never sees a sale, so its algorithm
never learns who the buyer is — and that learning is precisely what makes reels-driven D2C work.

## The real constraint is AOV, not intent

One week at ₹500/day = ₹3,500, assuming ₹9 CPLPV and 2% site conversion:

| Product | Orders | Revenue | ROAS |
| --- | --- | --- | --- |
| ₹199 single 90 g | 7.8 | ₹1,548 | **0.44** |
| ₹299 single 180 g | 7.8 | ₹2,326 | 0.66 |
| **₹599 combo** | 7.8 | ₹4,659 | **1.33** |
| ₹899 large combo | 7.8 | ₹6,992 | 2.00 |

At ₹199 a Meta test cannot pay back — not because the traffic is poor, but because ₹199 cannot
absorb a ₹9 visit at 2% conversion. Indian D2C on Meta generally needs ₹600+ orders.

**The autocomplete data already points at the fix:** `combo` appeared in 4 of 20 suggestions.
Buyers are actively searching for spice combos. Bundle 90 g + 180 g, or build a biryani set, at
₹599–899.

## Decision: run the one-week test

Three conditions, so it yields an answer rather than another ambiguous cycle:

1. **Destination is spiceto.in, not Amazon.** Meta pixel installed and firing first. This single
   change is what separates this from every previous plan.
2. **Advertise a bundle at ₹599+**, not the ₹199 single.
3. **Optimise for Add to Cart**, not Purchase. A fresh pixel will not reach the ~50 weekly
   purchases Meta needs to exit the learning phase; it will reach enough ATCs.

Creative is already produced and the ad copy is written, so the only new work is destination and
offer.

## Open input

**Is spiceto.in live and taking orders?** Shopify and WooCommerce both appear in the browser, and
the pack carries the domain — but this determines whether the test starts next week or whether
the store has to be finished first.

## What does not change

- The **Amazon listing work stands on its own** — title, ingredients fix, Vine. That is about
  organic rank and the Amazon channel, and is unaffected by whatever Meta does.
- The **Amazon draft campaign** in Ads Manager still points at the ASIN. If this test runs, it
  runs as a **new campaign pointed at spiceto.in**, not by unpausing the old one.
