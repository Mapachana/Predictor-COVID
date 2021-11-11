from dataclasses import dataclass

@dataclass(frozen=True)
class Datos:
    '''
    Clase para representar los datos de nuevos casos en una comunidad autónoma en un día dado
    '''

    fecha: str
    com_autonoma: str
    num_casos: int
