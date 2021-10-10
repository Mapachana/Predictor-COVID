from datetime import datetime

class Datos:

    def __init__(self, numcasos, ciud, prov, comAuto):
        self.NumCasos = numcasos
        self.Ciudad = ciud
        self.Provincia = prov
        self.ComAutonoma = comAuto
        self.Fecha = datetime.today()
