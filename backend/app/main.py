from fastapi import FastAPI
from app.api.v1.ft_users import router as raw_router
from app.api.v1.health import router as health_router

app = FastAPI(title="42Sentinel")

app.include_router(raw_router, prefix="/api/v1/raw")
app.include_router(health_router, prefix="/api/v1")
