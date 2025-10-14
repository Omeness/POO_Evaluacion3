from abc import ABC, abstractmethod


class Servicio(ABC):

    @abstractmethod
    def corte_cabello(self):
        pass

    @abstractmethod
    def coloracion(self):
        pass