from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv('./env', override=True)  # Force reload

title = os.getenv("TEST","TEST")
app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    position: str

users = [{"name":"Hour","age":"23","position":"developer"},{"name":"Nich","age":"21","position":"teacher"}]

@app.get("/")
async def read_root():
    print("haha",title)
    return {"Hello", "World"}

@app.get("/users")
async def get_users():
    return users

@app.get("/users/{user_id}")
async def get_users_detail(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}    

@app.put("/users/{user_id}")
async def update_user(user_id: int, users: User):
    return {"user_name": users.name, "user_id": user_id}

@app.get("/say-hi")
async def say_hi(name: str | None = None):
    if name is not None:
        return f"Hello: {name}"
    else:
        return "Hello World"