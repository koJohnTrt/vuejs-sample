import inspect
import textwrap

from fastapi.responses import JSONResponse
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from datetime import date, datetime

import configs.common as comm
import configs.messages as msg
from utils.log_utils import put_error_info
from models.roads import RoadModel


PROGRAM_CODE_PUT = "CPO00010"
PROGRAM_CODE_POST = "CPU00010"

# データ取得
def get_road(db: Session):
    try:
        # データ検索SQL
        query = textwrap.dedent('''\
            SELECT
                REC_ID,
                CODE,
                NAME,
                DATE_FROM,
                DATE_TO
            FROM
                ROADS
            ORDER BY REC_ID
        ''')

        # SQLの実行
        result = db.execute(text(query)).fetchall()

        return result

    # DBの接続エラー
    except OperationalError as err:
        code = "ME0001"
        message = msg.ME0001
        other = str(err)
        frame = inspect.currentframe()
        put_error_info(__file__,inspect.getframeinfo(frame).function, inspect.getframeinfo(frame).lineno, code, message, other)

        response = { 'code': code, 'message': message }
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=response
        )

    # DB query エラー
    except Exception as err:
        code = "ME0020"
        message = msg.ME0020
        other = str(err)
        frame = inspect.currentframe()
        put_error_info(__file__,inspect.getframeinfo(frame).function, inspect.getframeinfo(frame).lineno, code, message, other)

        response = { 'code': code, 'message': message }
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=response
        )


# データ登録
def post_road(db: Session, data):
    bind_parms = {}
    try:
        # データ登録SQl
        query = textwrap.dedent('''\
            INSERT INTO
                ROADS
                (CREATE_DATE,
                CREATE_CODE,
                CREATE_PGM,
                UPDATE_DATE,
                UPDATE_CODE,
                UPDATE_PGM,
                REC_ID,
                CODE,
                NAME,
                DATE_FROM,
                DATE_TO)
            VALUES
                (now(),
                :create_code,
                :create_pgm,
                now(),
                :update_code,
                :update_pgm,
                :rec_id,
                :code,
                :name,
                :date_from,
                :date_from)
        ''')

        for road in data:
        # データ設定
            bind_parms={
                "create_code": comm.AUTHOR_CODE,
                "create_pgm": PROGRAM_CODE_POST,
                "update_code": comm.AUTHOR_CODE,
                "update_pgm": PROGRAM_CODE_POST,
                "rec_id": road['rec_id'],
                "code": road['code'],
                "name": road['name'],
                "date_from": road['date_from'],
                "date_to": road['date_to']
            }

            # SQLの実行
            db.execute(text(query), bind_parms)

    # DB接続エラー
    except OperationalError as err:
        code = "ME0001"
        message = msg.ME0001
        other = str(err)
        frame = inspect.currentframe()
        put_error_info(__file__,inspect.getframeinfo(frame).function, inspect.getframeinfo(frame).lineno, code, message, other)

        response = { 'code': code, 'message': message }
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=response
        )

    # DB query エラー
    except Exception as err:
        code = "ME0021"
        message = msg.ME0021
        other = str(err)
        frame = inspect.currentframe()
        put_error_info(__file__,inspect.getframeinfo(frame).function, inspect.getframeinfo(frame).lineno, code, message, other)

        db.rollback()

        response = { 'code': code, 'message': message }
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=response
        )

    db.commit()
    response = { 'code': "MI0001", 'message': msg.MI0001 }
    return JSONResponse(
        content=response
    )