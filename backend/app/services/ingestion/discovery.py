from pathlib import Path
from typing import Optional


_KNOWLEDGE_DIR = Path(__file__).resolve().parents[3] / "knowledge"


def discover_markdown_files(knowledge_dir: Optional[Path] = None) -> list[Path]:
    """Return sorted paths to Markdown files under the knowledge directory."""
    root = (knowledge_dir or _KNOWLEDGE_DIR).resolve()
    return sorted(path for path in root.rglob("*.md") if path.is_file())