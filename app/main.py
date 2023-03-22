from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worlddd"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname/")
def write_name(data: dict):
    name = data.get("name")
    return {"hello": name}

handler = Mangum(app)
