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

---

## Update: 11 Aug reverted to near-zero — consistent with the backlog theory

| Campaign | 10 Aug | 11 Aug |
| --- | --- | --- |
| Auto | 75 impr / 2 clicks / ₹15.82 / **3 purchases / ₹1,187.62** | 53 impr / **0 clicks** / ₹0 / 0 purchases |
| Exact | 54 impr / 0 clicks / ₹0 / 0 purchases | 61 impr / 1 click / ₹10.97 / 0 purchases |
| Kudampuli | 158 impr / 2 clicks / ₹19.47 / 0 purchases | 136 impr / 0 clicks / ₹0 / 0 purchases |

Zero clicks on 53 impressions is not itself concerning — at the account's normal 1–2.7% CTR,
a 0-click day happens 24–59% of the time by chance alone.

**But the pattern across both days together supports the backlog explanation, not a new
steady rate.** If 10 Aug's 3 purchases had marked the start of a genuine daily conversion
pattern, 11 Aug would be expected to look similar. Instead it reverted close to zero — consistent
with 10 Aug being a one-time catch-up of pre-negative-keyword clicks converting under Amazon's
attribution window, not evidence of an ongoing rate.

**Read as of 11 Aug: one strong (likely catch-up) day + one quiet day is not yet evidence of
demand in either direction.** The CTR pattern across this project has consistently run above
benchmark — real, repeated evidence of click-level interest — but a *purchase* rate needs to be
observed as a repeatable pattern, not a single day, before it means anything. Continue watching
daily for at least 5–7 more days before drawing a conclusion.
