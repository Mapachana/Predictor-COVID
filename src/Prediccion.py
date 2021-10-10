class Prediccion:

    def __init__(self,datos):
        self.HistorialDatos = list(datos)
        self.NumCasosPredict = 0
        self.Prediccion = ""
        self.NivelAlerta = 0
