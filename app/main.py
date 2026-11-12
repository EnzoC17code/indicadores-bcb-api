from fastapi import FastAPI

app = FastAPI(title="Indicadores BCB API")

@app.get("/")
def raiz():
    return {"status": "ok"}

@app.delete("/")
def raiz():
    return {"status": "deleted"}