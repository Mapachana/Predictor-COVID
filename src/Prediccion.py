
class Prediccion:

    def __init__(self,datos):
        self.historialDatos = list(datos)
        self.numCasosPredict = 0
        self.prediccion = ""
        self.nivelAlerta = 0

    def historialDatos(self):
        return self.historialDatos

    def numCasosPredict(self):
        return self.numCasosPredict

    def prediccion(self):
        return self.prediccion

    def nivelAlerta(self):
        return self.nivelAlerta