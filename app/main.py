from fastapi import FastAPI
from app.api.endpoints import auth

app = FastAPI()
api_prefix = "/api"

app.include_router(auth.auth_router, prefix=api_prefix + "/auth")

@app.get("/")
def main():
    return {"message":"Hello world"}

