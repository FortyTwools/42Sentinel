from fastapi import APIRouter
from app.services.fetch import fetchUsers

router = APIRouter()

@router.post("/fetch/users")
def fetch_users(campus):
	return {"token": fetchUsers(campus=campus)}


@router.post("/fetch/evaluations")
def fetch_evaluations():
	pass
