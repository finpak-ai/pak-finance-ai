from fastapi import FastAPI

app = FastAPI(title="Finance App API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
