from fastapi import FastAPI

app = FastAPI(title="Restaurant AI Agent")

@app.get("/")
def health():
    return {"status": "ok"}
