from fastapi import FastAPI
from pydantic import BaseModel
from database import db

app = FastAPI()

# ------------------- Models -------------------
class User(BaseModel):
    name: str
    age: int

# ------------------- Routes -------------------

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/users")
async def create_user(user: User):
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id), "message": "User created"}

@app.get("/users")
async def get_users():
    users = []
    async for index, user in enumerate(db.users.find(), start=1):
        users.append({
            "id": index,               # เปลี่ยน _id เป็นเลขลำดับ
            "name": user["name"],
            "age": user["age"]
        })
    return users
