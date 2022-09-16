# using standard data type to validate the input

from fastapi import FastAPI

app=FastAPI()

@app.get("/items/{id}")

async def root(id:int):
    return {"item_id": id}