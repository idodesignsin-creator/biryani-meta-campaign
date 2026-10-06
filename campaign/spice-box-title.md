# Spice Box — title review (2026-10-06)

Second Spiceto listing: **Premium Kerala Spice Box, Combo of 4, 230 g, ₹599 (MRP ₹799)**.
Contents per the A+ image: 50 g green cardamom, 85 g black pepper, 45 g cloves, 50 g cinnamon,
packed in a clear four-compartment box. Amazon files it under
**Grocery › Hampers & Gourmet Gifts › Spices Gifts**.

## Current title (199 characters)

> Spiceto Premium Kerala Spice Box (Combo of 4, 230g) - Green Cardamom, Black Pepper, Cloves &
> Indian Cinnamon | Single-Origin Idukki Spices | Export Quality Whole Spices | Farm Fresh
> Traditional Combo

## What's wrong with it

1. **The listing is in a gift category, but the title never mentions gifting.** People shopping
   in Spices Gifts search for *spices gift box*, *gift hamper*, *Diwali gift* and *corporate
   gift*, and the title contains none of those words. At ₹599 for 230 g (₹299.50/100 g) this
   doesn't compete on price per gram with loose cardamom and pepper. It competes as a gift.
   **Diwali is 8 Nov, about four weeks away**, which is the biggest gifting window of the year.
2. **"Spice Box" on its own is ambiguous.** Amazon autocomplete already showed that
   *"spices storage box"* refers to the empty container, the masala dabba
   (`autocomplete-findings.md`). With "Spice Box" leading the title, container shoppers see this
   listing and don't click, which pulls CTR down. Writing **"Spices Gift Box"** makes the meaning
   clear and still matches the query *spice box*.
3. **About 50 characters go on words nobody searches for.** *Premium*, *Export Quality*, *Farm
   Fresh*, *Traditional* and the second *Combo* bring in almost no queries. Amazon's title
   guidance also discourages subjective and promotional wording.
4. **"Indian Cinnamon" isn't how shoppers search.** They type *cinnamon sticks* or *dalchini*.
   Also check what the product actually is. True cinnamon (*Cinnamomum verum*) and cassia are
   different spices, and on the biryani listing the Ingredients attribute already had two spices
   declared wrongly (`listing-fixes.md`). The photo shows bark that is mostly flat, broken
   pieces rather than rolled quills. If it's cassia, call it cassia everywhere, including the
   Ingredients attribute.
5. **The title is 199 characters, but the cap is 75** (confirmed). The long title only survives
   because it was saved before the cap, so the replacement below is written for 75.

## Final — title 72/75, Item Highlight 125/125

The 75-character cap is confirmed for this listing, so the title holds only the core match terms
and the Item Highlight carries everything else. **No word appears in both fields.** Repeating a
word doesn't strengthen it, it only uses up space.

### Item Name (72 of 75 characters)

```
Spiceto Kerala Spices Gift Box 230g - Cardamom, Pepper, Cloves, Cinnamon
```

- **Brand, origin, what it is and the weight** sit in the first 35 characters, which still show
  when mobile search results cut the title short.
- **"Spices Gift Box"** matches *spice box*, *spices gift box* and *gift box* queries, and tells
  container shoppers this isn't an empty masala dabba.
- **All four spices are named in English**, because those are the primary search terms.
  *Pepper* also matches *black pepper*, since *black* is in the highlight.

### Item Highlight (125 of 125 characters)

```
Diwali & Corporate Gift Hamper - Combo of 4 Idukki Whole Spices: 50g Green Elaichi, 85g Black Pepper, 45g Laung, 50g Dalchini
```

Everything the title couldn't fit:

| Moved here | Why |
| --- | --- |
| Diwali, Corporate, Gift Hamper | The gift queries that belong to this category |
| Combo of 4 | *Combo* is a word shoppers type (`autocomplete-findings.md`) |
| Idukki, Whole | The single-origin claim, and the *whole spices* queries |
| Green, Black | Complete *green cardamom* and *black pepper* |
| Elaichi, Laung, Dalchini | Hindi names, so the English names in the title aren't repeated |
| 50g / 85g / 45g / 50g | Per-spice weights help conversion: the buyer sees 50 g of cardamom |

The highlight uses exactly 125 characters, so any edit must stay the same length. **After Diwali,
swap `Diwali` for `Festive`.** Both are six characters, so it still fits.

**Dropped completely:** Premium, Export Quality, Farm Fresh, Traditional, Single-Origin (Idukki
already says it). As noted above, if the cinnamon is actually cassia, change *Cinnamon* and
*Dalchini* to cassia before publishing.

### Generic keywords (backend search terms), gift-led: 247 of 250 bytes

The title already covers the product terms (spices, cardamom, pepper, cloves, cinnamon, Kerala).
This listing sits in **Spices Gifts**, and the buyer isn't searching for "cardamom". They're
searching for *something to give*. So the whole backend field goes on gift intent: occasions,
recipients and gift formats. None of these words is in the title. Amazon combines them with the
title's *gift box* and *spices*, so each one creates queries like *corporate gift box*,
*diwali gift hamper*, *gift for employees*, *housewarming gift* and *spices gift basket*.

```
corporate diwali hamper employee client festive deepavali dhanteras navratri christmas new year housewarming griha pravesh wedding return favour guests anniversary parents family friends staff office bulk souvenir gourmet edible food basket pongal
```

| Group | Words | Example queries completed with the title |
| --- | --- | --- |
| Corporate / B2B | corporate employee client staff office bulk | *corporate diwali gift*, *gift for employees*, *client gift box*, *bulk diwali gifts* |
| Festivals (now → Jan) | diwali deepavali dhanteras navratri christmas new year pongal | *diwali gift hamper*, *dhanteras gift*, *christmas gift box*, *new year gift* |
| Life events | housewarming griha pravesh wedding anniversary | *housewarming gift*, *griha pravesh return gift*, *wedding return gift* |
| Return gifts | return favour guests | *return gift for guests*, *wedding favour* |
| Recipients | parents family friends | *gift for parents*, *diwali gift for family* |
| Gift format | hamper basket festive gourmet edible food souvenir | *gourmet gift hamper*, *edible gift*, *food gift basket*, *kerala souvenir* |

Rules followed: no title words, no repeats, no plurals (Amazon matches *hampers* from *hamper*),
no competitor brands, and no unverifiable claims such as *luxury*, *premium* or *best*.

**Rotate the festival words through the year.** Seller Central allows edits at any time, and
past festivals waste bytes:

| When | Remove | Add |
| --- | --- | --- |
| After Diwali (mid-Nov) | navratri dhanteras deepavali | sankranti thanksgiving secret santa |
| After Pongal (late Jan) | christmas new year pongal | eid holi womens day |
| Late July | (spring festivals) | rakhi raksha bandhan onam |
| Late Sept | (Rakhi, Onam) | navratri dhanteras deepavali |

Keep *diwali* in all year. It's the biggest gift query and still gets searched outside the season.

**Note:** *souvenir* targets tourists looking for something to take home from Kerala. Idukki and
Munnar are spice-tourism destinations, so it fits the product even though it isn't a festival.

## What would move conversion more than the title

- **The main image shows only the box.** For a gift, the second image should show it
  *gift-wrapped or in a sleeve*, if packaging like that exists. If it doesn't, that's the bigger
  gap.
- **Reviews.** As on the biryani listing, a strong title brings clicks, and reviews turn those
  clicks into orders. Consider adding this ASIN to the Vine plan once FBA stock is in.
- **A Diwali deal or coupon** shows a badge next to the title in search results, which helps
  more than any wording change in late October.
