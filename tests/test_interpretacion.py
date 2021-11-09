import sys
import unittest

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')


from prediccion.interpretacion import Interpretacion

class TestInterpretacion(unittest.TestCase):
    
    def setUp(self):
        ''''
        Funcion fixture que crea el objeto interpretacion a usar para los tests
        '''
        self.interp = Interpretacion("./tests/datos_prueba.csv")


    def test_tiene_datos(self):
        '''
        Funcion test para comprobar si el contenedor de datos esta vacio
        '''
        #self.interp = Interpretacion("./tests/datos_prueba.csv")

        assert self.interp.contenedor_datos != []

    def test_excepcion(self):
        ''''
        Funcion test para comprobar si se lanza una excepcion de fichero no encontrado al pasar un archivo inexistente
        '''
        with self.assertRaises(SystemExit):
            interp = Interpretacion("./noexisto.csv")

    def test_datos_correctos(self):
        '''
        Funcion test para comprobar si los datos se han leido correctamente y tienen sentido
        '''
        for elem in self.interp.contenedor_datos:
            assert elem.fecha != ''
            assert elem.com_autonoma != ''
            assert elem.num_casos >= 0

    def test_interpretacion_correcta(self):
        '''
        Funcion test para comprobar si las interpretaciones son correctar
        '''

        interpretacion_generada = self.interp.generar_interpretacion('Andalucía', '2021-01-10')
        assert interpretacion_generada == "No vamos bien"

        interpretacion_generada = self.interp.generar_interpretacion("Andalucía", "2020-03-10")
        assert interpretacion_generada == "Vamos bien"


    def test_interpretacion_ccaa_no_existe(self):
        ''''
        Funcion test para asegurarse de que no realiza predicciones si los datos pedidos no son correctos
        '''

        interpretacion_generada = self.interp.generar_interpretacion('CCAANoExistente', '2021-01-10')
        assert interpretacion_generada == "No se ha encontrado la comunidad autonoma o fecha indicadas"
