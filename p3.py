# use Enum by using class

from enum import Enum
from fastapi import FastAPI

class root(str, Enum):
    ename :"ename"
    Degination:"Degination"     #dought in this session
    Company: "Company "

app=FastAPI()

@app.get("/people/{details}")
async def read_data(details:root):
    if details is root.ename:
        return {"the data is":details}
    elif details is root.Degination:
        return {"the data is":details}
    elif details is root.Company:
        return {"the data is":details}



