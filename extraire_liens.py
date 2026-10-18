import argparse
import re
from html import unescape
from pathlib import Path

parser = argparse.ArgumentParser(description="Extraire les liens <loc> d'un fichier XML")
parser.add_argument("-xml", required=True, help="Chemin du fichier XML d'entrée")
parser.add_argument("-sortie", required=True, help="Chemin du fichier TXT de sortie")
args = parser.parse_args()

fichier_xml = Path(args.xml)
fichier_sortie = Path(args.sortie)

if not fichier_xml.is_file():
    parser.error(f"Fichier XML introuvable : {fichier_xml}")

texte = fichier_xml.read_text(encoding="utf-8", errors="ignore")

liens = re.findall(r"<loc\b[^>]*>(.*?)</loc>", texte, flags=re.IGNORECASE | re.DOTALL)
liens = [unescape(lien.strip()) for lien in liens if lien.strip()]
liens = list(dict.fromkeys(liens))  # Supprime les doublons

fichier_sortie.write_text("\n".join(liens), encoding="utf-8")
print(f"{len(liens)} lien(s) enregistré(s) dans : {fichier_sortie}")
