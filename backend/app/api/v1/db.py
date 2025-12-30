from fastapi import APIRouter, Depends, status
from app.db.session import get_db
from app.schemas import FtUser, Project, ProcessedUser

router = APIRouter()

#this file is for dev purposes, to be removed later (or access with permission check)
@router.get("/ft_users", status_code=status.HTTP_200_OK)
def get_db_ft_users(Session = Depends(get_db)):
    users = Session.query(FtUser).all()
    return {
        "status": "success",
        "message": "SELECT * FROM ft_users",
        "data": users
    }

@router.get("/projects", status_code=status.HTTP_200_OK)
def get_db_projects(Session = Depends(get_db)):
    projects = Session.query(Project).all()
    return {
        "status": "success",
        "message": "SELECT * FROM projects",
        "data": projects
    }

@router.get("/processed", status_code=status.HTTP_200_OK)
def get_db_processed(Session = Depends(get_db)):
    processed = Session.query(ProcessedUser).all()
    return {
        "status": "success",
        "message": "SELECT * FROM ProcessedUsers",
        "data": processed
    }