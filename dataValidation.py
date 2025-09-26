from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, EmailStr

app = FastAPI()

class User(BaseModel):
    name : str
    email : EmailStr
    age : PositiveInt

@app.post("/user")
async def create_user(user: User):
    return {"Message" : f"User created user {user}"}

