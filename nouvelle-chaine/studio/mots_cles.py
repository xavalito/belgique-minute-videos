"""Recherche de mots-clés : ce que les gens tapent vraiment sur YouTube et Google (Belgique, français).

Usage : python3 mots_cles.py "prime énergie" "indexation salaire"
Pour chaque expression : suggestions YouTube et Google, avec et sans « belgique », puis les mots
qui reviennent le plus. Choisir le mot-clé principal parmi ces suggestions (formulation exacte).
"""
import sys, json, time, urllib.parse, urllib.request
from collections import Counter

URL = "https://suggestqueries.google.com/complete/search?client=firefox&hl=fr&gl=BE&q="


def suggestions(q, youtube):
    url = URL + urllib.parse.quote(q) + ("&ds=yt" if youtube else "")
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return json.loads(r.read().decode("utf-8", "replace"))[1]
    except Exception as e:
        return [f"(erreur : {e})"]


def main():
    termes = sys.argv[1:]
    if not termes:
        sys.exit(__doc__)
    mots = Counter()
    for t in termes:
        for q in dict.fromkeys([t, t + " belgique", t + " 2026", t + " 2027"]):
            for yt in (True, False):
                s = suggestions(q, yt)
                print(f"{'YouTube' if yt else 'Google '} | {q} → " + " · ".join(s))
                for x in s:
                    mots.update(w for w in x.lower().split() if len(w) > 3)
                time.sleep(0.3)
    print("\nMots les plus recherchés :", ", ".join(w for w, _ in mots.most_common(25)))


if __name__ == "__main__":
    main()
