from app.services.ingestion.discovery import discover_markdown_files
from app.services.ingestion.document_loader import load_documents
from app.services.ingestion.validation.document_validator import validate_documents
from app.services.ingestion.cleaning.document_cleaner import clean_documents


def ingest_knowledge():
	paths = discover_markdown_files()
	documents = load_documents(paths)
	valid_documents, validation_errors = validate_documents(documents)
	if validation_errors:
		print(validation_errors)

	cleaned_documents = clean_documents(valid_documents)
	print(cleaned_documents)
	return cleaned_documents
