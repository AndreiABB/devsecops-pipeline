from fastapi import FastAPI

app = FastAPI(title="DevSecOps API")

@app.get("/")
def root():
    return {"message": "API funcionando correctamente v3"}

@app.get("/health")
def health():
    return {"status": "ok"}
