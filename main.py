from fastapi import FastAPI
app = FastAPI(title="Fellaride API")
@app.get("/")
def root():
    return {"message": " Fellaride API is running successfully! "}
@app.get("/health")
def health_check():
    return {"status": "ok"}
    