import sys
import os
import unittest

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')


#from prediccion.interpretacion import ErrorEncontrandoFichero, EstadoSituacion, Interpretacion
#from prediccion.gestor_interpretacion import GestorInterpretacion

#import prediccion.interpretacion as it
#import prediccion.gestor_interpretacion as gt

import prediccion.interpretacion as it
import prediccion.gestor_interpretacion as gt

class TestGestorInterpretacion(unittest.TestCase):
    
    def setUp(self):
        self.interp = gt.GestorInterpretacion("./tests/datos_prueba.csv")

    def test_tiene_datos(self):
        assert self.interp.interpretacion.contenedor_datos != []

    def test_datos_correctos(self):
        for elem in self.interp.interpretacion.contenedor_datos:
            assert elem.fecha != ''
            assert elem.com_autonoma != ''
            assert elem.num_casos >= 0

    def test_interpretacion_correcta(self):
        interpretacion_generada = self.interp.generar_interpretacion('Andalucía', '2021-01-10')
        assert interpretacion_generada == gt.EstadoSituacion.MALA

        interpretacion_generada = self.interp.generar_interpretacion("Andalucía", "2020-03-10")
        assert interpretacion_generada == gt.EstadoSituacion.BUENA

    def test_interpretacion_ccaa_no_existe(self):
        interpretacion_generada = self.interp.generar_interpretacion('CCAANoExistente', '2021-01-10')
        assert interpretacion_generada is gt.EstadoSituacion.DESCONOCIDA

    def test_fichero_existe(self):
        assert os.path.isfile("/tmp/IV/logs.log")
    
    def leer_fichero(self, fichero):
        lineas = []
        with open(fichero, "r") as fichero:
            lineas = fichero.readlines()
        return lineas

    def obtener_codigo_log(self, fichero):
        lineas_fichero = self.leer_fichero(self.interp.config.LOGFILE)
        linea = lineas_fichero[-1]
        linea = linea.split(" - ")
        return  linea[0]

    def test_muestra_log_fichero_no_encontrado(self):
        gt.GestorInterpretacion("./noexisto.csv")
        codigo = self.obtener_codigo_log(self.interp.config.LOGFILE)
        assert codigo == "ERROR"
    
    def test_muestra_log_no_interpretacion(self):
        self.interp.generar_interpretacion('CCAANoExistente', '2021-01-10')

        codigo = self.obtener_codigo_log(self.interp.config.LOGFILE)
        assert codigo == "ERROR"

    def test_muestra_log_interpretacion_generada(self):
        self.interp.generar_interpretacion("Andalucía", "2020-03-10")
        codigo = self.obtener_codigo_log(self.interp.config.LOGFILE)
        assert codigo == "INFO"