from fastapi import APIRouter, Depends, status
from app.services.fetch import fetch_ft_users
from app.db.session import get_db
from app.core.config import settings
from sqlalchemy.orm import Session
from app.services.ft_users import trim_and_insert, retrieve

router = APIRouter()

@router.post("/fetch/users", status_code=status.HTTP_201_CREATED)
def fetch_users(db: Session = Depends(get_db)):
    raw = fetch_ft_users(settings.FT_CAMPUS)
    inserted_count = trim_and_insert(raw, db)
    return {
        "status": "success",
        "message": f"Succesfully fetched and inserted {inserted_count} users"
    }


@router.get("/fetch/users", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = retrieve(db)
    return {
        "status": "success",
        "message": "SELECT * FROM ft_users",
        "data": users
    }


@router.post("/fetch/evaluations")
def fetch_evaluations():
    pass
