
import sys
from functools import reduce
from enum import Enum

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')

import datos as dt


class ErrorEncontrandoFichero(Exception):
    pass


class EstadoSituacion(Enum):
    BUENA = "Vamos bien"
    MALA = "No vamos bien"
    DESCONOCIDA = "No se ha encontrado la comunidad autonoma o fecha indicadas"


class Interpretacion:
    '''
    Clase para obtener información de un conjunto de Datos
    '''

    def __init__(self, fichero):
        '''
        Constructor de la clase Interpretacion, que trabaja con los datos para dar una explicacion sencilla de la situacion actual.

        Argumentos:
            - fichero: fichero desde el que se van a leer los datos
        '''
        self.contenedor_datos = list()
        self.NUM_DIAS = 14
        self.leer_datos(fichero)
 
    def leer_datos(self, fichero_leer):
        '''
        Metodo para leer y almacenar los datos de un fichero para trabajar con ellos
        '''
        lineas = []
        try:
            with open(fichero_leer, "r") as fichero:
                lineas = fichero.readlines()

            lineas.pop(0)
            for linea in lineas:
                aux = linea.split(",")
                fecha = aux[0]
                ccaa = aux[2]

                lista_casos = aux[3:]
                lista_casos = map(int, lista_casos)
                casos = reduce(lambda x, y:x+y, lista_casos)

                self.contenedor_datos.append(dt.Datos(fecha, ccaa, casos))

        except:
            raise ErrorEncontrandoFichero("No se ha encontrado el fichero")

    def generar_interpretacion(self,com_auto,fecha):
        '''
        Metodo para crear una interpretacion a partir del contenedor de datos filtrandola
        por comunidad autonoma y fecha. 
        
        Devuelve: Un string con la interpretación o error si no se ha podido generar.
        '''

        indice = -1
        for i in range(0,len(self.contenedor_datos)):
            if self.contenedor_datos[i].com_autonoma == com_auto and self.contenedor_datos[i].fecha == fecha:
                indice = i
                break
        
        if indice >= 0:
            total_casos = 0

            indice_inicio = max(indice-self.NUM_DIAS, 0)

            # Sumo todos los casos desde el dia de indice_inicio hasta indice (fecha indicada)
            total_casos = reduce(lambda x,y:x+y, (x.num_casos for x in self.contenedor_datos[indice_inicio:indice]))

            if total_casos < 500:
                return EstadoSituacion.BUENA
            else:
                return EstadoSituacion.MALA
        else:
            return EstadoSituacion.DESCONOCIDA
                      
