from sqlalchemy.orm import Session
from app.schemas.FtUsers import FtUser
from sqlalchemy.exc import ProgrammingError
from fastapi import HTTPException

def get_trimmed_user(data: dict) -> FtUser:
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
    users = []
    for user in raw:
        users.append(get_trimmed_user(user))
    db.add_all(users)
    db.commit()
    return len(users)


def retrieve(db: Session) -> list[dict]:
    try:
        users = db.query(FtUser).all()
        return users
    except ProgrammingError:
        raise HTTPException(status_code=404, detail="ft_users table does not exist")