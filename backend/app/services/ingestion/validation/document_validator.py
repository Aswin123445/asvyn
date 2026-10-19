from typing import Optional, TypedDict

from app.schemas.document import Document


MIN_CONTENT_LENGTH = 50


class ValidationError(TypedDict):
    source: Optional[str]
    reasons: list[str]


def _get_source(document: object) -> Optional[str]:
    try:
        metadata = getattr(document, "metadata", None)
        if isinstance(metadata, dict):
            source = metadata.get("source")
            if isinstance(source, str) and source.strip():
                return source
    except Exception:
        pass
    return None


def _validate_document(document: object) -> list[str]:
    if not isinstance(document, Document):
        return ["item is not an instance of the internal Document model"]

    reasons = []

    try:
        page_content = document.page_content
    except Exception:
        page_content = None
        reasons.append("page_content could not be read")

    if not isinstance(page_content, str):
        if "page_content could not be read" not in reasons:
            reasons.append("page_content must be a string")
    else:
        trimmed_content = page_content.strip()
        if not trimmed_content:
            reasons.append("page_content must not be empty or whitespace-only")
        elif len(trimmed_content) < MIN_CONTENT_LENGTH:
            reasons.append(
                f"page_content must contain at least {MIN_CONTENT_LENGTH} "
                "characters after trimming whitespace"
            )

    try:
        metadata = document.metadata
    except Exception:
        reasons.append("metadata could not be read")
        return reasons

    if not isinstance(metadata, dict):
        reasons.append("metadata must be a dictionary")
        return reasons

    try:
        source = metadata.get("source")
        if not isinstance(source, str) or not source.strip():
            reasons.append("metadata['source'] must be a non-empty string")

        if "category" in metadata:
            category = metadata["category"]
            if not isinstance(category, str) or not category.strip():
                reasons.append(
                    "metadata['category'] must be a non-empty string when present"
                )
    except Exception:
        reasons.append("metadata fields could not be inspected")

    return reasons


def validate_documents(
    documents: list[object],
) -> tuple[list[Document], list[ValidationError]]:
    valid_documents = []
    validation_errors = []

    for document in documents:
        try:
            reasons = _validate_document(document)
        except Exception as error:
            reasons = [f"validation failed unexpectedly ({type(error).__name__})"]

        if reasons:
            validation_errors.append(
                {"source": _get_source(document), "reasons": reasons}
            )
        else:
            valid_documents.append(document)

    return valid_documents, validation_errors