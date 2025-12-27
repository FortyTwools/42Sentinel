from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    print("debug")
    return {"status": "healthy"}
