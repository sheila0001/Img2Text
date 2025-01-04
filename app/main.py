
import pathlib
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent


app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)  #http get --> will return JSON (javascript object notation) will show to the browser
def home_view(request: Request):

    #this is opening the home.html and turning the content into a string
    return templates.TemplateResponse("home.html", {"request":request})#will expect a string as response because the class is HTML

@app.post("/") #HTPP POST will send data to another app
def home_detail_view():
    return {"hello": "world"}
