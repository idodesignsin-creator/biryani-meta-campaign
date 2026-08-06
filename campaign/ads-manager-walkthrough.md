# Ads Manager — Manual Setup Walkthrough

For building the campaign by hand in the Ads Manager UI. Every ID here was resolved
against the live account, so the names below are the exact strings Meta's picker expects.

---

## Saved Audience 1 — "Spiceto | Metro Spice Buyers | 25-54"

### Locations — already done

Ahmedabad +17 km, Bangalore +20 km, Chennai +17 km, Delhi NCR +30 km,
Hyderabad +25 km, and the rest of the 12.

The 17 km values are Meta snapping to its preset steps (10 miles ≈ 17 km) where the plan
said 15 km. Leave them — the difference is immaterial to delivery.

### Uncheck "Reach more people likely to respond"

It's ticked by default. The fine print reads *"We'll also reach people interested in your
selected towns/cities and regions"* — that's location expansion, and it delivers to people
who are merely *interested in* Mumbai rather than living there.

You're selling a physical product that has to be delivered to a home address. Someone in
Dubai who follows Mumbai pages is not a customer. **Uncheck it.**

### Age and gender

- Minimum age: **25**
- Maximum age: **54**
- Gender: **All** — see the reasoning in `targeting.md`; revisit at day 7 on real data

### Detailed targeting — Include (the OR layer)

In the **Detailed targeting** box, type each of these and select the exact match:

| Type this | Meta ID (to verify you picked the right one) |
| --- | --- |
| `Cooking` | 6003659420716 |
| `Recipes` | 6003385609165 |
| `Indian cuisine` | 6003494675627 |

Three is enough. Meta treats these as OR, and `Cooking` (~753M) and `Recipes` (~481M)
already contain almost everyone the smaller cooking interests would add. Piling on
`Cookbook`, `Cooking At Home`, `Celebrity chef` and `Cooking shows` widens nothing and
just makes the audience harder to reason about later.

**Do not go looking for spice interests.** Searching Meta's live catalogue returns zero
results for `Biryani`, `Garam masala`, `Masala`, `Spice` and `Herbs and spices`. None of
them exist. `Amazon.in` doesn't either — the entity is `Amazon.com`.

### Detailed targeting — Narrow (the AND layer) ← this is the important step

Click **"Narrow audience"** underneath the Include box. A second box appears labelled
*"AND must also match at least one of the following"*. Into **that** box:

| Type this | Meta ID | What it is |
| --- | --- | --- |
| `Online shopping` | 6003346592981 | interest |
| `Amazon.com` | 6003002193982 | interest |
| `Engaged Shoppers` | 6071631541183 | behaviour — under Browse → Behaviours → Purchase behaviour |

This is the step that does the work. Layer 1 alone is everyone who likes food content.
Layer 2 alone is everyone who shops online. You want the intersection: people who cook
*and* actually buy things on the internet.

**On using `Amazon.com` for an Indian audience:** it's correct. Meta's interest entities
are brands, not domains — `Amazon.com` is *the company Amazon*, and Indian users who
engage with Amazon India get tagged against it. There is no per-marketplace interest for
any large brand; `Amazon.co.uk` and `Amazon.de` don't exist either.

It's also not load-bearing. All three narrow options are OR'd, and `Online shopping`
(~1.35B) and `Engaged Shoppers` (~1.13B) dwarf `Amazon.com` (~338M globally), so the
layer works regardless of how well the Amazon entity maps to India.

To verify: build a throwaway audience with the 12 India locations, 25–54, and
`Amazon.com` as the only interest. Tens of millions means it maps fine. Then delete it.

### Sanity check

The estimate should drop from **101M–118.8M** to somewhere in the **low tens of millions**.

If it barely moves, you've added the second group to the *Include* box instead of the
*Narrow* box. Include widens (OR), Narrow restricts (AND). Check that your screen shows
two separate boxes with **"AND must also match"** between them, not one long list.

Don't narrow any further. At ₹500/day you'll reach a small fraction of this audience
regardless, and over-narrowing raises CPM and slows the learning phase for no benefit.

### Confirmed built — 2026-08-06

Saved audience `claude Spiceto Biriyani Tire 1.0` built in Ads Manager and verified
against the plan:

| Setting | Value |
| --- | --- |
| Locations | 12 cities, radii as planned (Ahmedabad/Chennai snapped to 17 km) |
| Location expansion | Unchecked |
| Age | 25–54 |
| Gender | All |
| Include | Cooking (food & drink), Recipes (food & drink), Indian cuisine (food & drink) |
| And must also match | Engaged shoppers, Amazon.com (retailer), Online shopping (retail) |
| Languages | Blank |
| Custom audiences | None included, none excluded |

**Audience estimate: 41,300,000 – 48,600,000**, down from 101,000,000 – 118,800,000
before the narrow layer. Record this — it's the baseline to compare any future targeting
change against.

### A note on Meta's "Apply" suggestions

Ads Manager surfaces inline suggestions like *"6.7% lower cost per result — based on our
experiment"* with an Apply button. Read what each one proposes before accepting.

The common one here re-enables location expansion. Decline it: a cheaper click from
someone outside your delivery radius is not a cheaper customer. Meta's suggestion engine
optimises for the metric it can see (cost per result), not for whether the parcel can
physically arrive.

---

## Saved Audience 2 — "Spiceto | Broad | 25-54"

Click **Save as new** and build a second one:

- **Same 12 locations**, same radii
- **Same** "Reach more people likely to respond" unchecked
- Age **25–54**, gender **All**
- **Detailed targeting: completely empty**

That's the whole audience. It should read back around 100M+, and that's correct.

This is the ad set most likely to win. Meta's interest catalogue cannot express "buys
whole spices online" — there is no such interest — so hand-picked targeting is a loose
proxy at best. Given good creative and a clean optimisation signal, the delivery system
usually finds buyers better than the proxy does.

---

## At the ad set level (not in the audience tool)

These are set when you build the ad set, not when you save the audience:

| Setting | Value |
| --- | --- |
| Optimisation for ad delivery | **Landing page views** (not Link clicks) |
| Bid strategy | Highest volume, no cost cap |
| Placements | **Advantage+ placements** (automatic) |
| Advantage+ Audience | **On** for both ad sets |
| Budget | Campaign level, ₹500/day, CBO on |

**Advantage+ Audience on the interest ad set** turns your interests into suggestions rather
than hard walls. That's deliberate — given how poorly Meta's catalogue covers this
category, you want it able to look past your guesses.

---

## Campaign and ad settings

| Setting | Value |
| --- | --- |
| Objective | Traffic |
| Destination | Website |
| URL | `https://www.amazon.in/dp/B0H6TP1DNS?th=1` |
| URL parameters | see below |
| CTA button | **Shop Now** |
| Status | Leave **Paused** until everything is reviewed |

**URL parameters** field (this is a separate box below the website URL — do not paste
these into the URL itself):

```
utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&utm_placement={{placement}}&utm_site={{site_source_name}}
```

Reminder from `measurement.md`: Amazon does not report UTM values anywhere in Seller
Central. These are correct so they work the day you route through spiceto.in — they are
not measurement today. Baseline the ASIN in Business Reports before you launch.

---

## Naming

The saved audience is currently `claude Spiceto Biriyani Tire 1.0`. Two suggestions:

- "Tire" → **"Tier"**
- Drop the `claude` prefix — in six months you'll want to know *what the audience is*, not
  who set it up

Something like `Spiceto | Metro Spice Buyers | 25-54 | v1` reads better in a list of
thirty audiences, and matches the naming convention in `structure.md`.
