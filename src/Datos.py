from datetime import datetime

class Datos:
    numCasos = 0
    ciudad = ""
    provincia = ""
    comAutonoma = ""
    fecha = ""

    def __init__(self, numcasos, ciud, prov, comAuto):
        self.numCasos = numcasos
        self.ciudad = ciud
        self.provincia = prov
        self.comAutonoma = comAuto
        self.fecha = datetime.today()

    def numCasos(self):
        return self.numCasos

    def ciudad(self):
        return self.ciudad

    def provincia(self):
        return self.provincia

    def comAutonoma(self):
        return self.comAutonoma

    def fecha(self):
        return self.fecha

