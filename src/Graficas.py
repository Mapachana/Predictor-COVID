class Graficas:

    def __init__(self,datos):
        self.contenedorDatos = list(datos)
        tam = len(self.contenedorDatos)
        self.numCasos = list()
        self.fechas = list()
        for i in range(tam):
            self.numCasos.append(self.contenedorDatos[i].numCasos)
            self.fechas.append(self.contenedorDatos[i].fecha)

    def contenedorDatos(self):
        return self.contenedorDatos

    def numCasos(self):
        return self.numCasos

    def fechas(self):
        return self.fechas
