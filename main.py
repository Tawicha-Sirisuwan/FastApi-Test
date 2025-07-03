from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return{"message" : "Hello World"}

@app.get('/hello')
def read_hello():
    return {"message": "Hello from FastAPI"}

@app.get('/items/{id}')
def read_item(id: int):
    return {"item_id": id, "message": "This is an item"}