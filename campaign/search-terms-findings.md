# Auto Campaign — Search Terms Findings (2026-08-08)

Report window 4 Jun – 8 Aug 2026 (Amazon caps the lookback at 65 days; the campaign started
3 Aug, so effectively all spend is 3–8 Aug). **20 terms, ₹576.94, zero purchases.**

19 of 20 terms captured (₹555.86 of ₹576.94); one row ~₹21.08 remains cut off.

## All terms

| Search term | Cost | Read |
| --- | --- | --- |
| `biryani spices` | ₹135.82 | On target — **23.5% of total spend** |
| `khada masala sabut` | ₹60.79 | On target — **2nd biggest term, Hindi** |
| `biryani whole spices` | ₹40.19 | On target |
| `sabut garam masala` | ₹38.25 | On target — Hindi |
| `12 masala 13 saman dev hotel jaipur` | ₹29.55 | **Waste** — junk / competitor brand |
| `Spiceto Idukki Green Cardamom` (B0FYY8TVNY) | ₹26.36 | **Waste — own product** |
| `khada masala mix` | ₹22.15 | On target — Hindi |
| `whole biryani masala spices` | ₹21.92 | On target |
| `masala whole spices` | ₹21.50 | On target |
| `biryani spices whole` | ₹21.14 | On target |
| `mdh garam masala` | ₹20.22 | **Waste** — competitor brand conquest |
| `whole spices biryani` | ₹19.55 | On target |
| `spices` | ₹19.42 | **Waste** — too generic |
| `biryani masala whole spices` | ₹18.45 | On target |
| `garam masala` | ₹17.27 | **Waste** — commodity head term |
| `badi elaichi` | ₹15.19 | **Waste** — single spice, wrong buyer |
| `garam masala spices whole` | ₹15.17 | On target |
| `sabut masala` | ₹10.88 | On target — Hindi |
| `spiceto` | ₹2.04 | Brand search, no purchase |

| Category | Spend | Share |
| --- | --- | --- |
| **On target** | **₹425.81** | **74%** |
| Waste | ₹128.01 | 22% |
| Brand | ₹2.04 | 0.4% |

## 1. Self-targeting — paying to advertise on your own listing

`Spiceto Idukki Green Cardamom Whole, 100g` (**B0FYY8TVNY**) is the seller's own ASIN, matched
as a *Substitute*. The biryani ad is being served on the cardamom detail page, at cost, to
people already on a Spiceto product.

**Add B0FYY8TVNY as a negative product target.**

## 2. The Substitutes group holds the waste

₹55.91 of visible spend, **zero sales**, and both clearly wasteful terms come from it. Auto
allows per-group bidding — **turn Substitutes off or cut its bid hard.**

`badi elaichi` (Close match) is a separate symptom: someone searching black cardamom wants one
spice, not a twelve-spice mix. Auto is matching too loosely.

## 3. Targeting is correct — 74% of spend

The working hypothesis was that the Auto clicks went to irrelevant queries. **They did not.**
₹425.81 went to people typing what the product literally is. This was never a targeting problem.

With 100% buy box, above-benchmark CTR and now confirmed-correct queries, the chain reads:
**right search → good ad → click → land on page → leave.** That points at the detail page.

## 4. Buyers search in Hindi — and the title dropped the Hindi term

| Term | Spend |
| --- | --- |
| `khada masala sabut` | ₹60.79 — 2nd biggest term overall |
| `sabut garam masala` | ₹38.25 |
| `khada masala mix` | ₹22.15 |
| `sabut masala` | ₹10.88 |
| **Total** | **₹132.07 — 23% of all spend** |

Nearly a quarter of traffic comes from vernacular whole-spice searches — and the reported
listing title **dropped "khada garam masala"**. Highest-intent buyers search *khada* and
*sabut* while the listing no longer carries the term organically. That is a ranking loss on
exactly the queries generating the paid traffic, and it makes restoring the title more urgent
than first assessed.

**It also shows the Exact keyword list was built on guesses.** Exact contains
`khada garam masala` (1 impression) but not `khada masala sabut` — the ₹60.79 term Auto found.
Auto did its job; the hand-written list did not.

