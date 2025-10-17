# Modelo 4 — Tarifa (abstracta) y subtipos.
# Propósito: calcular el importe según franja temporal (abstracción/polimorfismo).
# Tarifa (abstracta)
# • calcular_importe(inicio, fin) -> {total, desglose[]}
# • Debe validar inicio < fin, segmentar el intervalo en tramos homogéneos y sumar
# subtotales.
# Subtipos requeridos
# • TarifaDiurna (08:00–19:59) → aplica solo a minutos dentro de esa franja.
# • TarifaNocturna (20:00–07:59) → contempla cruce de medianoche.
# • TarifaFinDeSemana (sábado/domingo) → prioritaria sobre Diurna/Nocturna cuando el
# tramo cae en fin de semana.
# Notas comunes
# • Política de prorrateo por minutos y redondeo monetario a 2 decimales (mitad arriba),
# consistente en todo el sistema.
# • La prioridad “FinDeSemana sobre Diurna/Nocturna” debe aplicarse de forma
# uniforme.Reglas de negocio

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

