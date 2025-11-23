# information log krne ke liye
import logging
import os
from datetime import datetime

'''

Logging Levels in Python :
CRITICAL
ERROR
WARNING
INFO
DEBUG
NOTSET

Small is Debug
Info is General Information
Warning is something to be cautious about
Error is when code fails
Critical is fatal error


'''

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,  # getcwd() means current working directory
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s- %(message)s ', # s for string printing and d for digit printing 
    level=logging.INFO,
)