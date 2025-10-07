from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"status": "ok"}
