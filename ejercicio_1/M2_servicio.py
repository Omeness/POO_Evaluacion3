from abc import ABC, abstractmethod


class Servicio(ABC):
    """La duracion debe ser un numero entero mayor a cero"""

    @abstractmethod
    def duracion_min(self)-> int:
        pass


class CorteCabello(Servicio):

    @property
    def duracion_min(self):
        return 30
    
    def __str__(self):
        return "Corte de Cabello"
    

class Coloracion(Servicio):

    @property
    def duracion_min(self):
        return 90
    
    def __str__(self):
        return "Coloracion"
    