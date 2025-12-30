from time import time
from fastapi import APIRouter, Depends, status, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas import FtUser, ProcessedUser
from app.services.ft_users import retrieve_user_from_intra
from app.utils.lock import get_lock
from app.services.processed_users import fetch_and_insert_raw_processed_user, build_processed_from_raw, format_data, is_processed_fresh

UPDATE_FRAME = 60 * 60 * 24 * 3

router = APIRouter()

@router.get("/processed/intra/{name}", status_code=status.HTTP_200_OK)
def get_user_intra(name: str | int, Session = Depends(get_db)):
    return {
        "status": "success",
        "message": "here's your user",
        "data": format_data(get_processed_from_user(retrieve_user_from_intra(name, Session), Session))
    }


@router.get("/evaluated/{name}", status_code=status.HTTP_200_OK)
def get_evaluator_data(name: str | int, Session = Depends(get_db)):
    data = get_processed_from_user(retrieve_user_from_intra(name, Session), Session)
    return {
        "status": "success",
        "message": "here's your user",
        "data": {
            "avg_grade": data.evaluated_avg_grade,
            "avg_time": data.evaluated_avg_time / 60,
            "total": data.evaluated_total_evals,
            "top": data.evaluated_top
        }
    }
            # format_data(get_processed_from_user(retrieve_user_from_intra(name, Session), Session))


@router.get("/evaluator/{intra}", status_code=status.HTTP_200_OK)
def get_evaluator_data(name: str | int, Session = Depends(get_db)):
    get_processed_from_user(retrieve_user_from_intra(name, Session), Session)
    return 


@router.get("/dashboard/{intra}", status_code=status.HTTP_200_OK)
def get_evaluator_data(name: str | int, Session = Depends(get_db)):
    get_processed_from_user(retrieve_user_from_intra(name, Session), Session)
    return 


@router.get("/profile/{intra}", status_code=status.HTTP_200_OK)
def get_evaluator_data(name: str | int, Session = Depends(get_db)):
    get_processed_from_user(retrieve_user_from_intra(name, Session), Session)
    return 



def get_processed_from_user(user: FtUser, db: Session) -> ProcessedUser:
    if not user:
        raise HTTPException(status_code=404, detail="user not found from the key provided")

    lock = get_lock(user.id)

    with lock:
        if user.processed and is_processed_fresh(user.processed, UPDATE_FRAME):
            processed = user.processed
            build_processed_from_raw(user.id, db)
        else:
            fetch_and_insert_raw_processed_user(user.id, db)
            build_processed_from_raw(user.id, db)
            processed = user.processed
    return processed
