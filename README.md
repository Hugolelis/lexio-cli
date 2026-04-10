# Lexio

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Progress-1a1a2e?style=for-the-badge&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white)]()

</div>

A command-line tool for lexiometric analysis of text files. Built with Python, focused on simplicity and statistical precision.

---

## Features

- **Word Frequency** — Analyze the most frequent words in a text.
- **Vocabulary & Unique Words** — Measure lexical richness and unique word count.
- **Top Words** — Displays the ranking of the most frequent words in the text.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-1a1a2e?style=for-the-badge&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-1a1a2e?style=for-the-badge&logo=fastapi&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-1a1a2e?style=for-the-badge&logo=python&logoColor=white)

---

## Project Structure

```text
lexio/
├── src/
│   ├── cli/
│   │   └── commands.py
│   ├── services/
│   │   └── analyzer.py
│   ├── helpers/
│   │   └── errors.py
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

**2. Create and activate virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -e .
```

**4. Run**
```bash
# comando aqui quando disponível
```

---

## License

Licensed under the **MIT** License. See [LICENSE](LICENSE) for details.
