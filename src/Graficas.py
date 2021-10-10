class Graficas:

    def __init__(self,datos):
        self.ContenedorDatos = list(datos)
        tam = len(self.ContenedorDatos)
        self.NumCasos = list()
        self.Fechas = list()
        for i in range(tam):
            self.NumCasos.append(self.ContenedorDatos[i].NumCasos)
            self.Fechas.append(self.ContenedorDatos[i].Fecha)
