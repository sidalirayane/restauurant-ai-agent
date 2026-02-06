from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(title="Restaurant AI Agent")

app.include_router(chat_router)

@app.get("/")
def health():
    return {"status": "ok"}
