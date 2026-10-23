"""Applique l'identité Argent Minute au kit vidéo (copié dans le dossier donné, ex. ~/bm).

Usage : python3 appliquer_identite.py ~/bm
Remplace le logo, les couleurs (bleu nuit → vert profond, jaune → or) et le bandeau d'en-tête.
"""
import sys, os, re, shutil, glob

kit = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/bm")
here = os.path.dirname(os.path.abspath(__file__))

COULEURS = {
    "#071430": "#04211A", "#0D2250": "#0A3D2F", "#11295C": "#0E4334", "#2A4A8C": "#1E6B52",
    "#FFD60A": "#F5C542", "#9DB0D6": "#A9CDBE", "#1C4BA8": "#178A63", "#123A8A": "#11634B",
    "#2A3F7A": "#1F5A47", "#0F2A63": "#0C3A2C", "#0A1A3D": "#062A20", "#040B1E": "#021410",
    "#3B63B3": "#2E8C6A", "#173A7E": "#145A44", "#2B4A8F": "#24704F", "#16336F": "#114C3A",
    "#102C66": "#0E4434", "#0F2758": "#0C3A2C", "#0E244F": "#0B3427", "#0A1C42": "#082C21",
    "#5B6B8C": "#5F7F72",
}
TEXTES = {"ACTU BELGIQUE · ": "ARGENT MINUTE · "}

shutil.copyfile(os.path.join(here, "logo_argent_772.png"), os.path.join(kit, "assets/logo/logo_bm.png"))
n = 0
for f in glob.glob(os.path.join(kit, "src", "*.py")):
    s = open(f, encoding="utf-8").read(); o = s
    for a, b in COULEURS.items():
        s = re.sub(re.escape(a), b, s, flags=re.I)
    for a, b in TEXTES.items():
        s = s.replace(a, b)
    if s != o:
        open(f, "w", encoding="utf-8").write(s); n += 1
reste = [c for f in glob.glob(os.path.join(kit, "src", "*.py")) for c in COULEURS if c.lower() in open(f).read().lower()]
assert not reste, f"couleurs non remplacées : {reste}"
assert "ARGENT MINUTE · " in open(os.path.join(kit, "src/render.py")).read()
print(f"Identité Argent Minute appliquée ({n} fichiers modifiés, logo remplacé).")
