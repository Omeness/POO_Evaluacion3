# Modelo 5 — PoliticaCancelacion (abstracta) y subtipos.
# Propósito: determinar penalización al cancelar según anticipación (abstracción/polimorfismo).
# Contrato (abstracta)
# • penalizacion(horas_previas, importe) -> {monto_penalizacion, motivo}
# o Valida horas_previas ≥ 0 e importe ≥ 0.
# Subtipos requeridos
# • CancelacionFlexible → 0% si horas_previas ≥ 24; de lo contrario 20% del importe.
# • CancelacionEstricta → 50% del importe, independiente de horas_previas.
# Relaciones.
# • Una Cancha tiene un CalendarioCancha con mantencion[].
# • Una Reserva referencia exactamente una Cancha.
# • Una Reserva cotiza con una Tarifa concreta (subtipo) y puede cancelar con una
# PoliticaCancelacion concreta (subtipo).
# • El desglose_tarifa y el importe en Reserva son solo lectura y se originan exclusivamente
# desde Tarifa.calcular_importe(...).

from abc import ABC, abstractmethod


class PoliticaCancelacion(ABC):
    @abstractmethod
    def penalizacion(self, horas_previas, importe):
        pass

class CancelacionFlexible(PoliticaCancelacion):
    def penalizacion(self, horas_previas, importe):
        if horas_previas >= 24:
            pass
        # 0% si horas_previas ≥ 24; de lo contrario 20% del importe.
        pass

class CancelacionEstricta(PoliticaCancelacion):
    def penalizacion(self, horas_previas, importe):
        # 50% del importe, independiente de horas_previas.
        pass