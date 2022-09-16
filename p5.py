from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def get_fullname(fast_name: str, age: int):
    result=fast_name.title()+" your age is "+ str(age)
    return result