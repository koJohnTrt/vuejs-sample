import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from environs import Env

from db import engine, session


from routers import (
    roads
)

env = Env()
env.read_env()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(SessionMiddleware, secret_key="test")


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router登録
app.include_router(roads.router)


# リクエストの都度呼ばれるミドルウェア（DB接続用セッションインスタンス作成）
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = session
    response = await call_next(request)
    request.state.db.close()
    return response

# サーバ起動
if __name__ == '__main__':
    uvicorn.run("main:app",
        host=env("SVR_HOST"),
        port=int(env("SVR_PORT")),
        # reload=env("SVR_RELOAD"),
    )
