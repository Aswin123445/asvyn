from fastapi import FastAPI

from app.api.v1.endpoints.knowledge import router as knowledge_router

app = FastAPI(title="Asvyn")
app.include_router(knowledge_router)