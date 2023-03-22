from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worlddd"}

@app.get("/callname/{name}")
def read_item(name: str = None):
    return {"hello": name}

@app.post("/callname/")
def read_item(name: str = None):
    return {"hello": name}

handler = Mangum(app)
