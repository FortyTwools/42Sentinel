from fastapi import FastAPI
from app.api.v1.ft_users import router as raw_router
from app.api.v1.health import router as health_router
from app.api.v1.processed_users import router as processed_router
from app.api.v1.db import router as db_router

app = FastAPI(title="42Sentinel")

app.include_router(health_router, prefix="/api/v1")
app.include_router(raw_router, prefix="/api/v1")
app.include_router(processed_router, prefix="/api/v1")
app.include_router(db_router, prefix="/api/v1/db")
