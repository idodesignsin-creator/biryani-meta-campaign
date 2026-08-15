# Cristal Kuruva Resort, Wayanad — Meta Ad Audience

A second, unrelated campaign tracked in this repo alongside the Spiceto biryani spices
work. This folder covers **audience targeting only** — a Custom Saved Audience for the
resort's Meta (Facebook/Instagram) ads, not the full campaign build.

## Brief, as given

- **Property:** Cristal Kuruva Resort, Wayanad, Kerala
- **Audience type requested:** a **Custom Saved Audience** — manual detailed targeting,
  not Meta's automatic/Advantage+ Audience expansion
- **Focus:** high-profile / high-converting premium travellers
- **Geography:** Kerala, Bangalore, Tamil Nadu, Mumbai

## Status — API creation is blocked right now

The connected ad account (`387266110719612`, I DO Designs Ad account) is reachable, but
the **Adspirer tool quota is at 0/15 for this billing period, resetting 2026-09-04**. That
blocks every live Meta Marketing API call, including the location/interest ID lookups
needed to fill in the spec below with verified numbers.

Nothing here needed the API to be useful, though: a Saved Audience is normally built by
hand in Ads Manager anyway, so the spec below is written to be typed straight into that
UI today. See [`audience-targeting.md`](audience-targeting.md).

Once quota resets, [`audience-spec.json`](audience-spec.json) is the machine-readable
version — feed it back to me and I'll resolve the real location/interest IDs and either
attach it to a new ad set or confirm the manual build matches.

## What's here

| File | Covers |
| --- | --- |
| [`audience-targeting.md`](audience-targeting.md) | The full targeting spec, reasoning, and copy-paste Ads Manager build steps |
| [`audience-spec.json`](audience-spec.json) | Machine-readable version for API creation once quota resets |
