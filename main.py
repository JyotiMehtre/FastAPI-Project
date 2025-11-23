from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Jyoti!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/create")
def create_item(data: dict):
    return {"status": "Item received", "data": data}
