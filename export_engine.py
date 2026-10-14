"""Export engine for report file generation."""


def export_markdown(report: str) -> bytes:
    """Encode Markdown report as UTF-8 bytes for download."""
    return report.encode("utf-8")
