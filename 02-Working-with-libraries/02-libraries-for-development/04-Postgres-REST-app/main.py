from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import Club
from models import Info

import database.postgres as db

app = FastAPI(
    title='Football service',
    version='0.0.1',
    description='This is a sample service, that football data.\n',
    servers=[{'url': 'http://localhost:8080/v0'}],
)

contextPathBase = "/football"

# for Docker paths
baseImagePath = pathlib.Path(__file__).parent.resolve()

@app.get(contextPathBase + '/info', response_model=None)
def get_info() -> Info:
    info = Info()
    info.generation_date = datetime.now()
    info.systemDescription = "a sample service"
    info.apiVersion = "0.0.1"
    return info

@app.get(contextPathBase + '/clubs', response_model=None)
def get_info() -> List[Club]:
    result = []
    clubs = db.get_all_clubs()
    for idx,c in enumerate(clubs):
        club = Club()
        club.id = c[0]
        club.name = c[1]
        club.league = c[2]
        result.append(club)
    return result

if __name__ == '__main__':
    db.connect()
    uvicorn.run('main:app', host="0.0.0.0", port=8000)