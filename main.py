from typing import Union

from fastapi import FastAPI
import json
from utils import *

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get(f"/stt")
async def read_root():
    return {"message": f"This is the language: {LANGUAGE_CODE}"}