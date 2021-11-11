import sys
import unittest

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')


from prediccion.interpretacion import ErrorEncontrandoFichero, EstadoSituacion, Interpretacion

class TestInterpretacion(unittest.TestCase):
    
    def setUp(self):
        self.interp = Interpretacion("./tests/datos_prueba.csv")


    def test_tiene_datos(self):
        assert self.interp.contenedor_datos != []

    def test_excepcion_fichero_no_encontrado(self):
        with self.assertRaises(ErrorEncontrandoFichero):
            interp = Interpretacion("./noexisto.csv")

    def test_datos_correctos(self):
        for elem in self.interp.contenedor_datos:
            assert elem.fecha != ''
            assert elem.com_autonoma != ''
            assert elem.num_casos >= 0

    def test_interpretacion_correcta(self):
        interpretacion_generada = self.interp.generar_interpretacion('Andalucía', '2021-01-10')
        assert interpretacion_generada == EstadoSituacion.MALA

        interpretacion_generada = self.interp.generar_interpretacion("Andalucía", "2020-03-10")
        assert interpretacion_generada == EstadoSituacion.BUENA

    def test_interpretacion_ccaa_no_existe(self):
        interpretacion_generada = self.interp.generar_interpretacion('CCAANoExistente', '2021-01-10')
        assert interpretacion_generada == EstadoSituacion.DESCONOCIDA
