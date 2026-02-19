from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/lesson", response_class=HTMLResponse)
def web_page():

    user_name = "Jang woon"
    number_1 = 1
    number_2 = 23

    return f"""
    <html>
      <head><title>Home</title></head>
      <body>
        <h1>Hello</h1>
        <p>My name is {user_name}</p>
        <p>{number_1}+{number_2}={number_1+number_2}이다</p>
      </body>
    </html>
    """



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


