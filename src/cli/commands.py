import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from src.services.analyzer import Analyzer
from src.helpers.stopwords import (
    get_all_stopwords,
    CUSTOM_STOPWORDS_PATH,
    _load_custom_stopwords,
    STOP_WORDS_EN_CONJUNCTIONS_CONNECTIVES,
    STOP_WORDS_EN_ARTICLES_PRONOUNS,
    STOP_WORDS_EN_PREPOSITIONS,
    STOP_WORDS_EN_VERBS_AUXILIARY,
    STOP_WORDS_EN_ADVERBS_OTHERS,
    STOP_WORDS_PT,
)
from src.helpers.errors import LexioError

app = typer.Typer(
    name="lexio",
    help="Lexio - Lexiometric analysis CLI tool",
    add_completion=False,
)
console = Console()


def _handle_error(e: LexioError) -> None:
    console.print(f"[bold red]Error:[/bold red] {e}")
    raise typer.Exit(code=1)


@app.command()
def analyze(
    filepath: str = typer.Argument(..., help="Path to the file (.txt, .pdf, .docx)"),
    top: int = typer.Option(10, "--top", "-t", help="Number of top words to display"),
    include_stopwords: bool = typer.Option(False, "--include-stopwords", help="Include stopwords in results"),
    min_length: int = typer.Option(3, "--min-length", "-m", help="Minimum word length to include"),
):
    """Perform full lexiometric analysis on a text, PDF, or DOCX file."""
    try:
        analyzer = Analyzer(filepath)
        result = analyzer.analyze()
    except LexioError as e:
        _handle_error(e)

    console.print()
    console.print(Panel.fit(
        f"[bold cyan]Lexiometric Analysis[/bold cyan]\n"
        f"File: [bold]{result.filepath}[/bold]",
        border_style="cyan",
    ))
    console.print()

    stats_table = Table(title="Statistics", border_style="green")
    stats_table.add_column("Metric", style="cyan", no_wrap=True)
    stats_table.add_column("Value", style="white", justify="right")

    stats_table.add_row("Total Words", str(result.total_words))
    stats_table.add_row("Unique Words", str(result.unique_words))
    stats_table.add_row("Sentences", str(result.sentence_count))
    stats_table.add_row("Paragraphs", str(result.paragraph_count))
    stats_table.add_row("Avg Word Length", str(result.avg_word_length))
    stats_table.add_row("Type-Token Ratio", str(result.type_token_ratio))
    stats_table.add_row("Hapax Legomena", str(result.hapax_legomena))
    stats_table.add_row("Dis Legomena", str(result.dis_legomena))

    console.print(stats_table)
    console.print()

    top_words = result.top_words(n=top, exclude_stopwords=not include_stopwords, min_length=min_length)
    if top_words:
        freq_table = Table(title=f"Top {top} Words", border_style="magenta")
        freq_table.add_column("Rank", style="cyan", justify="right")
        freq_table.add_column("Word", style="green")
        freq_table.add_column("Frequency", style="white", justify="right")
        freq_table.add_column("Bar", style="yellow")

        max_freq = top_words[0][1] if top_words else 1
        for i, (word, count) in enumerate(top_words, 1):
            bar_len = int((count / max_freq) * 30)
            bar = "█" * bar_len
            freq_table.add_row(str(i), word, str(count), bar)

        console.print(freq_table)

    console.print()


@app.command("top-words")
def top_words(
    filepath: str = typer.Argument(..., help="Path to the file (.txt, .pdf, .docx)"),
    count: int = typer.Option(10, "--count", "-n", help="Number of words to display"),
    include_stopwords: bool = typer.Option(False, "--include-stopwords", help="Include stopwords in results"),
    min_length: int = typer.Option(3, "--min-length", "-m", help="Minimum word length to include"),
):
    """Display the most frequent words in a text, PDF, or DOCX file."""
    try:
        analyzer = Analyzer(filepath)
        result = analyzer.analyze()
    except LexioError as e:
        _handle_error(e)

    words = result.top_words(n=count, exclude_stopwords=not include_stopwords, min_length=min_length)

    console.print()
    console.print(Panel.fit(
        f"[bold cyan]Top {count} Words[/bold cyan] in [bold]{result.filepath}[/bold]",
        border_style="cyan",
    ))
    console.print()

    table = Table(border_style="magenta")
    table.add_column("Rank", style="cyan", justify="right")
    table.add_column("Word", style="green")
    table.add_column("Frequency", style="white", justify="right")

    for i, (word, freq) in enumerate(words, 1):
        table.add_row(str(i), word, str(freq))

    console.print(table)
    console.print()


