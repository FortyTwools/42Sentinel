from sqlalchemy.orm import Session
from app.schemas import Project
from app.services.fetch import fetch_project

def get_project(p_id: int, db: Session) -> Project:
    project = db.query(Project).filter(Project.id == p_id).first()
    if project: return project

    project_json = fetch_project(p_id)
    project = Project(
        id=p_id,
        name=project_json['name'],
        cursus=project_json['cursus'][0]['name']
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
