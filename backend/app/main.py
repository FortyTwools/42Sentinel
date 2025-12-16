from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Uvicorn": "I'm alive"}


@app.get("/health")
def health_check():
    print("debug")
    return {"status": "healthy"}