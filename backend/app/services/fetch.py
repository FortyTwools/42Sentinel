from app.core.config import settings
import requests
import time

_token_cache = {
    "access_token": None,
    "expires_at": 0,
}

def getToken() -> str:
    """Return a valid 42API token, fetching a new one if expired."""
    now = int(time.time())
    if _token_cache["access_token"] and _token_cache["expires_at"] > now:
        return _token_cache["access_token"]

    response = requests.post(
        f"{settings.FT_API_BASE_URL}/oauth/token",
        data={
            "grant_type": "client_credentials",
            "client_id": settings.FT_API_UID,
            "client_secret": settings.FT_API_SECRET,
        },
    )
    data = response.json()
    _token_cache["access_token"] = data["access_token"]
    _token_cache["expires_at"] = now + data.get("expires_in", 3600) - 10
    return _token_cache["access_token"]

def fetchUsers(campus: int):
    token = getToken()
    if not campus or not token:
        return
    return token
    
