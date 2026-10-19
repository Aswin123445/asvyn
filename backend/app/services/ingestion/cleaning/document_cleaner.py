import re
import unicodedata
from dataclasses import replace

from app.schemas.document import Document


def clean_document(document: Document) -> Document:
    """Return a cleaned copy, raising ValueError if cleaning empties the content."""
    content = document.page_content.replace("\r\n", "\n").replace("\r", "\n")
    content = "".join(
        character
        for character in content
        if character in "\n\t" or unicodedata.category(character) != "Cc"
    )
    content = re.sub(r"\n{3,}", "\n\n", content).strip()

    if not content:
        raise ValueError("Document content is empty after cleaning")

    return replace(document, page_content=content)


def clean_documents(documents: list[Document]) -> list[Document]:
    return [clean_document(document) for document in documents]