from pathlib import Path
from typing import Optional, Union

from app.schemas.document import Document


FilePath = Union[Path, str]


def _get_category(path: Path) -> Optional[str]:
    parts = path.parts
    for index, part in enumerate(parts[:-1]):
        if part.lower() == "knowledge":
            return parts[index + 1]
    if path.parent.name.lower() != "knowledge":
        return path.parent.name
    return None


def load_document(file_path: FilePath) -> Document:
    path = Path(file_path)
    try:
        page_content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise RuntimeError(f"Could not load Markdown file '{path}': {error}") from error

    metadata = {"source": str(path.resolve())}
    category = _get_category(path.resolve())
    if category is not None:
        metadata["category"] = category

    return Document(page_content=page_content, metadata=metadata)


def load_documents(file_paths: list[FilePath]) -> list[Document]:
    return [load_document(file_path) for file_path in file_paths]