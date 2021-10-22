from datetime import datetime

class Datos:
    '''
    Clase para representar los datos de nuevos casos en una comunidad autónoma en un día dado
    '''

    def __init__(self, fecha, com_auto, num_casos):
        '''
        Constructor de la clase Datos.

        Argumentos:
            - num_casos: numero de casos nuevos ese dia
            com_auto: Comunidad autonoma donde se reportan los casos
            fecha: Dia con los nuevos casos
        '''
        self.fecha = fecha
        self.com_autonoma = com_auto
        self.num_casos = num_casos
