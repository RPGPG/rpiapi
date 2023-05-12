from fastapi import FastAPI, Form
from pydantic import BaseModel
from tabulate import tabulate
from fastapi.responses import HTMLResponse, PlainTextResponse
import pandas as pd
from pydantic import BaseSettings

import os
import datetime

from cred import user_data


class Settings(BaseSettings):
    openapi_url: str = ""


settings = Settings()
app = FastAPI(openapi_url=settings.openapi_url)


class Input(BaseModel):
    username: str
    password: str
    raspberry_temp: float
    room_temp: float
    humidity: int
    timestamp: int


@app.post("/input/")
async def insert_data(inp: Input):
    if inp.username == user_data["username"] and inp.password == user_data["password"]:
        df = pd.DataFrame({"timestamp": datetime.datetime.fromtimestamp(inp.timestamp),
                        "raspberry_temp": inp.raspberry_temp,
                        "room_temp": inp.room_temp,
                        "humidity": inp.humidity}, index=[0])
        if os.path.isfile("data/data.csv"):
            df.to_csv("data/data.csv", header=False, mode="a", index=False)
        else:
            df.to_csv("data/data.csv", index=False)
        return {"status": "ok"}
    else:
        return {"status": "error"}

@app.get("/get_data/", response_class=HTMLResponse)
async def get_data():
    try:
        df = pd.read_csv("data/data.csv")
        df.set_index("timestamp", inplace=True)
    except FileNotFoundError:
        return "no data"
    return tabulate(df, headers='keys', tablefmt='html')

@app.get("/get_data_raw/", response_class=PlainTextResponse)
async def get_data_raw():
    try:
        df = pd.read_csv("data/data.csv")
        df.set_index("timestamp", inplace=True)
    except FileNotFoundError:
        return "no data"
    return tabulate(df, headers='keys', tablefmt='pretty')
