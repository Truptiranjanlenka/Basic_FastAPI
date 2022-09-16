# Path converter

from fastapi import FastAPI

app=FastAPI()

@app.get("/files/{file_path:path}")
async def root(file_path: str):
    return {"file_path_is":file_path}
