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

from models import Logo
from models import Info

app = FastAPI(
    title='Logo service',
    version='0.0.1',
    description='This is a sample service, that provides logo images.\n',
    servers=[{'url': 'http://localhost:8000/logo-service'}],
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

keycloak_realm = "http://192.168.100.14:8090/realms/microservices"

keycloak_config = KeycloakConfiguration(
     url="http://192.168.100.14:8090/",
     realm="microservices",
     client_id="microservices",
     client_secret="microservices",
)

setup_keycloak_middleware(
     app,
     keycloak_configuration=keycloak_config,
)

data = [{"name": "starwit",
         "creator": "Markus",
         "imageUri": "resources/starwit.png"},
        {"name": "starwit-bw",
         "creator": "Markus",
         "imageUri": "resources/starwit-bw.png"}]

contextPathBase = "/logo-service"

# for Docker paths
baseImagePath = pathlib.Path(__file__).parent.resolve()

@app.get(contextPathBase + '/info', response_model=None)
def get_info() -> Info:
    info = Info()
    info.generation_date = datetime.now()
    info.systemDescription = "a sample service"
    info.apiVersion = "0.0.1"
    return info

@app.get(contextPathBase + '/logo/all', response_model=List[Logo])
def get_all_logos() -> List[Logo]:
    result = []
    for idx, d in enumerate(data):
        l = Logo()
        l.id = idx
        l.name = d['name']
        l.creator = d['creator']
        l.imageUri = d['imageUri']
        result.append(l)
    return result

@app.get(contextPathBase + '/logo/{id}', response_model=Logo)
def get_logo_by_id(id: int) -> Logo:
    d = data[id]
    l = Logo()
    l.id = id
    l.name = d['name']
    l.creator = d['creator']
    l.imageUri = d['imageUri']
    return l

@app.get(contextPathBase + '/logo/image/{id}', response_model=bytes)
def get_logo_image(id: int) -> bytes:
    imagePath = str(baseImagePath) + "/" + data[id]['imageUri']
    fr = FileResponse(imagePath)
    return fr

@app.get(contextPathBase + "/private")
def get_private():
    return {"message": "This endpoint is private"}

@app.get(contextPathBase + "/admin")
def get_private():
    return {"message": "Admin only"}

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)