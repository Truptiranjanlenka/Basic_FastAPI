from fastapi import FastAPI

app=FastAPI()

@app.get("/")


def root(fast_name: str, last_name: str):
    if fast_name.isalpha() and last_name.isalpha():
        full_name = fast_name.title() + " " + last_name.title()
        return full_name
    else:
        a=("Please input character only")
        return a
