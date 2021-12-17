import sys
import logging

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')

import datos as dt
import interpretacion as it
import config as config

class GestorInterpretacion:
    '''Clase para gestionar la clase Interpretacion'''
    def __init__(self, fichero):
        '''Constructor de la clase GestorInterpretacion, que gestiona la clase Interpretacion'''
        # Instancio la configuracion para configurar el logger
        self.config = config.Config()
        logging.basicConfig(filename=self.config.LOGFILE, filemode='a', format=self.config.FORMAT, level=self.config.LEVEL)
        self.logger = logging.getLogger()

        try:
            self.interpretacion = it.Interpretacion(fichero)
            self.logger.info("Se crea el objeto de interpretacion")
        except:
           self.logger.error("No se ha encontrado el fichero")

    def generar_interpretacion(self, com_auto, fecha):
        '''Metodo para genear una interpretacion. Recibe como argumentos la comunidad autonoma y fecha'''
        salida = self.interpretacion.generar_interpretacion(com_auto, fecha)
        if salida == it.EstadoSituacion.DESCONOCIDA:
            self.logger.error("No se ha podido generar la interpretacion")
        else:
            self.logger.info("Interpretacion generada correctamente")