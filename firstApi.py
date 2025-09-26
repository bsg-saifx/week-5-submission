from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def root():
    return {"message":"pong"}

@app.get("/greet/{name}")
async def greet(name):
    return {"message":f"Hello {name}"}

@app.get("/add")
async def sum(number1 :int, number2 :int):
    return number1+number2

