# En construccion ...
# Autor Pablont98

from Datos import *
from Interpretacion import *
from Graficas import *
from Prediccion import *

# PRUEBAS DE CODIGO 

lista_datos = list()
datos_archidona_hoy = Datos(40,"Archidona","Malaga","Andalucia")
datos_archidona_ayer = Datos(30,"Archidona","Malaga","Andalucia")
datos_sevilla = Datos(100,"Sevilla","Sevilla","Andalucia")
lista_datos.append(datos_archidona_hoy)
lista_datos.append(datos_sevilla)

lista_datos_archidona = list()
lista_datos_archidona.append(datos_archidona_hoy)
lista_datos_archidona.append(datos_archidona_ayer)

interpretacion = Interpretacion(lista_datos)
grafica = Graficas(lista_datos_archidona)

prediccion = Prediccion(lista_datos_archidona)

print(interpretacion.contenedorDatos[0].numCasos)
print(lista_datos_archidona[1].numCasos)
print(grafica.contenedorDatos[0].numCasos)
print(len(grafica.contenedorDatos))
print(grafica.numCasos[0])
print(prediccion.historialDatos[1].numCasos)


