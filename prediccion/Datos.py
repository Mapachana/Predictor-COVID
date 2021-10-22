from datetime import datetime

class Datos:
    '''
    Clase para representar los datos de nuevos casos en una comunidad autónoma en un día dado
    '''

    def __init__(self, num_casos, com_auto, fecha):
        '''
        Constructor de la clase Datos.

        Argumentos:
            - num_casos: numero de casos nuevos ese dia
            com_auto: Comunidad autonoma donde se reportan los casos
            fecha: Dia con los nuevos casos
        '''
        self.num_casos = num_casos
        self.com_autonoma = com_auto
        self.fecha = fecha
