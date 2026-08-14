import re, math
from collections import Counter

# The 21 indexed title tags for mestahotel.com (from SERP data)
pages = {
 "/":                              "Luxury Hotel in Wayanad | Hotels in Sulthan Bathery - mesta Hotel",
 "/about.php":                     "mesta HOTEL - Best Hotels in Sulthan Bathery | Wayanad Hotels",
 "/rooms.php":                     "Rooms & Suites | Best Luxury Hotels in Wayanad - Mesta Hotel",
 "/rooms-pride.php":               "Best Hotels in Wayanad | Best Budget Hotels in Wayanad",
 "/luxury-balcony-rooms-wayanad.php":"Best Hotels in Wayanad | Best Budget Hotels in Wayanad",
 "/restaurants.php":               "Best Budget Hotels in Wayanad | Family Friendly Hotels in Wayanad",
 "/banquets.php":                  "Banquet Hall | Hotels in Sulthan Bathery | mesta Hotel Wayanad",
 "/things-todo.php":               "Things To Do In Wayanad | Top Attractions - Hotels in Wayanad",
 "/contact-mesta-hotel-wayanad.php":"Contact Top Hotels in Wayanad | Hotels in Sulthan Bathery",
 "/blog.php":                      "Welcome to mesta hotel",
 "/4-star-hotels-in-wayanad.html":  "Best Wayanad Hotels | 4-star Hotels In Wayanad | Mesta Hotels",
 "/rooms/blossom.html":            "Blossom | hotel rooms in wayanad | Top hotels in :wayanad",
 "/restaurants.html":              "Restaurants in Our Four-star Hotel | 4 star Hotels in Wayanad",
 "/facilities.html":               "Facilities at mesta Hotel | Couple friendly hotels in Wayanad",
 "/gallery.html":                  "Gallery | 4 star Hotels in Wayanad | Luxury hotels in Wayanad",
 "/offers-packages.html":          "Exclusive Deals at Wayanad Hotels | Mesta Hotel Offers",
 "/blog/adventure-activities":     "The Ultimate Guide to Adventure Activities in Wayanad",
 "/blog/solo-travelers-guide":     "Solo Traveler's Guide to Wayanad | Best Hotels In Wayanad | mesta Hotel",
 "/blog/wayanad-on-a-budget":      "Wayanad On A Budget | Choose Budget Resorts In Wayanad | Blog",
 "/blog/planning-a-wayanad-trip":  "Planning a Wayanad Trip | Best Hotels in Wayanad | Blog",
 "/blog/how-to-select-best-stay":  "Best Place to Stay in Wayanad | Mesta Hotel",
}

def tok(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in
            {"in","to","the","at","a","of","our","and","on","as","per","do"}]

docs = {u: tok(t) for u, t in pages.items()}
N = len(docs)
df = Counter()
for ws in docs.values():
    df.update(set(ws))

def vec(ws):
    tf = Counter(ws)
    v = {w: (c / len(ws)) * math.log(N / df[w]) for w, c in tf.items()}
    n = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {w: x / n for w, x in v.items()}

V = {u: vec(ws) for u, ws in docs.items()}

def cos(a, b):
    return sum(v * b.get(w, 0.0) for w, v in a.items())

urls = list(pages)
pairs = []
for i in range(len(urls)):
    for j in range(i + 1, len(urls)):
        pairs.append((cos(V[urls[i]], V[urls[j]]), urls[i], urls[j]))
pairs.sort(reverse=True)

print("TF-IDF COSINE SIMILARITY - mestahotel.com title tags")
print("=" * 78)
print("\nMOST SIMILAR PAGE PAIRS (cannibalization risk):\n")
for s, a, b in pairs[:14]:
    flag = "CRITICAL" if s > .85 else "HIGH" if s > .60 else "MODERATE" if s > .40 else ""
    print(f"  {s:5.3f}  {flag:9} {a}\n         {'':9} {b}\n")

# centroid: how "generic" is each title vs the site average
cent = Counter()
for v in V.values():
    for w, x in v.items():
        cent[w] += x / N
cn = math.sqrt(sum(x * x for x in cent.values())) or 1.0
cent = {w: x / cn for w, x in cent.items()}

print("=" * 78)
print("\nDISTANCE FROM SITE CENTROID (low = generic/undifferentiated):\n")
for s, u in sorted((cos(V[u], cent), u) for u in urls):
    bar = "#" * int(s * 40)
    print(f"  {s:5.3f} {bar:<40} {u}")
