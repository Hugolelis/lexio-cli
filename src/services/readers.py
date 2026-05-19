import re
from dataclasses import dataclass
from pathlib import Path

import fitz
import docx

from src.helpers.errors import FileNotFound, InvalidFile

SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


@dataclass
class ReadResult:
    text: str
    paragraph_count: int


def read_txt(path: Path) -> ReadResult:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise InvalidFile(f"File is not a valid text file: {path}")

    paragraphs = re.split(r"\n\s*\n", text)
    paragraph_count = len([p for p in paragraphs if p.strip()])
    return ReadResult(text=text, paragraph_count=paragraph_count)


def read_pdf(path: Path) -> ReadResult:
    try:
        doc = fitz.open(path)
        text_parts = []
        paragraph_count = 0

        for page in doc:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if block.get("type") == 0:
                    paragraph_count += 1
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            text_parts.append(span.get("text", ""))
                    text_parts.append("\n")
            text_parts.append("\n")

        doc.close()
        return ReadResult(text="\n".join(text_parts), paragraph_count=paragraph_count)
    except Exception as e:
        raise InvalidFile(f"Failed to read PDF: {e}")


def read_docx(path: Path) -> ReadResult:
    try:
        doc = docx.Document(path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return ReadResult(
            text="\n\n".join(paragraphs),
            paragraph_count=len(paragraphs),
        )
    except Exception as e:
        raise InvalidFile(f"Failed to read DOCX: {e}")


def read_file(path: Path) -> ReadResult:
    ext = path.suffix.lower()
    if ext == ".txt":
        return read_txt(path)
    elif ext == ".pdf":
        return read_pdf(path)
    elif ext == ".docx":
        return read_docx(path)
    raise InvalidFile(f"Unsupported file type: {ext}")
