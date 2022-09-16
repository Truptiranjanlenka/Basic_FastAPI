from fastapi import FastAPI

app=FastAPI()

@app.get("/items/{id}")

async def show(id):
    return {"item_id":id}