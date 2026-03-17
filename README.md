```
 ██╗     ███████╗██╗  ██╗██╗ ██████╗ 
 ██║     ██╔════╝╚██╗██╔╝██║██╔═══██╗
 ██║     █████╗   ╚███╔╝ ██║██║   ██║
 ██║     ██╔══╝   ██╔██╗ ██║██║   ██║
 ███████╗███████╗██╔╝ ██╗██║╚██████╔╝
 ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ 
```

# 📊 Lexio
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-in%20progress-orange?style=flat-square)]()
[![Version](https://img.shields.io/badge/version-0.1.0-blue?style=flat-square)]()

A command-line tool for lexiometric analysis of text files. Built with Python, focused on simplicity and statistical precision.

## ✨ Features

* **Word Frequency** — Analyze the most frequent words in a text.
* **Vocabulary & Unique Words** — Measure lexical richness and unique word count.
* **Top Words** — Displays the ranking of the most frequent words in the text.

---

## 🛠️ Tech Stack

* **Language:** [Python 3.11+](https://www.python.org/)
* **CLI:** [Typer](https://typer.tiangolo.com/) — modern CLI framework based on type hints
* **Terminal UI:** [Rich](https://rich.readthedocs.io/) — beautiful terminal output with tables and charts

---

## 📂 Project Structure

```text
lexio/
├── src/
│   ├── cli/
│   │   └── commands.py       # CLI commands and argument definitions
│   ├── services/
│   │   └── analyzer.py       # Core analysis logic
│   ├── helpers/
│   │   └── errors.py         # Custom error handling
│   └── main.py               # Entrypoint
├── pyproject.toml            # Project manifest and dependencies
└── README.md
```

---

## ⚙️ Running

#### 1. Clone the Repository

```bash
git clone https://github.com/Hugolelis/lexio.git
cd lexio
```

#### 2. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -e .
```

#### 4. Run

```bash

```

---

## 📄 License

This project is licensed under the **MIT** License. See the [LICENSE](LICENSE) file for details.
