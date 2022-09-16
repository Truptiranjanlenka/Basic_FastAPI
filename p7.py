# retrive the data a specific user_id

from fastapi import FastAPI

app= FastAPI()

@app.get("/user/{user_id}")

async def user_read():
    return {"user_id": "this is the current user"}

@app.get("/user/{user_item}")
async  def user_item(user_item: str):
    return {"user_item": user_item}


# conclusoin is if we defind same type of path then route always take 1st function data