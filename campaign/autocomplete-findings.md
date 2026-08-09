# Amazon Autocomplete — Real Demand Data (2026-08-09)

Amazon's search-bar suggestions are ordered by popularity. They are **better keyword evidence
than the paid search-terms report**, because they show demand that has not yet been paid to
discover.

## What people actually type

Typing `biryani spices`:

| Suggestion | Note |
| --- | --- |
| biryani spices | |
| biryani spices whole | |
| biryani spices storage box | different product — spice boxes |
| biryani spices combo pack all | **combo** |
| biryani spices box | different product |
| biryani spices whole combo | **combo** |
| biryani spices box for kitchen | different product |
| biryani spices combo | **combo** |
| biryani spices strainer | different product |
| biryani spices shajeera | a spice this product contains |

Typing `biryani whole`:

| Suggestion | Note |
| --- | --- |
| biryani whole spices | |
| biryani whole spices combo | **combo** |
| biryani whole masala | |
| biryani whole spices masala | |
| biryani whole spices all mix | |
| biryani whole spice mix | real query, but small — see below |
| biryani whole kit | **blocked by a negative** |
| biryani masala whole spices all mix | |
| biryani raw spices whole kit | **blocked by a negative** |
| biryani whole species | misspelling of "spices" |

## What this changes — and one thing it does not

**1. `combo` should never have been dropped from backend keywords.** The original backend list
had `combo pack`; an earlier pass here removed it as low value. Autocomplete puts **`combo` in 4
of 20 suggestions** — one of the highest-volume modifiers in the category. The seller's instinct
was right.

**2. `biryani whole spice mix` — the "re-add it" call was itself an overstatement.**

Autocomplete proves a query **exists and is typed**. It does not prove the query carries
meaningful volume — position 6 of 10 says real, not big. Meanwhile the keyword's own history is
real evidence the other way: bid at **₹15.09, exactly Amazon's suggestion and inside the
₹9.34–₹18.86 range**, it drew **1 impression in 8 days** (at 50% top-of-search). Both things are
true — a genuine query, and a small one.

**Do not re-add it as exact.** The phrase keyword `biryani whole spices` already covers it:
phrase match fires when the phrase appears in order with extra words around it, and
`biryani whole spice mix` contains `biryani whole spice` + `mix`, with singular/plural handled as
a close variant. The phrase keyword catches it at a lower bid with nothing extra to manage.

## Negatives that are blocking real demand

- **`kit` (negative phrase)** — blocks `biryani whole kit` and `biryani raw spices whole kit`,
  both popular searches for exactly this product. **Remove.**
- **`ready` (negative phrase)** — blocks any query containing "ready", including the product's own
  *ready to grind* positioning. **Remove.**

## This settles the phrase-match case

| Phrase keyword | Autocomplete searches it catches |
| --- | --- |
| `biryani spices` | **7** |
| `biryani whole spices` | **4** |

Two phrase keywords cover eleven real queries — far more efficient than adding eleven exact
keywords, and it is how the volume problem gets solved.

## Competitive read

The products ranking for `biryani spices combo pack all` are **Tulua 12-variety combo, Tulua
4-pack, Bhoj 10-in-1 hamper, DRY FRUIT HUB 650 g combo** — all multi-pack variety sets of
*separate* spices.

Spiceto is 12 spices blended in one pouch. **Different product.** So:

- **Do** use `combo` in backend keywords to catch the search.
- **Do not** restyle the listing as a combo pack. A buyer expecting 12 separate jars would be
  disappointed, and that route earns returns and 1-star reviews — the exact opposite of what this
  listing needs.

Also observed: search results still display the **old title**. Amazon had not reindexed at the
time of capture, which is expected within 24–72 hours.

## Updated backend keywords — 247 / 250 bytes

```
biriyani khade saboot podi thalassery malabar hyderabadi kolkata ambur arcot lucknowi bhatkal handi pilaf tadka elaichi tejpatta dalchini laung jaiphal javitri saunf shahi jeera kali mirch south indian briyani kadha combo kit species shajeera pack
```

**Added:** `combo kit species shajeera pack` — `species` is a genuine misspelling appearing in
the suggestions, `shajeera` is a spice the product contains.
**Dropped for room:** `donne phodni potli dindigul` — the thinnest regional terms.

## Auto campaign is choked — 5 impressions on 9 Aug

Down from 454/day. Two causes stacked:

1. **Only Close match is enabled** — Loose match, Substitutes and Complements were all switched
   off. The 454 came from all four groups together.
2. **The 26 negatives include the 9 terms that were 74% of Auto's spend.** Auto is blocked from
   everything it was good at.

**Fix:** re-enable **Loose match** at ~₹8, and cut **Close match from ₹19.59 to ₹10** — that bid
is still more than twice the affordable ceiling.
