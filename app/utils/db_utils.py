from starlette.requests import Request


# DB接続のセッションを各エンドポイントの関数に渡す
def get_db(request: Request):
    return request.state.db