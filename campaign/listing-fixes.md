# Listing Fixes — Detail Page Audit (2026-08-09)

Reviewed the live Seller Central record for `B0H6TP1DNS` (SKU GJ-4847-CO3V).

## 1. The title omits every word buyers actually type

**Current:** `Spiceto Premium Whole Garam Masala 90g | 12 Hand-Weighed Spices`

**63 characters of ~200 available — under a third of the indexing space used.**

| Missing word | Ad spend from search terms containing it |
| --- | --- |
| **biryani** | **₹257.07** |
| **sabut** | ₹109.92 |
| **khada** | ₹82.94 |

*Biryani* does not appear in the title of a biryani product. Neither do the two Hindi words
that drove 23% of paid traffic. Money is being spent on clicks for `khada masala sabut` and
`biryani whole spices` while the listing ranks organically for neither.

### Replacement (170 characters)

```
Spiceto Biryani Whole Spices 90g | Khada Garam Masala Sabut, 12 Hand-Weighed Spices from Idukki Kerala | Ready to Grind for Authentic Biryani, Curry & Rice | 50+ Servings
```

Covers biryani, khada, sabut, whole spices, garam masala, 90g, 12, hand-weighed, Idukki,
Kerala, ready to grind, curry, rice, 50+ servings. Brand first, then the dominant search term —
Amazon weights early words more heavily.

## 2. Correction: the description is NOT empty

`vine-blocker.md` named the empty description field as the first suspect for Vine's
"incomplete" verdict. **That is wrong** — the description is present and substantial, and there
are 6 bullet points.

**Remaining suspects: the Images tab and the Offer tab.** Image count is the most common cause;
Vine also requires an FBA offer in New condition with stock available.

## 3. Two spices are labelled wrongly — INCLUDING IN THE INGREDIENTS FIELD

**Escalated.** The error is not only in marketing copy. The structured **Ingredients** attribute
— the legal ingredient declaration for a packaged food — reads:

> • Cardamom • Black Pepper • Clove • Cinnamon • Bay Leaf • Nutmeg • Mace (Javithri) • Star
> Anise • Cumin (Jeerakam) • Poppy Seeds (Khus Khus) • **Fenugreek (Sha Jeerakam)** •
> **Fenugreek (Perumjeerakam)**

Under FSSAI labelling rules an accurate ingredient declaration is required. Beyond compliance:
someone avoiding fenugreek is misinformed, and someone who reacts to fennel is not warned.

**Also check the printed pouch.** If the physical label carries the same error, that is a larger
fix than a Seller Central edit.


The description reads: *"Fenugreek (Sha Jeerakam), Fenugreek (Perumjeerakam)"* — both wrong, and
they are not the same spice as each other.

| Malayalam | Actually is | Listed as |
| --- | --- | --- |
| Jeerakam | Cumin | Cumin ✓ |
| Sha Jeerakam | Caraway / Black Cumin (shahi jeera) | **Fenugreek** ✗ |
| Perumjeerakam | **Fennel (saunf)** | **Fenugreek** ✗ |

Fenugreek is *uluva* / methi — neither of these. Bullet 1 repeats the error.

**Why this matters more than a normal typo:** the whole proposition is precision and expert
knowledge, and the target buyer grinds their own masala — precisely the person who knows
perumjeerakam is fennel. Getting two of twelve spices wrong undermines the claim on the very
page where it is being made.

## 4. `hand-weighted` should be `hand-weighed`

Title has it right. Description says "hand-weighted", "HAND-WEIGHTED PRECISION",
"Hand-weighting". This is the **third** asset with this word wrong — video QC found
`HAND-WELGHED`. Fix everywhere at once.

## 5. Bullet 1 names 11 spices, then says "& more"

There are exactly 12. List all twelve. "& more" on a 12-item list reads as though something is
being withheld, when the complete list is the strongest proof on the page.

## 6. Minor — "99% consistency"

Bullet 2 carries an unsupported statistic. Precise-sounding numbers with no source reduce
credibility rather than adding it. *"Identical ratio in every pack"* says the same thing without
inviting the question.

## 7. More field-level errors found on the attributes page

- **Serving Size Description** — *"1 to 2 teaspoons if you **griend** it"* → grind
- **Parent ASIN title** — *"Biriyani mix varrient"* → two typos (Biryani, variant)
- **Nutrition sections all empty** — Energy, Fat, Protein, Carbohydrate, Vitamins & Minerals.
  Not marked required and **not** the Vine blocker, but FSSAI expects nutritional information on
  packaged food and Amazon displays these fields.

## Also observed

- **Item Highlight** — `Perfect for Biryani, Curries, Rice Dishes - 50+ Servings`. Carries
  biryani and the servings claim, but highlights weigh far less than the title.
- **Generic Keywords** — `khada combo pack dum sabut authentic arcot idukki lucknowi kolkata
  ambur south indian elaichi tejpatta kali mirch laung`. Has khada and sabut, but **not
  biryani**. Backend keywords rank far below the title regardless.
- **Browse node** — Grocery > Cooking & Baking Supplies > Spices & Masalas > Whole Spices,
  Seeds & Herbs. Correct.
- **A/B Experiments** — "Not eligible due to low traffic". Independent confirmation of the
  traffic problem.
