import argparse
import re
from html import unescape
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Extract URLs from <loc> tags in an XML file."
)
parser.add_argument("-xml", required=True, help="Path to the XML input file")
parser.add_argument("-sortie", required=True, help="Path to the output TXT file")
args = parser.parse_args()

fichier_xml = Path(args.xml)
fichier_sortie = Path(args.sortie)

if not fichier_xml.is_file():
    parser.error(f"XML file not found: {fichier_xml}")

partie_a_enlever = input(
    "Enter the additional part to remove from each URL (press Enter to skip): "
).strip()

texte = fichier_xml.read_text(encoding="utf-8", errors="ignore")

liens = re.findall(
    r"<loc\b[^>]*>(.*?)</loc>",
    texte,
    flags=re.IGNORECASE | re.DOTALL
)

liens = [unescape(lien.strip()) for lien in liens if lien.strip()]

liens = [lien.replace("https://www.", "") for lien in liens]

if partie_a_enlever:
    liens = [lien.replace(partie_a_enlever, "") for lien in liens]

# 7yed 3lia zmer
liens = list(dict.fromkeys(liens))

fichier_sortie.write_text("\n".join(liens), encoding="utf-8")
print(f"{len(liens)} link(s) saved to: {fichier_sortie}")

