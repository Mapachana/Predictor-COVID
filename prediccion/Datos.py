from datetime import datetime

class Datos:

    def __init__(self, numcasos, ciud, prov, com_auto):
        self.num_casos = numcasos
        self.ciudad = ciud
        self.provincia = prov
        self.com_autonoma = com_auto
        self.fecha = datetime.today()
