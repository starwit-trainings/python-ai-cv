from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi_keycloak_middleware import KeycloakConfiguration, setup_keycloak_middleware

from jwt import PyJWKClient
import jwt
from typing import Annotated

from models import Club
from models import Info

app = FastAPI(
    title='Football service',
    version='0.0.1',
    description='This is a sample service, that football data.\n',
    servers=[{'url': 'http://localhost:8000/football'}],
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

keycloak_realm = "http://192.168.1.211:8090/realms/microservices"

keycloak_config = KeycloakConfiguration(
     url="http://192.168.1.211:8090/",
     realm="microservices",
     client_id="microservices",
     client_secret="microservices",
)

setup_keycloak_middleware(
     app,
     keycloak_configuration=keycloak_config,
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

@app.get(contextPathBase + '/clubs', response_model=List[Club])
def get_info() -> List[Club]:
    result = []
    for idx,c in enumerate(data):
        club = Club()
        club.id = c["id"]
        club.name = c["name"]
        club.league = c["league"]
        result.append(club)
    return result

@app.get(contextPathBase + '/clubs/league/{id}', response_model=List[Club])
def get_info() -> List[Club]:
    result = []
    # TODO
    return result

@app.get(contextPathBase + "/private")
def get_private():
    return {"message": "This endpoint is private"}

@app.get(contextPathBase + "/admin")
def get_private():
    return {"message": "Admin only"}

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)