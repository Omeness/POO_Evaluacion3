from abc import ABC, abstractmethod
from typing import List


class PoliticaTurno(ABC):
    @abstractmethod
    def asignar(self, semana, colaboradores, franjas)-> List:
        pass


class TurnoFijo(PoliticaTurno):
    # • TurnoFijo — mantiene titular por franja; si no puede, asigna suplente (marca
    # marcado_forzado si rompe preferencia).
    def asignar(self, semana, colaboradores, franjas):
        pass


class TurnoRotativo(PoliticaTurno):
    # • TurnoRotativo — prohíbe que la misma persona abra dos días seguidos.
    def asignar(self, semana, colaboradores, franjas):
        pass


class TurnoFlexible(PoliticaTurno):
    # • TurnoFlexible — prioriza preferencia (manana/tarde); si no hay alternativa, asigna y
    # marca marcado_forzado.
    def asignar(self, semana, colaboradores, franjas):
        pass