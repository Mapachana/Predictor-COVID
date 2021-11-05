import sys,os
import unittest
import pytest

#myPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, myPath + '/../')
#sys.path.insert(0, myPath + '/../prediccion/')

sys.path.append('../')
sys.path.append('../prediccion/')

# Configuro paths
sys.path.append('./')
sys.path.append('./prediccion/')


from ..prediccion.interpretacion import Interpretacion

@pytest.fixture
def interp():
    interp = Interpretacion([])
    interp.leer_datos("./prediccion/ccaa_de_declaracion_covid19_datos_isciii_nueva_serie.csv")

    return interp

def test_tiene_datos(interp):
    assert interp.contenedor_datos != []
