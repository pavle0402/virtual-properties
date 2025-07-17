from fastapi import FastAPI
from app import router

app = FastAPI(title="Virtual properties API")

app.include_router(router)

@app.get("/")
def main():
    return {"message":"Hello world"}

