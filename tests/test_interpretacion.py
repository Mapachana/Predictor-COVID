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
    with aux.assertRaises(FileNotFoundError):
        #interp.leer_datos("./noexisto.csv")
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

    # Redirijo la salida
    captured_output = io.StringIO()
    sys.stdout = captured_output

    interp.generar_interpretacion('Andalucía', '2021-01-10')
    interpretacion_generada = captured_output.getvalue()
    assert interpretacion_generada == "No vamos bien\n"

    # Vaciar la salida anterior
    captured_output.truncate(0)
    captured_output.seek(0)

    interp.generar_interpretacion("Andalucía", "2020-03-10")
    interpretacion_generada = captured_output.getvalue()
    assert interpretacion_generada == "Vamos bien\n"

    # Dejo la salida como estaba
    sys.stdout = sys.__stdout__
    
def test_interpretacion_ccaa_no_existe(interp):
    ''''
    Funcion test para asegurarse de que no realiza predicciones si los datos pedidos no son correctos
    '''

     # Redirijo la salida
    captured_output = io.StringIO()
    sys.stdout = captured_output

    interp.generar_interpretacion('CCAANoExistente', '2021-01-10')
    interpretacion_generada = captured_output.getvalue()
    assert interpretacion_generada == "No se ha encontrado la comunidad autonoma o fecha indicadas\n"

    # Dejo la salida como estaba
    sys.stdout = sys.__stdout__
