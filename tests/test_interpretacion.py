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
    interp = Interpretacion([])
    interp.leer_datos("./tests/datos_prueba.csv")

    return interp

def test_tiene_datos(interp):
    assert interp.contenedor_datos != []

def test_excepcion():
    interp = Interpretacion([])
    aux = unittest.TestCase()
    with aux.assertRaises(FileNotFoundError):
        interp.leer_datos("./noexisto.csv")

def test_datos_correctos(interp):
    for elem in interp.contenedor_datos:
        assert elem.fecha != ''
        assert elem.com_autonoma != ''
        assert elem.num_casos >= 0

def test_interpretacion_correcta(interp):
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
    
