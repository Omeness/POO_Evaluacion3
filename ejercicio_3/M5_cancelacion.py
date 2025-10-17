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