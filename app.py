import fastapi as f
import requests as r
from slash import *

app = f.FastAPI() # Run the app with uvicorn app:app --reload

@app.get("/")
def index():
    return {"message": "Hello World. Lets blather!"}

@app.get("/blather")
index()

