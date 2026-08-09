# Correction: Exact-Only Cannot Run the Test (2026-08-09)

## The error

The plan in `search-terms-findings.md` §9 — *"₹120/day at ₹8–9 CPC → 150 clicks in 10–11
days"* — **does not survive the impression math.** Switching Auto off was endorsed without
checking whether Exact alone could deliver the volume. It cannot.

| Setup | Impressions/day | Time to 150 clicks @1.5% CTR |
| --- | --- | --- |
| Exact only (current) | ~6 | **never** |
| 50/day | 0.75 clicks/day | 200 days |
| 150/day | 2.25 clicks/day | 67 days |
| Auto running (before) | ~454 | 22 days |

Exact match on long-tail terms is inherently low-volume. **The ₹120/day budget will never be
spent — volume is the binding constraint, not money.**

## The fix

**Turn Auto back on**, with the waste cut rather than the campaign:

- Negative **product** target `B0FYY8TVNY` (own cardamom listing)
- **Substitutes** targeting group off
- Negative **phrase**: `mdh`, `elaichi`
- Negative **exact**: `spices`, `garam masala` (phrase would destroy on-target traffic)

Keep Exact running alongside at its controlled bids. Auto supplies volume and discovery; Exact
holds the price down on proven terms.

## Nothing has been tested since the listing changes

Title, bullets, images and a 5% price cut all landed — followed by roughly **one impression**.
The listing changes have not failed; they have not been measured.

Second-order problem: **five variables changed at once with no traffic.** Even once traffic
arrives, attribution across those changes is impossible. From here: stop changing the listing,
start measuring it.

## Is it reviews? Leading suspect — but price is ruled out

**Price is not the barrier, and there is direct evidence.**

Amazon displays price in the search results grid, so shoppers see ₹199 *before* clicking. CTR
runs 1.10–1.57% against a 0.3–0.5% benchmark — roughly **3x**. Shoppers see the price and click
anyway, at an above-average rate.

The loss occurs *after* the click. Price is identical on both sides of that click. What changes
is what the detail page shows: **3 reviews, no A+ content.**

Reviews are the leading suspect. Still a suspect, not a verdict — confirmation needs traffic.

## Do not discount further

| Price | Margin | Affordable CPC @8% conv |
| --- | --- | --- |
| ₹199 | ₹62 | ₹4.96 |
| ₹189 (current) | ₹53 | ₹4.21 |
| ₹175 | ₹40 | ₹3.16 |
| ₹150 | ₹16 | **₹1.28** |

Actual CPC paid: **₹8–13.** Every rupee off price drags the ceiling further below what is already
being paid — worsening a confirmed problem to address an unconfirmed one.

Nor is price winnable: at ₹150 the pack is still >2x an Everest or MDH packet, and national
brands hold scale advantages that cannot be out-discounted. The proposition is hand-weighed,
expert ratio, Kerala origin. **Prove the premium; do not abandon it.**

A coupon is the better instrument *if* discounting ever happens — reversible, leaves list price
intact — but it mainly buys CTR, which is not where this listing is losing.

## What actually moves it

1. **Brand Registry** — the unlock. Requires a registered trademark. **Open question: does
   Spiceto have one?** With it: Vine (up to 30 genuine reviews with no sales required) plus A+
   content. Without it, the loop holds — orders needed for reviews, reviews needed for orders.
2. **Request a Review** button in Seller Central on every order. Free, immediate, compliant.
3. **Check delivery time** to the metro cities is inside a week. Slow delivery suppresses
   conversion on impulse grocery purchases.
