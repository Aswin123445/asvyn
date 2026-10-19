from fastapi import APIRouter

from app.services.ingestion.service import ingest_knowledge


router = APIRouter(prefix="/api/v1/knowledge", tags=["knowledge"])


@router.post("/ingest")
def start_knowledge_ingestion():
    return ingest_knowledge()