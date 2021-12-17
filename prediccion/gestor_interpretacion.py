import sys
import os
import logging

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')

import datos as dt
from interpretacion import EstadoSituacion, Interpretacion
import config as config

class GestorInterpretacion:
    '''Clase para gestionar la clase Interpretacion'''
    def __init__(self, fichero):
        '''Constructor de la clase GestorInterpretacion, que gestiona la clase Interpretacion'''
        # Instancio la configuracion para configurar el logger
        self.config = config.Config()

        path = self.config.LOGFOLDER
        existe = os.path.exists(path)
        if not existe:
            os.mkdir(path)
        path = self.config.LOGFILE
        existe = os.path.isfile(self.config.LOGFILE)
        if not existe:
            open(self.config.LOGFILE, 'w+').close()

        logging.basicConfig(filename=self.config.LOGFILE, filemode='a', format=self.config.FORMAT, level=self.config.LEVEL)
        self.logger = logging.getLogger()


        try:
            self.interpretacion = Interpretacion(fichero)
            self.logger.info("Se crea el objeto de interpretacion")
        except:
           self.logger.error("No se ha encontrado el fichero")

    def generar_interpretacion(self, com_auto, fecha):
        '''Metodo para genear una interpretacion. Recibe como argumentos la comunidad autonoma y fecha'''
        salida = self.interpretacion.generar_interpretacion(com_auto, fecha)

        if salida == EstadoSituacion.DESCONOCIDA:
            self.logger.error("No se ha podido generar la interpretacion")
        else:
            self.logger.info("Interpretacion generada correctamente")

        return salida