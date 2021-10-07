from datetime import date


class Interpretacion:

    def __init__(self, datos):
        self.contenedorDatos = list(datos)
        self.textoExplicacion = ""

    def contenedorDatos(self):
        return self.contenedorDatos

    def textoExplicacion(self):
        return self.textoExplicacion