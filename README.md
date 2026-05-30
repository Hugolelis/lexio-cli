# Lexio

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-1a1a2e?style=for-the-badge&logo=python&logoColor=white)]()
[![Version](https://img.shields.io/badge/Version-0.1.0-1a1a2e?style=for-the-badge&logoColor=white)]()

</div>

> **Lexio** is a command-line tool for lexiometric analysis of text documents. It extracts statistical insights from `.txt`, `.pdf`, and `.docx` files — including word frequency, vocabulary richness, and readability metrics — with automatic stopword filtering and configurable analysis parameters.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

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

## Installation

```bash
# Clone the repository
git clone https://github.com/Hugolelis/lexio.git
cd lexio

# Install dependencies
pip install -e .
```

---

## Usage

### Basic analysis

```bash
lexio analyze sample.txt
```

Output includes statistics and a ranked list of the most frequent words:

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

## Architecture

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

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.
