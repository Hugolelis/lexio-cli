# Lexio

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-1a1a2e?style=for-the-badge&logo=python&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white)]()

</div>

> **Lexio** is a command-line tool for lexiometric analysis of text documents. It extracts statistical insights from `.txt`, `.pdf`, and `.docx` files — including word frequency, vocabulary richness, and readability metrics — with automatic stopword filtering and configurable analysis parameters.

<details>
<summary><strong>Table of Contents</strong></summary>

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [Configuration](#configuration)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [License](#license)
- [Author](#author)

</details>

---

## About

Manually eyeballing a text for word frequency or vocabulary richness doesn't scale past a page. Lexio turns that into a single command across `.txt`, `.pdf`, and `.docx` files, computing the same lexicometric measures linguists use by hand — type-token ratio, hapax/dis legomena, word frequency — with stopword filtering built in so the numbers aren't dominated by "the", "and", "de", "que".

<!-- Adjust to your actual motivation — draft based on the feature list. -->

---

## Demo

```bash
lexio analyze sample.txt
```

```
╭───────────────────────╮
│ Lexiometric Analysis  │
│ File: sample.txt      │
╰───────────────────────╯

         Statistics
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Metric          ┃  Value ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Total Words     │    859 │
│ Unique Words    │    325 │
│ Sentences       │     72 │
│ Paragraphs      │     35 │
│ Avg Word Length │   3.99 │
│ Type-Token Ratio│ 0.3783 │
│ Hapax Legomena  │    204 │
│ Dis Legomena    │     47 │
└─────────────────┴────────┘
```

---

## Features

| Capability | Description |
|---|---|
| **Multi-format** | Analyze `.txt`, `.pdf`, and `.docx` files |
| **Lexiometric stats** | Total words, unique words, sentences, paragraphs |
| **Readability metrics** | Type-token ratio, hapax/dis legomena, average word length |
| **Word frequency** | Rank top words with visual bar charts |
| **Vocabulary** | List all unique words alphabetically or by frequency |
| **Word search** | Check exact frequency of any word |
| **Stopword filtering** | Built-in 300+ stopwords for English and Portuguese |
| **Custom stopwords** | User-defined word filters via `~/.lexio/stopwords.txt` |
| **Minimum length** | Filter out short words with `--min-length` |

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
git clone https://github.com/Hugolelis/lexio.git
cd lexio
pip install -e .
```

### Verify installation

```bash
lexio version
```

---

## Usage

### Basic analysis

```bash
lexio analyze sample.txt
```

### Top words

```bash
lexio top-words document.pdf -n 20
```

### Vocabulary

```bash
lexio vocabulary report.docx
lexio vocabulary sample.txt -s freq        # sort by frequency
lexio vocabulary sample.txt --min-length 4 # only words >= 4 chars
```

### Word frequency lookup

```bash
lexio freq sample.txt programming
```

### Stopword management

```bash
lexio stopwords                           # list all stopwords
lexio stopwords --lang en                 # english only
lexio stopwords --lang pt                 # portuguese only
```

### Including stopwords

By default, stopwords are filtered out. Include them with `--include-stopwords`:

```bash
lexio analyze sample.txt --include-stopwords
```

---

## Commands

| Command | Description | Aliases |
|---|---|---|
| `analyze` | Full lexiometric analysis with stats and top words | — |
| `top-words` | Rank most frequent words | — |
| `vocabulary` | List all unique words | — |
| `freq` | Check frequency of a specific word | — |
| `stopwords` | List all active stopwords | — |
| `version` | Show version | — |

### Global options

| Option | Description | Default |
|---|---|---|
| `--include-stopwords` | Include stopwords in results | `False` |
| `--min-length`, `-m` | Minimum word length to include | `3` |
| `--top`, `-t` | Number of top words to display | `10` |
| `--count`, `-n` | Number of words in top-words output | `10` |
| `--sort`, `-s` | Sort vocabulary by `alpha` or `freq` | `alpha` |
| `--lang`, `-l` | Filter stopwords by language | `all` |

---

## Configuration

### Custom stopwords

Create `~/.lexio/stopwords.txt` to add domain-specific words to filter:

```
# Custom stopwords
algorithm
framework
repository
```

The custom list merges with the built-in 300+ stopwords automatically.

---

## Architecture & Design Decisions

```
src/
├── main.py                 # Entry point
├── cli/
│   └── commands.py         # CLI commands (Typer)
├── services/
│   ├── analyzer.py         # Core analysis engine
│   └── readers.py          # File readers (.txt, .pdf, .docx)
└── helpers/
    ├── errors.py           # Custom exceptions
    └── stopwords.py        # Stopword lists and filtering
```

The pipeline follows a clean separation of concerns:

1. **Reader** — detects file extension and extracts raw text with paragraph count
2. **Analyzer** — tokenizes, counts, and computes statistical metrics
3. **CLI** — presents results using Rich tables and panels

**Why this shape:** readers are isolated behind a single interface so adding a new format (`.epub`, `.md`) only means implementing one more reader, without touching the analyzer. Typer was chosen for the CLI layer for its type-hint-driven commands and automatic `--help` generation; Rich handles output formatting so the analyzer stays free of any presentation logic.

**Known limitations:**
- No lemmatization/stemming — word variants (`run` / `running`) are counted as distinct words, which affects vocabulary and frequency metrics.
- Stopword filtering only ships English and Portuguese lists; other languages need a fully custom list via `~/.lexio/stopwords.txt`.
- Large PDFs are parsed synchronously — no progress indicator or streaming for very large files.

<!-- Adjust "Why this shape" and "Known limitations" to match your actual reasoning — draft based on the code structure. -->

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

## Author

**Hugo** — [GitHub](https://github.com/Hugolelis)