## 5. Two more waste items, and one cheap opportunity

- **`mdh garam masala` ₹20.22** — conquesting a national brand. A shopper seeking MDH at ~₹70
  finds a ₹199 pack. Unwinnable comparison. Negative it.
- **`spices` ₹19.42** — far too generic to carry intent.
- **`spiceto` ₹2.04, no purchase.** One click, so nothing conclusive — but note the price. It is
  the *only* traffic in this report under the ₹4–9 affordable ceiling. A small defensive brand
  campaign is cheap and blocks competitors bidding on the name.

## 6. Where the evidence stands

26 clicks on precisely-correct terms, zero sales.

| True conversion | P(0 sales in 26 clicks) | |
| --- | --- | --- |
| 10% | 6.5% | **now unlikely** |
| 8% | 11.5% | plausible |
| 5% | 26% | plausible |
| 3% | 45% | plausible |

A healthy 10% listing is effectively ruled out. **5% remains plausible, so this still does not
convict the listing** — the Business Report's 3.4% ceiling is the tighter bound. The picture is
consistent and pointing one way; it is not yet proof.

## Actions

### ⚠️ Negative match types — a careless choice here destroys the campaign

| Negative | Match type | Why |
| --- | --- | --- |
| `spices` | **EXACT ONLY** | As a *phrase* negative it blocks 8 on-target terms worth **₹293.74** — almost all the good traffic |
| `garam masala` | **EXACT ONLY** | As a phrase it blocks `sabut garam masala` and `garam masala spices whole` — ₹53.42 |
| `mdh` | Phrase — safe | Blocks nothing on-target |
| `elaichi` | Phrase — safe | Blocks nothing on-target |
| `12 masala 13 saman dev hotel jaipur` | Exact | Junk |
| ASIN `B0FYY8TVNY` | Negative **product** target | Own cardamom listing |

### Everything else

| Action | Where | Detail |
| --- | --- | --- |
| Turn off / reduce **Substitutes** bid | Auto | ₹55.91, 0 sales; both clear waste items came from it |
| Harvest into Exact @ ₹8–12 | Exact | `biryani spices`, `khada masala sabut`, `biryani whole spices`, `sabut garam masala`, `khada masala mix`, `whole biryani masala spices`, `masala whole spices`, `biryani spices whole`, `whole spices biryani` |
| Then negative those terms in Auto | Auto | Auto discovers, Exact controls the bid |
| Small defensive brand campaign | New | `spiceto` at ~₹2 CPC — the only affordable traffic found |

**Harvest here means price control, not scaling.** Normally terms are harvested because they
convert; none of these did. The reason to move them is that Auto pays ~₹16 for them while Exact
can bid ₹8–10, far closer to what a ₹199 pack can carry.

`biryani spices` needs the cap most: **₹135.82, 23.5% of all spend, nothing back.**

## 7. Harvest executed — bids set on the 9 terms

Amazon's add-keyword dialog surfaced impression share and rank, which confirms the whole
niche-over-commodity argument numerically:

| Term | Impression share | Rank | Suggested bid |
| --- | --- | --- | --- |
| `biryani whole spices` | **24.64%** | **1** | **₹5.56** |
| `biryani spices` | 1.72% | 14 | ₹10.14 |

₹135.82 went into `biryani spices` in Auto for a 1.72% share at rank 14 — head-term prices for
invisibility. The more specific `biryani whole spices` gives rank 1 and a quarter of impressions
at half the bid. **The more specific the term, the cheaper it is and the more it is dominated.**

### Bids

Defaults came in at Amazon's suggestion, averaging ₹11.14 against a ₹4–9 ceiling.

