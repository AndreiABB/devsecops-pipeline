from fastapi import FastAPI

app = FastAPI(title="DevSecOps API")

@app.get("/")
def root():
    return {"message": "API funcionando correctamente v2"}

@app.get("/health")
def health():
    return {"status": "ok"}
