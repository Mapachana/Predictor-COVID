# En construccion ...
# Autor Pablont98

from Datos import *
from Interpretacion import *
from Graficas import *
from Prediccion import *

# PRUEBAS DE CODIGO

ListaDatos = list()
DatosArchidonaHoy = Datos(40,"Archidona","Malaga","Andalucia")
DatosArchidonaAyer = Datos(30,"Archidona","Malaga","Andalucia")
DatosSevilla = Datos(100,"Sevilla","Sevilla","Andalucia")
ListaDatos.append(DatosArchidonaHoy)
ListaDatos.append(DatosSevilla)

ListaDatosArchidona = list()
ListaDatosArchidona.append(DatosArchidonaHoy)
ListaDatosArchidona.append(DatosArchidonaAyer)

Interpretacion = Interpretacion(ListaDatos)
Grafica = Graficas(ListaDatosArchidona)

Prediccion = Prediccion(ListaDatosArchidona)

print(Interpretacion.ContenedorDatos[0].NumCasos)
print(ListaDatosArchidona[1].NumCasos)
print(Grafica.ContenedorDatos[0].NumCasos)
print(len(Grafica.ContenedorDatos))
print(Grafica.NumCasos[0])
print(Prediccion.HistorialDatos[1].NumCasos)
