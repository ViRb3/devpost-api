import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import api

app = FastAPI(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def hello():
    return 'Hello'

@app.get('/user/{username}')
def user(username: str):
    return api.get_user(username)

@app.get('/project/{project_name}')
def project(project_name: str):
    return api.get_project(project_name)
