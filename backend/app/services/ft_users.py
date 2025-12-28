from sqlalchemy.orm import Session
from app.schemas.ft_users import ft_user

def get_trimmed_user(data: dict) -> ft_user:
    return ft_user(
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
    users = db.query(ft_user).all()
    return users
    
