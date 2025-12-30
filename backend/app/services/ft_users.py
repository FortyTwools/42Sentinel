from sqlalchemy.orm import Session
from app.schemas.FtUsers import FtUser
from sqlalchemy.exc import ProgrammingError
from fastapi import HTTPException

def get_trimmed_user(data: dict) -> FtUser:
    """Builds a FtUser from data (JSON) from 42API"""
    return FtUser(
        id=data["id"],
        name=data["displayname"],
        login=data["login"],

        image_link=data["image"]["link"],
        image_large=data["image"]["versions"].get("large"),
        image_medium=data["image"]["versions"].get("medium"),
        image_small=data["image"]["versions"].get("small"),
        image_micro=data["image"]["versions"].get("micro"),

        staff=data["staff?"],
        active=data["active?"],
    )


def trim_and_insert(raw: list[dict], db: Session) -> int:
    """Gets a raw JSON object from 42API and insert the users in the db correspondingly"""
    users = []
    for user in raw:
        users.append(get_trimmed_user(user))
    db.add_all(users)
    db.commit()
    return len(users)


def retrieve_user_from_intra(intra: str, db: Session) -> list[dict]:
    """SELECT * FROM FtUsers WHERE intra == login"""
    try:
        user = db.query(FtUser).filter(FtUser.login == intra).first()
        return user
    except ProgrammingError:
        raise HTTPException(status_code=404, detail="ft_users table does not exist")


def retrieve_all(db: Session) -> list[dict]:
    """SELECT * FROM FtUsers"""
    try:
        users = db.query(FtUser).all()
        return users
    except ProgrammingError:
        raise HTTPException(status_code=404, detail="ft_users table does not exist")