from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    print("debug")
    return {"status": "healthy"}
