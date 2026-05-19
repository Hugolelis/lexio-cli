import re
from collections import Counter
from pathlib import Path

from src.helpers.errors import FileNotFound, InvalidFile
from src.helpers.stopwords import get_all_stopwords
from src.services.readers import SUPPORTED_EXTENSIONS, read_file


class LexioResult:
    """Holds the result of a lexiometric analysis."""

    def __init__(
        self,
        filepath: str,
        total_words: int,
        unique_words: int,
        word_freq: Counter,
        sentence_count: int,
        paragraph_count: int,
        avg_word_length: float,
        type_token_ratio: float,
        hapax_legomena: int,
        dis_legomena: int,
    ):
        self.filepath = filepath
        self.total_words = total_words
        self.unique_words = unique_words
        self.word_freq = word_freq
        self.sentence_count = sentence_count
        self.paragraph_count = paragraph_count
        self.avg_word_length = avg_word_length
        self.type_token_ratio = type_token_ratio
        self.hapax_legomena = hapax_legomena
        self.dis_legomena = dis_legomena

    def top_words(
        self,
        n: int = 10,
        exclude_stopwords: bool = True,
        min_length: int = 0,
        stopwords: set[str] | None = None,
    ) -> list[tuple[str, int]]:
        freq = self.word_freq
        if exclude_stopwords:
            sw = stopwords if stopwords is not None else get_all_stopwords()
            freq = Counter({w: c for w, c in freq.items() if w not in sw})
        if min_length > 0:
            freq = Counter({w: c for w, c in freq.items() if len(w) >= min_length})
        return freq.most_common(n)

    def vocabulary(
        self,
        exclude_stopwords: bool = True,
        min_length: int = 0,
        stopwords: set[str] | None = None,
    ) -> list[str]:
        words = set(self.word_freq.keys())
        if exclude_stopwords:
            sw = stopwords if stopwords is not None else get_all_stopwords()
            words = {w for w in words if w not in sw}
        if min_length > 0:
            words = {w for w in words if len(w) >= min_length}
        return sorted(words)


class Analyzer:
    """Performs lexiometric analysis on text, PDF, and DOCX files."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self._validate_file()

    def _validate_file(self) -> None:
        if not self.filepath.exists():
            raise FileNotFound(f"File not found: {self.filepath}")
        if not self.filepath.is_file():
            raise InvalidFile(f"Not a file: {self.filepath}")
        if self.filepath.stat().st_size == 0:
            raise InvalidFile(f"File is empty: {self.filepath}")
        if self.filepath.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise InvalidFile(
                f"Unsupported file type: {self.filepath.suffix}. "
                f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
            )

    def _read_text(self) -> str:
        result = read_file(self.filepath)
        self._paragraph_count = result.paragraph_count
        return result.text

    def _tokenize(self, text: str) -> list[str]:
        return re.findall(r"[a-zA-Z\u00C0-\u024F']+", text.lower())

    def _count_sentences(self, text: str) -> int:
        sentences = re.split(r"[.!?]+", text)
        return len([s for s in sentences if s.strip()])

    def analyze(self) -> LexioResult:
        text = self._read_text()
        words = self._tokenize(text)

        total_words = len(words)
        word_freq = Counter(words)
        unique_words = len(word_freq)

        sentence_count = self._count_sentences(text)
        paragraph_count = self._paragraph_count

        avg_word_length = sum(len(w) for w in words) / total_words if total_words else 0
        type_token_ratio = unique_words / total_words if total_words else 0

        hapax_legomena = sum(1 for c in word_freq.values() if c == 1)
        dis_legomena = sum(1 for c in word_freq.values() if c == 2)

        return LexioResult(
            filepath=str(self.filepath),
            total_words=total_words,
            unique_words=unique_words,
            word_freq=word_freq,
            sentence_count=sentence_count,
            paragraph_count=paragraph_count,
            avg_word_length=round(avg_word_length, 2),
            type_token_ratio=round(type_token_ratio, 4),
            hapax_legomena=hapax_legomena,
            dis_legomena=dis_legomena,
        )
