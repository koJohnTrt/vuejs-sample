from datetime import datetime

from environs import Env

env = Env()
env.read_env()

YMD = '{:%Y-%m-%d}'.format(datetime.now())

LOG_FILE_PATH  = "logs/{time:YYYY-MM-DD}.log"
LOG_MSG_FORMAT = "[{time:YYYY-MM-DD HH:mm:ss}] {level} {message}"
LOG_LEVEL      = env("LOG_LEVEL")

#SQL_FILE_PATH = "logs/sql_"+YMD+".log"
