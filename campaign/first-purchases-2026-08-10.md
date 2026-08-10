# First Real Purchases (2026-08-10)

After weeks of zero everywhere, the account shows its first genuine conversion signal.

## Account totals, 10 Aug 2026

287 impressions, 4 clicks, ₹35.29 spend, CPC ₹8.82, **3 purchases, ₹1,187.62 sales**.

| Campaign | Impr | Clicks | Cost | Purchases | Sales |
| --- | --- | --- | --- | --- | --- |
| Auto | 75 | 2 | ₹15.82 | **3** | **₹1,187.62** |
| Exact | 54 | 0 | ₹0.00 | 0 | ₹0.00 |
| Kudampuli | 158 | 2 | ₹19.47 | 0 | ₹0.00 |

Internal consistency check passes: CTR (2/75 = 2.67%) and CPC (₹15.82/2 = ₹7.91) both match
the displayed figures exactly — the Impressions/Clicks/Cost numbers are a genuine, consistent
snapshot.

## Why 3 purchases against only 2 clicks is not an error

Amazon's summary view attributes **Purchases and Sales by order date**, while **Clicks and
Cost are attributed by click/event date** — the "traffic date-based conversion attribution"
link on the campaign manager screen points at exactly this distinction. Sponsored Products
carries up to a 14-day attribution window.

Auto was running ~454 impressions/day just days before this, prior to the negative keywords
and bid fixes being applied (see `autocomplete-findings.md`, `search-terms-findings.md`). Those
older clicks are the far more likely source of today's purchases — a backlog converting now,
not today's 2 clicks alone.

## Average order value is worth checking

₹1,187.62 ÷ 3 = **₹395.87 average order value** — roughly 2x the 90 g pack's ₹199. Consistent
with the 180 g pack (₹299), multi-unit orders, or a mix. **Check the Orders report** for the
exact SKU and quantity — that identifies which pack size is actually converting.

## ROAS — promising, not yet a settled rate

₹1,187.62 sales against ₹15.82 Auto spend is 75x; against the full ₹35.29 account spend, 34x.
Striking numbers, but drawn from **3 purchases** — treat as an early positive signal, not a
conversion rate to plan around yet.

## What stays the same

- **Exact remains flat** — 54 impressions, 0 clicks, ₹0 spent. Consistent with the pattern
  established throughout this project; Exact was never expected to carry volume.
- **Auto is confirmed as both the volume and the conversion engine**, exactly as argued when
  Auto vs. Exact-only was first compared in `volume-correction.md`.

## Recommended next step

**Don't touch anything.** Let Auto continue running as configured and watch whether purchases
keep accumulating over the next few days. That is what turns one promising data point into an
actual, trustworthy conversion rate.
