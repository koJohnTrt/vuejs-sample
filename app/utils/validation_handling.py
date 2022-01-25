
from datetime import datetime

from configs import messages
from utils.log_utils import put_error_info

def validation_check(request, data):
    err_messages = []
    parms = {}

    for i in data:
        for key, val in i.items():
            if key == 'code':
                if(len(str(i['code'])) < 1 or len(str(i['code'])) > 4):
                    err_messages.append(messages.ME0014 + " (" + key + ")")

            if key == 'name':
                if(len(str(i['name'])) < 1 or len(str(i['name'])) > 20):
                    err_messages.append(messages.ME0014 + " (" + key + ")")

            if key == 'date_from':
                if not (isinstance(val, datetime)):
                    err_messages.append(messages.ME0013 + " (" + key + ")")

            if key == 'date_to':
                if not (isinstance(val, datetime)):
                    err_messages.append(messages.ME0013 + " (" + key + ")")

    # エラーが発生したURLリファラーを取得する
    file_url = str(request.url).split('/')
    file = file_url[3].split('?')
    filename = ".\\app\\routers\\" + file[0] + ".py"

    # GET, POST, PUT, DELETEだけが取得できます。
    method = request.method
    
    if len(err_messages) != 0:
        # ログにエラー情報を保存する
        put_error_info(filename, method, "", "",  err_messages, parms)

    return err_messages
