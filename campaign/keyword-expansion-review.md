# Review — "Final Master Keyword List" Expansion (2026-08-10)

Reviewed a 35-keyword expansion plan (9 live + 26 new, across 6 tiers) built on the "garam
masala leads" finding this project already confirmed independently. **The keyword selection is
sound. The bid guidance is not — most of it reverts to Amazon's suggested-bid logic, which this
project rejected weeks ago.**

## Headline finding: 13 of 29 proposed bids exceed the affordable ceiling

This project established, from the seller's own margin math (contribution margin × conversion
rate, at ₹199 and ₹70–100 COGS): **affordable CPC is ₹4–9.**

| COGS | Margin | Ceiling @8% conv | Ceiling @5% conv |
| --- | --- | --- | --- |
| ₹70 | ₹77 | ₹6.16 | ₹3.85 |
| ₹85 | ₹62 | ₹4.96 | ₹3.10 |
| ₹100 | ₹47 | ₹3.76 | ₹2.35 |

The new list proposes ₹14–16 for its top "Tier 0" keywords. Break-even at ₹15 CPC needs
**19–32% conversion** depending on COGS. The highest conversion share found anywhere in this
project's Brand Analytics data was JK's 28.57% — on one query, one week, for a **different
seller's listing**. Not a rate to plan a launch bid around.

## The clearest instance: a live keyword already priced at the ceiling on purpose

`sabut garam masala` is live at **₹9.43** — set there deliberately (`search-terms-findings.md`:
"floor sits at the ceiling edge"). This list proposes raising it to **₹13–14**. That is not a
refinement; it is the list reverting to "bid what Amazon suggests to win," the exact logic
`sp-optimisation-plan.md` rejected as costing money the product can't carry.

## Recommendation

**Cap every bid in this list at ₹8–9, regardless of tier.** Use the list for *which* keywords to
add — that reasoning is genuinely good and builds correctly on the Brand Analytics work — not
for what to pay.

## Two more issues, before applying anything

### `garam masala` (Tier 5, ₹6–8) repeats a mistake already fixed

This is the exact commodity term already identified as wrong-buyer traffic and negatived at
account level (`search-terms-findings.md`: ₹17.27 spent, zero result, "commodity head term").
The new doc's own note — "high risk of irrelevant (powder) clicks" — confirms the earlier
finding still applies. **Skip.**

### Word-order duplicates will compete with each other

Amazon treats word order as a close variant on exact match, so keeping both members of a pair
means occasionally paying the pricier twin's bid for a query the cheaper one would have caught
— the same issue flagged earlier in this project for `khada garam masala mix` /
`mix khada garam masala`.

| Pair | Keep |
| --- | --- |
| `khada garam masala` vs `garam masala khada` | first only |
| `garam masala whole mix` vs `whole mix garam masala` | first only |
| `sabut khada masala` vs already-live `khada masala sabut` | leave live one, drop new |
| proposed `garam masala sabut` vs already-live `sabut garam masala` | leave live one, drop new |

### Tier 3 regional terms have no evidence base

Every other tier cites a rank number or a captured click/conversion share from this project's
own data. Tier 3 (Lucknowi, Punjabi, Kashmiri, Mughlai, North Indian garam masala) cites
neither — no rank, no Brand Analytics row, no autocomplete suggestion anywhere collected so far.
It's a hypothesis, not a finding, unlike the rest of the list. Fine to explore, but as a small
separate test (1–2 terms, ₹8 cap) rather than folded in as equally proven.

## Curated add list — same selection, ceiling-capped, duplicates removed

**Add at ₹8–9:**
```
garam masala whole mix
garam masala whole
whole garam masala
khada garam masala
premium garam masala whole
hand weighed garam masala
garam masala 12 spices
garam masala for biryani
khada garam masala mix
biryani garam masala whole spices
garam masala whole pack
```

**Already live, leave as is:** `khada masala sabut`, `khada masala mix`, `whole spice garam
masala`, `sabut garam masala` (stays at ₹9.43, not ₹13–14).

**Drop:** `whole mix garam masala`, `garam masala khada`, `sabut khada masala`,
`garam masala sabut`, standalone `garam masala`.

**Small separate test only, ₹8 cap:** 1–2 of the five Tier 3 regional terms, seller's choice.

## Pause list — agree with the source doc's calls

| Keyword | Action |
| --- | --- |
| `masala whole spices` | Lower to ₹8 |
| `biryani masala whole spices` | Lower to ₹7 or pause |
| `whole spices biryani` | Pause |
| `biryani whole spices`, `biryani spices` | Keep as is — best performers, don't touch |

---

## Correction (2026-08-10): word order is NOT a close variant on Exact match

Earlier reviews in this project (here, and in `search-terms-findings.md`) claimed word-order
pairs like `khada garam masala mix` / `mix khada garam masala` would compete with each other on
Exact match, since Amazon "treats word order as a close variant." **That claim is wrong.**

Amazon's actual close-variant rules for Exact match cover plurals/singulars, common
misspellings, abbreviations and accents — **not word order.** `garam masala sabut` and
`sabut garam masala` are two fully independent keywords; each fires only on its own literal
sequence and neither competes with the other for the same auction.

The live account data confirms this directly: `khada masala sabut` shows 6 impressions and
`sabut garam masala` shows 7 — independent, uncorrelated numbers, consistent with genuinely
distinct targets rather than one cannibalising the other.

**Practical effect: word-order pairs do not need to be pruned.** The earlier advice to "keep
only one member of each pair" no longer applies on Exact match. (It may still apply to Phrase or
Broad match, where Amazon's matching is looser — not verified either way in this project.)

## Live Exact campaign as of 10 Aug 2026 — 9 keywords, avg bid ₹9.11

| Keyword | Bid | Amazon suggested |
| --- | --- | --- |
| biryani spices whole | ₹8.00 | ₹16.34 (₹12.26–20.43) |
| garam masala | ₹10.00 | ₹13.38 (₹8.62–16.73) |
| garam masala sabut | ₹9.00 | ₹13.42 (₹6.97–17.15) |
| garam masala whole | ₹10.00 | ₹49.61 (₹42.76–59.66) |
| garam masala whole mix | ₹9.00 | ₹36.42 (₹30.14–47.67) |
| khada garam masala | ₹9.00 | ₹13.37 (₹11.38–17.30) |
| khada masala sabut | ₹8.00 | ₹10.75 (₹7.81–14.56) |
| sabut garam masala | ₹10.00 | ₹13.42 (₹9.03–17.44) |
| whole garam masala | ₹9.00 | ₹11.78 (₹8.83–14.73) |

All bids sit in ₹8–10 — close to the established ₹4–9 ceiling, a large improvement on the
earlier ₹14–16 proposal.

### Two open items

**`biryani whole spices` and `biryani spices` are both absent from this set.** Unlike the
word-order question above, this is not a mechanics correction — it is the account's only actual
Spiceto-specific proof of performance. `biryani whole spices` was rank #1 by impression share in
this account (24.64%), live at ₹6.95, before being dropped. `biryani spices` was live and
delivering at ₹7.61. Recommend re-adding both rather than running on an entirely unproven set.

**`garam masala` standalone is live at ₹10** — inside Amazon's own suggested range, i.e. priced
to actually win volume on the highest-volume, least-relevant term in the set (rank ~9,654). This
is the same commodity term that cost ₹17.27 for zero result before being negatived once already
(`search-terms-findings.md`). Recommend cutting to ₹6–7 if kept at all, and watching closely.
