# Do Low Exact-Match Impressions Mean Low Search Demand? (2026-08-18)

Question from the 11–18 Aug Exact keyword table: 10 keywords live, all showing the product,
but impressions are low across the board except `garam masala` at 35. Does low impressions
mean people aren't searching with these keywords?

## No — this is Exact match behaving exactly as designed, not a demand signal

**Exact fires only on the literal string typed, never on anything containing it.** This was
proven directly on 9 Aug (`volume-correction.md`): `biryani whole spices` was bid at ₹6.95 —
the top of its suggested range, meaning the auction was being won every time it was eligible —
and still drew only ~1 impression that day. The bid wasn't the constraint. Almost nobody types
that exact multi-word sequence verbatim; "biryani whole spices online," "best biryani whole
spices," "biryani whole spices 100g" are all different queries Exact never sees.

The current 9–10 keywords (`khada masala sabut`, `sabut garam masala`, `biryani masala whole
spices`, etc.) are all similarly specific, multi-word phrasings. Low impression counts across
the set is the structurally expected outcome of Exact match on long-tail terms — not evidence
that demand for biryani/khada garam masala is low.

## `garam masala`'s 35 impressions is the outlier for the opposite reason it looks like

It's the one short, generic, commodity-level term in the set. Brand Analytics ranked it around
**#9,654** search frequency (`brand-analytics-garam-masala.md`) — far higher overall search
volume than any of the specific khada/sabut/biryani phrasings. More impressions there is a
function of casting a wider net, not proof it's a "better" keyword. A meaningful share of that
volume is buyers looking for **powder**, not whole spices — the exact wrong-buyer risk already
flagged twice: `search-terms-findings.md` recorded ₹17.27 spent on this term for zero result
before it was negatived once, and `keyword-expansion-review.md` recommended cutting the
standalone bid to ₹6–7 if kept at all, specifically because it's the highest-volume,
least-relevant term in the set.

## Where the actual demand signal lives: Auto, not Exact

Proven directly by the 10 Aug week (`first-purchases-2026-08-10.md`): Auto's loose ("close
match") targeting on `biryani masala whole spices` produced all 3 purchases and ₹1,187.62 in
sales that week, while Exact ran flat at 0 purchases the whole time. Exact's role is to hold
the price down on phrasings Auto has already proven convert — it is not the layer that
discovers or measures demand.

## Practical read

**Don't treat low Exact impressions as a reason to raise bids or judge a keyword "dead."**
That's the tool doing what it's built to do. Keep watching Auto's weekly search terms report
for the real volume and conversion signal — that's where "are people searching for this"
actually gets answered.
