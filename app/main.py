from fastapi import FastAPI
from app.routers import router_files, router_users

app = FastAPI()

app.include_router(router_files.router)
app.include_router(router_users.router)
