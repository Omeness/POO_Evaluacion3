from abc import ABC, abstractmethod
from datetime import datetime


class Tarifa(ABC):
    @abstractmethod
    def calcular_importe(self, inicio, fin):
        pass


class TarifaDiurna(Tarifa):
    def __init__(self):
        self._inicio = datetime.strptime(f"08:00", "%H:%M")
        self.fin = datetime.strptime(f"19:59", "%H:%M")

    def calcular_importe(self, inicio, fin):
        pass


class TarifaNocturna(Tarifa):
    def __init__(self):
        self._inicio = datetime.strptime(f"20:00", "%H:%M")
        self.fin = datetime.strptime(f"07:59", "%H:%M")

    def calcular_importe(self, inicio, fin):
        pass


class TarifaFinDeSemana(Tarifa):
    #prioritaria sobre Diurna/Nocturna cuando el tramo cae en fin de semana.
    pass

