import json
import os

from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, status
from starlette.requests import Request
from sqlalchemy.orm import Session
from typing import List

import cruds.roads as crud
from utils.db_utils import get_db
from utils.validation_handling import validation_check
import configs.messages as msg
from schemas.roads import RoadsSelect
from utils.common_utils import (
    get_excel_data,
    create_excel_from_template,
    create_excel_from_template_openpyxl,
    get_excel_data_openpyxl
)


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/road_search', response_model=List[RoadsSelect], status_code=status.HTTP_200_OK)
@router.get('/road_search', status_code=status.HTTP_200_OK)
async def get_roads_info(request: Request, db: Session = Depends(get_db)):
    response = crud.get_road(db)
    if type(response) == JSONResponse:
        result_data = response.body.decode()
        result_data = json.loads(result_data)
        request.session['error'] = result_data['message']
        response = []
    return response


@router.get('/roads', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
@router.get('/', response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_roads(request: Request, db: Session = Depends(get_db)):
    response = crud.get_road(db)
    if type(response) == JSONResponse:
        result_data = response.body.decode()
        result_data = json.loads(result_data)
        request.session['error'] = result_data['message']
        response = []

    return templates.TemplateResponse("roads/list.html", {"request": request, "roads": response, "menu": "Roads"})


# roads登録
@router.post('/roads', status_code=status.HTTP_200_OK) 
async def insert_to_road(request: Request, data = Depends(get_excel_data_openpyxl), db: Session = Depends(get_db)):
    
    # ファイルアップロードに失敗した場合
    if type(data) == JSONResponse:
        result_data = data.body.decode()
        result_data = json.loads(result_data)
        request.session['reg_error'] = result_data['message']
        # request.session['reg_error'] = "ファイルのアップロードに失敗しました。"
    else:
        validation = validation_check(request, data)

        # バリデーションエラーが発生した場合
        if len(validation) != 0:
            request.session['reg_error'] = list(dict.fromkeys(validation))
        else:
            result = crud.post_road(db, data)
            result_data = result.body.decode()
            result_data = json.loads(result_data)
    
            # 登録処理が失敗した場合
            if result_data['code'] == 'MI0001':
                request.session['success'] = msg.MI0002
            else:
                request.session['reg_error'] = result_data['message']

    return RedirectResponse(url='/roads', status_code=status.HTTP_302_FOUND)



@router.get("/roads_excel_export")
async def get_filelist(db: Session = Depends(get_db)):
    response = crud.get_road(db)
    columns = ["rec_id", "code", "name", "date_from", "date_to"]
    filename = "road_excel.xlsx"

    create_excel_from_template_openpyxl(response, filename, columns)
    download_path = f"{os.getcwd()}/{filename}"
    return FileResponse(download_path, media_type='application/octet-stream',filename=filename)
