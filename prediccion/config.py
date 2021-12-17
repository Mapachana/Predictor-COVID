import sys
import os
import logging
from dotenv import load_dotenv, find_dotenv
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
        os.mkdir(path)
        self.LEVEL = os.getenv('LEVEL')

