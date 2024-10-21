from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import Club
from models import Info

app = FastAPI(
    title='Football service',
    version='0.0.1',
    description='This is a sample service, that football data.\n',
    servers=[{'url': 'http://localhost:8080/v0'}],
)

data = [{"id": 1,
        "name": "FC Bayern Muenchen",
         "league": 1},
        {"id": 2,
        "name": "VfL Wolfsburg",
         "league": 1}]

contextPathBase = "/football"

# for Docker paths
baseImagePath = pathlib.Path(__file__).parent.resolve()

@app.get(contextPathBase + '/info', response_model=Info)
def get_info() -> Info:
    info = Info()
    info.generation_date = datetime.now()
    info.systemDescription = "a sample service"
    info.apiVersion = "0.0.1"
    return info

@app.get(contextPathBase + '/clubs', response_model=None)
def get_info() -> List[Club]:
    result = []
    for idx,c in enumerate(data):
        club = Club()
        club.id = c["id"]
        club.name = c["name"]
        club.league = c["league"]
        result.append(club)
    return result

@app.get(contextPathBase + '/clubs/league/{id}', response_model=None)
def get_info() -> List[Club]:
    result = []
    # TODO
    return result

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)