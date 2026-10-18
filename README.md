<div align="center">🔗 XML Link Extractor

⚡ Extract. Clean. Organize.

A lightweight Python CLI tool to extract clean URLs from XML files.

Turn messy XML sitemaps into a clean, deduplicated list of links — in seconds.

<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Dependencies-None-2EA44F?style=for-the-badge" alt="No dependencies"/>
  <img src="https://img.shields.io/badge/License-MIT-8A2BE2?style=for-the-badge" alt="MIT License"/>
</p><p>
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-example">Example</a> •
  <a href="#-contributing">Contributing</a>
</p></div>---

✨ Features

- 🔍 Automatic extraction — extracts URLs from XML "<loc>" tags.
- 🧹 Duplicate removal — keeps unique URLs while preserving their original order.
- 🛡️ Empty tag handling — automatically skips empty "<loc>" elements.
- 📂 Flexible file paths — supports paths containing spaces.
- ⚡ Zero dependencies — uses Python's standard library.
- 🐍 Simple CLI — straightforward commands, no complicated setup.

🚀 Installation

Prerequisites

- Python 3.8 or later

Check your Python version:

python --version

Get the project

git clone https://github.com/KappaMatsu/extract-xml-links.git
cd extract-xml-links

No additional packages are required. You're ready to go!

💻 Usage

Run the script with an XML input file and a destination text file:

python extraire_liens.py -xml "input.xml" -sortie "links.txt"

Argument| Description
"-xml"| Path to the input XML file
"-sortie"| Path to the output text file

Example with spaces in file paths:

python extraire_liens.py -xml "my files/site map.xml" -sortie "my files/extracted links.txt"

«💡 Tip: On some Linux or macOS systems, you may need to use "python3" instead of "python".»

📋 Example

Input — "sitemap.xml"

<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://example.com/</loc>
    </url>
    <url>
        <loc>https://example.com/about</loc>
    </url>
    <url>
        <loc>https://example.com/</loc>
    </url>
    <url>
        <loc></loc>
    </url>
</urlset>

Command

python extraire_liens.py -xml "sitemap.xml" -sortie "links.txt"

Output — "links.txt"

https://example.com/
https://example.com/about

The result: clean URLs, no empty entries, no duplicates. 🎯

🛠️ How It Works

       📄 XML File
           |
           v
    🔍 Parse <loc> Tags
           |
           v
    🧹 Skip Empty Values
           |
           v
    ♻️ Remove Duplicates
       (Keep Order)
           |
           v
       📋 links.txt

🆘 Help

Display the available command-line options:

python extraire_liens.py --help

🤝 Contributing

Contributions, suggestions and bug reports are welcome!

1. Fork this repository.
2. Create a feature branch: "git checkout -b feat/my-feature"
3. Commit your changes: "git commit -m "Add my feature""
4. Push your branch: "git push origin feat/my-feature"
5. Open a Pull Request.

Found a bug or have an idea? Feel free to open an "issue" (https://github.com/KappaMatsu/extract-xml-links/issues).

📜 License

This project is distributed under the MIT License. See the "LICENSE" (LICENSE) file for details.

---

<div align="center">⭐ If you find this project useful, consider giving it a star!

Made with 🐍 Python

<a href="https://github.com/KappaMatsu/extract-xml-links">KappaMatsu / extract-xml-links</a>

</div>