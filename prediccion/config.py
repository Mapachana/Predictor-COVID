import sys
import os
from dotenv import load_dotenv
from dotenv.main import find_dotenv

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')

class Config:
    def __init__(self):
        load_dotenv(find_dotenv())
        
        self.FORMAT = os.getenv('FORMAT')
        self.LOGFILE = os.getenv('LOGFILE')
        path = os.getenv('LOGFOLDER')
        existe = os.path.exists(path)
        if not existe:
            os.mkdir(path)
        self.LEVEL = os.getenv('LEVEL')
        