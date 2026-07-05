import logging

from app.config.settings import settings
from app.routers.auth_router import router as auth_router
from app.routers.health_router import router as health_router
from app.routers.ingest_routers import router as ingest_router
from app.routers.chat_router import router as chat_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.app_name, version="0.0.1", description="Multimodal agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(ingest_router)
app.include_router(chat_router)


logger = logging.getLogger(__name__)

logger.info(
    "Application startup configured",
    extra={
        "app_name": settings.app_name,
        "api_prefix": settings.api_prefix,
        "llm_provider": settings.llm_provider,
        "elastic_search": settings.elasticsearch_index,
    },
)
