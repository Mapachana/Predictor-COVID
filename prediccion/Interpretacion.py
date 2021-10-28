import Datos as dt

class Interpretacion:
    '''
    Clase para obtener información de un conjunto de Datos
    '''

    def __init__(self, datos):
        '''
        Constructor de la clase Interpretacion, que trabaja con los datos para dar una explicacion sencilla de la situacion actual.

        Argumentos:
            - datos: Lista de datos sobre los que se trabaja 
        '''
        self.contenedor_datos = list(datos)
 
    def leer_datos(self,fichero_leer):
        '''
        Metodo para leer y almacenar los datos de un fichero para trabajar con ellos
        '''
        lineas = []
        with open(fichero_leer, "r") as fichero:
            lineas = fichero.readlines()

        lineas.pop(0)
        for linea in lineas:
            aux = linea.split(",")
            fecha = aux[0]
            ccaa = aux[2]
            casos = int(aux[3])+int(aux[4])+int(aux[5])+int(aux[6])+int(aux[7])+int(aux[7])

            self.contenedor_datos.append(dt.Datos(fecha, ccaa, casos))

        print(self.contenedor_datos)
        print(self.contenedor_datos[0].fecha)
        print(self.contenedor_datos[0].com_autonoma)
        print(self.contenedor_datos[0].num_casos)

    def generar_interpretacion(self,com_auto,fecha):
        ''' Metodo para crear una interpretacion a partir del contenedor de datos 
        se puede filtrar dicha interpretacion por comunidad autonoma y
        fecha. Si no se desea contar con alguno de esos atributos, 
        se marca como cadena vacia "" '''   
        pass


interp = Interpretacion([])
interp.leer_datos("ccaa_de_declaracion_covid19_datos_isciii_nueva_serie.csv")