# Lexio

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-1a1a2e?style=for-the-badge&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white)]()

</div>

A command-line tool for lexiometric analysis of text files. Built with Python, focused on simplicity and statistical precision.

---

## Features

- **Multi-Format Support** — Analyze `.txt`, `.pdf`, and `.docx` files.
- **Full Analysis** — Complete lexiometric analysis with statistics (total words, unique words, sentences, paragraphs, avg word length, type-token ratio, hapax/dis legomena).
- **Word Frequency** — Check the frequency of any specific word in a text.
- **Vocabulary & Unique Words** — Display all unique words, sorted alphabetically or by frequency.
- **Top Words** — Displays the ranking of the most frequent words in the text with visual bars.
- **Smart Stopword Filtering** — Automatically filters 300+ stopwords and connectives in English and Portuguese.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-1a1a2e?style=for-the-badge&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-1a1a2e?style=for-the-badge&logo=fastapi&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-1a1a2e?style=for-the-badge&logo=python&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1a1a2e?style=for-the-badge&logoColor=white)
![python-docx](https://img.shields.io/badge/python--docx-1a1a2e?style=for-the-badge&logoColor=white)

---

## Project Structure

```text
lexio/
├── src/
│   ├── cli/
│   │   └── commands.py
│   ├── services/
│   │   ├── analyzer.py
│   │   └── readers.py
│   ├── helpers/
│   │   ├── errors.py
│   │   └── stopwords.py
│   └── main.py
├── pyproject.toml
└── README.md
```

---

## Running

**1. Clone the repository**
```bash
git clone https://github.com/Hugolelis/lexio.git
cd lexio
```

**2. Install dependencies**
```bash
pip install -e .
```

**3. Run**
```bash
# Full analysis
lexio analyze <file.txt>
lexio analyze <file.pdf>
lexio analyze <file.docx>

# Top words
lexio top-words <file> -n 20

# Vocabulary
lexio vocabulary <file> -s freq

# Word frequency
lexio freq <file> <word>

# Stopwords
lexio stopwords
lexio stopwords --lang en
lexio stopwords --lang pt
```

---

## Custom Stopwords

Create `~/.lexio/stopwords.txt` to add your own words to filter:

```text
# Custom stopwords for Lexio
# One word per line. Lines starting with # are ignored.
algorithm
framework
library
```

These words will be automatically combined with the built-in stopwords.

---

## License

Licensed under the **MIT** License. See [LICENSE](LICENSE) for details.
