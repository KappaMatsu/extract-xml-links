XML Link Extractor

A small Python command-line tool that extracts URLs from <loc> tags in an XML file and saves them to a text file.
Features

    Extracts URLs from <loc> tags.
    Skips empty <loc> tags.
    Removes duplicate links while preserving their original order.
    Supports file paths containing spaces.
    Requires no external dependencies.

Requirements

    Python 3.8 or later.

Check that Python is installed:
bash

python --version

Depending on your system, you may need to use python3 instead of python.
Setup

Save the script as extraire_liens.py. No additional packages are required.
Usage
bash

python extraire_liens.py -xml "input.xml" -sortie "links.txt"

    -xml: Path to the XML input file.
    -sortie: Path to the output text file.

Example with paths containing spaces:
bash

python extraire_liens.py -xml "my files/site map.xml" -sortie "my files/extracted links.txt"

The output file will contain one link per line:
text

https://www.files.com/docs/networking-and-performance/ip-addresses/dedicated-ip-addresseshttps://www.files.com/docs/networking-and-performance/ip-addresses/hardcoded-or-static-ip-addresseshttps://www.files.com/docs/networking-and-performance/ip-addresses/bring-your-own-ip-byoip

Example XML File
xml

<url>  <loc>https://example.com/page-1</loc></url><url>  <loc>https://example.com/page-2</loc></url><url>  <loc></loc></url>

The empty <loc> tag is skipped.
Help

To display the available options:
bash

python extraire_liens.py --help
