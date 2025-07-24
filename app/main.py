from fastapi import FastAPI
from app import router
from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Virtual properties API")
add_pagination(app)

app.include_router(router)

@app.get("/")
def main():
    return {"message":"Hello world"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)