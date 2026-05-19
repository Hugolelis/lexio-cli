class LexioError(Exception):
    """Base exception for Lexio."""

    pass


class FileNotFound(LexioError):
    """Raised when a file is not found."""

    pass


class InvalidFile(LexioError):
    """Raised when a file is invalid or unreadable."""

    pass
