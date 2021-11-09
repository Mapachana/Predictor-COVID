import sys
import unittest
import pytest
import io

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')


from prediccion.interpretacion import Interpretacion


@pytest.fixture
def interp():
    ''''
    Funcion fixture que crea el objeto interpretacion a usar para los tests
    '''
    interp = Interpretacion("./tests/datos_prueba.csv")

    return interp

def test_tiene_datos(interp):
    '''
    Funcion test para comprobar si el contenedor de datos esta vacio
    '''
    assert interp.contenedor_datos != []

def test_excepcion():
    ''''
    Funcion test para comprobar si se lanza una excepcion de fichero no encontrado al pasar un archivo inexistente
    '''
    aux = unittest.TestCase()
    with aux.assertRaises(SystemExit):
        interp = Interpretacion("./noexisto.csv")

def test_datos_correctos(interp):
    '''
    Funcion test para comprobar si los datos se han leido correctamente y tienen sentido
    '''
    for elem in interp.contenedor_datos:
        assert elem.fecha != ''
        assert elem.com_autonoma != ''
        assert elem.num_casos >= 0

def test_interpretacion_correcta(interp):
    '''
    Funcion test para comprobar si las interpretaciones son correctar
    '''

    interpretacion_generada = interp.generar_interpretacion('Andalucía', '2021-01-10')
    assert interpretacion_generada == "No vamos bien"

    interpretacion_generada = interp.generar_interpretacion("Andalucía", "2020-03-10")
    assert interpretacion_generada == "Vamos bien"


def test_interpretacion_ccaa_no_existe(interp):
    ''''
    Funcion test para asegurarse de que no realiza predicciones si los datos pedidos no son correctos
    '''

    interpretacion_generada = interp.generar_interpretacion('CCAANoExistente', '2021-01-10')
    assert interpretacion_generada == "No se ha encontrado la comunidad autonoma o fecha indicadas"

