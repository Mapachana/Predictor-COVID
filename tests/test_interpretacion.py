import sys
import unittest
import pytest

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')



from prediccion.interpretacion import Interpretacion


@pytest.fixture
def interp():
    interp = Interpretacion([])
    #interp.leer_datos("./prediccion/ccaa_de_declaracion_covid19_datos_isciii_nueva_serie.csv")

    return interp

def test_tiene_datos(interp):
    interp.leer_datos("./prediccion/ccaa_de_declaracion_covid19_datos_isciii_nueva_serie.csv")
    assert interp.contenedor_datos != []

def test_excepcion(interp):
    aux = unittest.TestCase()
    with aux.assertRaises(FileNotFoundError):
        interp.leer_datos("./noexisto.csv")

