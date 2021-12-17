import sys
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
        interpretacion_generada = self.interp.interpretacion.generar_interpretacion('CCAANoExistente', '2021-01-10')
        assert interpretacion_generada is gt.EstadoSituacion.DESCONOCIDA

interp = gt.GestorInterpretacion("./tests/datos_prueba.csv")

interpretacion_generada = interp.generar_interpretacion('Andalucía', '2021-01-10')