@app.command("vocabulary")
def vocabulary(
    filepath: str = typer.Argument(..., help="Path to the file (.txt, .pdf, .docx)"),
    include_stopwords: bool = typer.Option(False, "--include-stopwords", help="Include stopwords in results"),
    min_length: int = typer.Option(3, "--min-length", "-m", help="Minimum word length to include"),
    sort: str = typer.Option("alpha", "--sort", "-s", help="Sort by: alpha (alphabetical) or freq (frequency)"),
):
    """Display all unique words in a text, PDF, or DOCX file."""
    try:
        analyzer = Analyzer(filepath)
        result = analyzer.analyze()
    except LexioError as e:
        _handle_error(e)

    words = result.vocabulary(
        exclude_stopwords=not include_stopwords,
        min_length=min_length,
    )

    if sort == "freq":
        words = sorted(words, key=lambda w: result.word_freq[w], reverse=True)

    console.print()
    console.print(Panel.fit(
        f"[bold cyan]Vocabulary[/bold cyan] — [bold]{len(words)}[/bold] unique words in [bold]{result.filepath}[/bold]",
        border_style="cyan",
    ))
    console.print()

    columns = 4
    text = Text()
    for i, word in enumerate(words):
        text.append(f"{word}  ", style="green")
        if (i + 1) % columns == 0:
            text.append("\n")

    console.print(text)
    console.print()


@app.command("freq")
def frequency(
    filepath: str = typer.Argument(..., help="Path to the file (.txt, .pdf, .docx)"),
    word: str = typer.Argument(..., help="Word to search for"),
):
    """Check the frequency of a specific word in a text, PDF, or DOCX file."""
    try:
        analyzer = Analyzer(filepath)
        result = analyzer.analyze()
    except LexioError as e:
        _handle_error(e)

    word_lower = word.lower()
    count = result.word_freq.get(word_lower, 0)

    console.print()
    if count > 0:
        percentage = (count / result.total_words) * 100
        console.print(Panel.fit(
            f"The word [bold green]'{word_lower}'[/bold green] appears "
            f"[bold yellow]{count}[/bold yellow] times "
            f"([bold]{percentage:.2f}%[/bold] of total words)",
            border_style="green",
        ))
    else:
        console.print(Panel.fit(
            f"The word [bold red]'{word_lower}'[/bold red] was not found in the text.",
            border_style="red",
        ))
    console.print()


@app.command()
def stopwords(
    lang: str = typer.Option("all", "--lang", "-l", help="Filter by language: en, pt, or all"),
    custom: bool = typer.Option(True, "--custom/--no-custom", help="Show custom stopwords from ~/.lexio/stopwords.txt"),
):
    """List all stopwords used for filtering."""
    lang_map = {
        "en": {
            "Conjunctions & Connectives": STOP_WORDS_EN_CONJUNCTIONS_CONNECTIVES,
            "Articles & Pronouns": STOP_WORDS_EN_ARTICLES_PRONOUNS,
            "Prepositions": STOP_WORDS_EN_PREPOSITIONS,
            "Verbs (Auxiliary & Common)": STOP_WORDS_EN_VERBS_AUXILIARY,
            "Adverbs & Others": STOP_WORDS_EN_ADVERBS_OTHERS,
        },
        "pt": {
            "Portuguese Stopwords": STOP_WORDS_PT,
        },
    }

    console.print()

    if lang == "all":
        categories = {}
        for lang_key in lang_map:
            categories.update(lang_map[lang_key])
    else:
        if lang not in lang_map:
            console.print(f"[bold red]Error:[/bold red] Unknown language '{lang}'. Use 'en', 'pt', or 'all'.")
            raise typer.Exit(code=1)
        categories = lang_map[lang]

    total = 0
    for category, words in categories.items():
        sorted_words = sorted(words)
        total += len(sorted_words)

        console.print(f"[bold cyan]{category}[/bold cyan] ({len(sorted_words)} words)")

        columns = 5
        text = Text()
        for i, word in enumerate(sorted_words):
            text.append(f"{word}  ", style="dim")
            if (i + 1) % columns == 0:
                text.append("\n")
        console.print(text)
        console.print()

    if custom:
        custom_words = _load_custom_stopwords()
        if custom_words:
            console.print(f"[bold yellow]Custom Stopwords[/bold yellow] ({len(custom_words)} words from {CUSTOM_STOPWORDS_PATH})")
            text = Text()
            for i, word in enumerate(sorted(custom_words)):
                text.append(f"{word}  ", style="yellow")
                if (i + 1) % columns == 0:
                    text.append("\n")
            console.print(text)
            console.print()
            total += len(custom_words)
        else:
            console.print(f"[dim]No custom stopwords found at {CUSTOM_STOPWORDS_PATH}[/dim]")
            console.print()

    console.print(Panel.fit(
        f"[bold]Total: {total}[/bold] stopwords loaded",
        border_style="cyan",
    ))
    console.print()


@app.command()
def version():
    """Show the version."""
    console.print("[bold blue]Lexio v0.1.0[/bold blue]")


if __name__ == "__main__":
    app()
