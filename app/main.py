from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"status": "ok", "app": "Aplicación: fastapi-multistage"}