from time import time
from fastapi import APIRouter, Depends, status, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas import FtUser, ProcessedUser
from app.services.ft_users import retrieve_user_from_id, retrieve_user_from_intra
from app.services.processed_users import fetch_and_insert_raw_processed_user, insert_processed_user, build_processed_from_raw, format_data, is_processed_fresh

UPDATE_FRAME = 60 * 60 * 24 * 3

router = APIRouter()

@router.get("/processed/intra/{name}", status_code=status.HTTP_200_OK)
def get_user_intra_name(name: str | int, Session = Depends(get_db)):
    return get_processed_from_user(retrieve_user_from_intra(name, Session), Session)


@router.get("/processed/id/{id}", status_code=status.HTTP_200_OK)
def get_user_intra_id(id: str | int, Session = Depends(get_db)):
    return get_processed_from_user(retrieve_user_from_id(id, Session), Session)


def get_processed_from_user(user: FtUser, db: Session):
    if not user:
        raise HTTPException(status_code=404, detail="user not found from the key provided")

    if user.processed and is_processed_fresh(user.processed, UPDATE_FRAME):
        processed = user.processed
        build_processed_from_raw(user.id, db)
    else:
        fetch_and_insert_raw_processed_user(user.id, db)
        # processed = db.query(ProcessedUser).filter(ProcessedUser.id == id).first() # remove later pls
        build_processed_from_raw(user.id, db)
        # insert_processed_user(processed, db)
    return {
        "status": "success",
        "message": "here's your user",
        "data": format_data(processed)
    }

    #find user in ft_users
    #if link exists && processed.updated_at() < 3 days from now()
    #	processed = ft_users.processed
    #else
    #	processed = fetch_processed_user()