| Keyword | Suggested | Set to | Why |
| --- | --- | --- | --- |
| `biryani whole spices` | ₹5.56 | **₹6.95** ↑ | *Raise.* Rank 1, 24.64% share, top-of-range still under ceiling. Buy more of the one term won cheaply. |
| `whole spices biryani` | ₹6.96 | ₹6.96 | Already inside the ceiling |
| `whole biryani masala spices` | ₹13.32 | ₹8.00 ↓ | Range floor is ₹6.87 |
| `biryani spices` | ₹10.14 | ₹7.61 ↓ | Range floor; 1.72% share does not justify more |
| `khada masala sabut` | ₹10.75 | ₹8.00 ↓ | Proven ₹60.79 in Auto |
| `khada masala mix` | ₹11.13 | ₹8.35 ↓ | Range floor |
| `sabut garam masala` | ₹13.42 | ₹9.03 ↓ | Floor sits at the ceiling edge |
| `masala whole spices` | ₹12.66 | ₹10.64 ↓ | Floor above ceiling — watch |
| `biryani spices whole` | ₹16.34 | **drop** | Dearest, floor ₹12.26, intent already covered |

≈23% lower in total, concentrated on affordable terms.

Bidding at range floors risks thin delivery; that is the price of staying near the ceiling. The
campaign's job right now is **diagnostic** — reach 100–200 clicks and settle whether the listing
converts. `biryani whole spices` at ₹6.95 is the best instrument for that, being the one place
real volume is affordable.

## 8. Auto switched off — Exact is now the whole campaign

State as of 2026-08-08 evening: **Auto and Broad off. Exact only**, ₹120/day, default bid ₹8,
16 keywords, 7 negatives. The head terms are gone — Exact impressions fell 47 → 11, exactly the
`garam masala whole` + `garam masala` traffic disappearing.

Two consequences: the "add the 9 terms as negatives in Auto" step is **moot** (nothing to
compete with), and **discovery has stopped.** Turn Auto back on at ~₹50/day for discovery only,
once the conversion question is settled.

### Still to clean: 10 of 16 keywords sit above the ₹9 ceiling

The nine harvested terms are correctly priced. The problem is the **original guessed keywords**,
still live at ₹9–13.40 with no volume after eight days:

| Keyword | Bid | Impressions | Action |
| --- | --- | --- | --- |
| `biryani garam masala` | ₹13.40 | 0 | **Pause** |
| `mix khada garam masala` | ₹12.98 | 0 | **Pause** |
| `khada garam masala mix` | ₹12.20 | 0 | **Pause** |
| `biryani whole spice mix` | ₹12.00 | 1 | **Pause** |
| `khada garam masala` | ₹12.00 | 1 | **Pause** — floor ₹11.38 is over ceiling; `khada masala sabut` covers the intent at ₹8 |
| `whole garam masala mix` | ₹9.70 | 0 | **Pause** |
| `whole spice garam masala` | ₹9.06 | 0 | **Pause** |
| `biryani masala whole spices` | ₹12.00 | **9** | **Cut to ₹8.00** — real term, most impressions of any old keyword, floor ₹7.68 |

Leaves ~9 keywords, every one drawn from a proven search query.

### Word-order duplicates compete with each other

Amazon's exact match treats word order as a close variant, so these match the same searches:

- `khada garam masala mix` / `mix khada garam masala` / `khada masala mix`
- `biryani whole spices` / `whole spices biryani`

Amazon picks one internally, often the higher bid — so keeping a ₹12.98 twin of an ₹8.35
keyword means occasionally paying ₹12.98 for traffic priced at ₹8.35. The pauses above resolve
most of it.

## 9. The decision rule

At ₹120/day and ₹8–9 CPC: **13–15 clicks/day, 150 clicks in 10–11 days, about ₹1,300.**

| If the listing truly converts | P(still 0 sales at 150 clicks) |
| --- | --- |
| 8% | 0.00% |
| 5% | 0.05% |
| 3% | 1.0% |

**Zero sales at 150 clicks convicts the listing** — stop spending, fix the page. Any sales,
measure the rate and recompute.

### Be clear-eyed: this will not be profitable

Break-even at ₹8 CPC needs **10–17% conversion** depending on COGS. The ~₹1,300 is **the price
of an answer, not an investment expected to pay back.**

A 5–8% result is still good news: it means the listing works and the only problem is that ₹199
cannot carry ₹8 clicks — fixed with the 180 g pack, bundles or price, not with ad tweaks.
