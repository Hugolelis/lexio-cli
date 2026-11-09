# Lexio

<div align="left">

[![Status](https://img.shields.io/badge/Status-Active-407a50?style=for-the-badge&labelColor=1a1a1a&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-0f766e?style=for-the-badge&labelColor=1a1a1a&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-0f766e?style=for-the-badge&labelColor=1a1a1a&logoColor=white)](LICENSE)

</div>

> **Lexio** is a command-line tool for lexiometric analysis of text documents. It extracts statistical insights from `.txt`, `.pdf`, and `.docx` files, including word frequency, vocabulary richness, and readability metrics, with automatic stopword filtering and configurable analysis parameters.

<details>
<summary><strong>Table of Contents</strong></summary>

- [About](#about)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [Configuration](#configuration)
- [Author](#author)
- [License](#license)

</details>

---

## About

Manually eyeballing a text for word frequency or vocabulary richness doesn't scale past a page. Lexio turns that into a single command across `.txt`, `.pdf`, and `.docx` files, computing the same lexicometric measures linguists use by hand (type-token ratio, hapax/dis legomena, word frequency) with stopword filtering built in so the numbers aren't dominated by "the", "and", "de", "que".

---

## Demo

```bash
printf 'The quick brown fox jumps over the lazy dog. The dog sleeps!\n\nA fox is quick; the programming of programming is fun.\n' > sample.txt
lexio analyze sample.txt --top 3
```

```
╭──────────────────────╮
│ Lexiometric Analysis │
│ File: sample.txt     │
╰──────────────────────╯

         Statistics
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Metric           ┃  Value ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Total Words      │     22 │
│ Unique Words     │     14 │
│ Sentences        │      3 │
│ Paragraphs       │      2 │
│ Avg Word Length  │   4.09 │
│ Type-Token Ratio │ 0.6364 │
│ Hapax Legomena   │      8 │
│ Dis Legomena     │      5 │
└──────────────────┴────────┘

                         Top 3 Words
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Rank ┃ Word  ┃ Frequency ┃ Bar                            ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│    1 │ quick │         2 │ ██████████████████████████████ │
│    2 │ fox   │         2 │ ██████████████████████████████ │
│    3 │ dog   │         2 │ ██████████████████████████████ │
└──────┴───────┴───────────┴────────────────────────────────┘
```

The statistics describe the whole text, while the ranking leaves stopwords out (`the`, `is`, `of`, ...). Use `--include-stopwords` to keep them in the ranking.

---

## Features

| Capability | Description |
|---|---|
| **Multi-format** | Analyze `.txt`, `.pdf`, and `.docx` files |
| **Lexiometric stats** | Total words, unique words, sentences, paragraphs |
| **Vocabulary richness** | Type-token ratio, hapax and dis legomena, average word length |
| **Word frequency** | Rank top words with visual bar charts |
| **Vocabulary** | List all unique words alphabetically or by frequency |
| **Word search** | Check the exact frequency (and share of the text) of any word |
| **Stopword filtering** | 570+ built-in stopwords for English and Portuguese, inspectable with `lexio stopwords` |
| **Custom stopwords** | User-defined word filters via `~/.lexio/stopwords.txt` |
| **Minimum length** | Filter out short words with `--min-length` (default 3) |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Python](https://python.org) >= 3.11 | Core language |
| [Typer](https://typer.tiangolo.com) | CLI interface builder |
| [Rich](https://rich.readthedocs.io) | Tables, panels and colored output |
| [PyMuPDF](https://pymupdf.readthedocs.io) | PDF text extraction |
| [python-docx](https://python-docx.readthedocs.io) | DOCX text extraction |

---

## Architecture & Design Decisions

```
.
├── src/
│   ├── main.py             # Entry point (the `lexio` script)
│   ├── cli/
│   │   └── commands.py     # CLI commands (Typer + Rich output)
│   ├── services/
│   │   ├── analyzer.py     # Core analysis engine (Analyzer, LexioResult)
│   │   └── readers.py      # File readers (.txt, .pdf, .docx)
│   └── helpers/
│       ├── errors.py       # Custom exceptions (LexioError, FileNotFound, InvalidFile)
│       └── stopwords.py    # Stopword lists, custom stopwords and filtering
├── pyproject.toml
├── LICENSE
└── README.md
```

The pipeline follows a clean separation of concerns:

1. **Reader**: detects file extension and extracts raw text with paragraph count
2. **Analyzer**: tokenizes, counts, and computes statistical metrics
3. **CLI**: presents results using Rich tables and panels

**Why this shape:** readers are isolated behind a single `read_file` function, so adding a new format (`.epub`, `.md`) only means implementing one more reader, without touching the analyzer. The analysis runs once and returns a result object; stopword filtering and minimum length are applied afterwards when asking for the top words or the vocabulary, so the statistics always describe the whole text. Typer was chosen for the CLI layer for its type-hint-driven commands and automatic `--help` generation; Rich handles output formatting so the analyzer stays free of any presentation logic.

**Known limitations:**
- No lemmatization/stemming: word variants (`run` / `running`) are counted as distinct words, which affects vocabulary and frequency metrics.
- Words are sequences of letters (accented letters and apostrophes included), so numbers are ignored, and sentences are counted by splitting on `.`, `!` and `?`.
- Stopword filtering only ships English and Portuguese lists; other languages need a fully custom list via `~/.lexio/stopwords.txt`.
- `freq` looks the word up in the raw counts, so it also finds stopwords and ignores `--min-length`.
- Paragraphs in PDFs are counted as text blocks, which is an approximation.
- Large PDFs are parsed synchronously: no progress indicator or streaming for very large files.
- No automated tests yet.

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
git clone https://github.com/Hugolelis/lexio-cli.git
cd lexio-cli
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

The `lexio` command is installed inside the virtual environment, so activate it before using it in a new terminal.

### Verify installation

```bash
lexio version
```

---

## Usage

### Basic analysis

```bash
lexio analyze sample.txt
lexio analyze sample.txt --top 20
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
lexio stopwords --no-custom               # hide your ~/.lexio/stopwords.txt
```

### Including stopwords

By default, stopwords are filtered out of the ranking and the vocabulary. Include them with `--include-stopwords`:

```bash
lexio analyze sample.txt --include-stopwords
```

---

## Commands

| Command | Description |
|---|---|
| `analyze <file>` | Full lexiometric analysis: statistics table plus the top words with bars |
| `top-words <file>` | Rank the most frequent words |
| `vocabulary <file>` | List all unique words |
| `freq <file> <word>` | Check the frequency of a specific word |
| `stopwords` | List the stopwords in use |
| `version` | Show version |

### Options

Options belong to each command, they are not global:

| Option | Short | Commands | Default | Description |
|---|---|---|---|---|
| `--top` | `-t` | `analyze` | `10` | Number of top words to display |
| `--count` | `-n` | `top-words` | `10` | Number of words to display |
| `--min-length` | `-m` | `analyze`, `top-words`, `vocabulary` | `3` | Minimum word length to include |
| `--include-stopwords` | | `analyze`, `top-words`, `vocabulary` | off | Keep stopwords in the results |
| `--sort` | `-s` | `vocabulary` | `alpha` | Sort by `alpha` or `freq` |
| `--lang` | `-l` | `stopwords` | `all` | Language to list: `en`, `pt` or `all` |
| `--custom` / `--no-custom` | | `stopwords` | `--custom` | Show or hide your custom stopwords |

---

## Configuration

### Custom stopwords

Create `~/.lexio/stopwords.txt` to add domain-specific words to filter, one per line (lines starting with `#` are comments):

```
# Custom stopwords
algorithm
framework
repository
```

The custom list merges with the built-in stopwords automatically.

---

## Author

[Hugolelis](https://github.com/Hugolelis)

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.
