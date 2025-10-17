from datetime import datetime
from .validaciones import sumar_pts

class Semana:
    def __init__(self, inicio, fin):
        """
        Crea una semana y mantiene registro de los retiros hechos.

        Mantiene registro de las veces que se han hecho retiros por subscriptor.

        Solo almacena y verifica bono semanal. Las adiciones se hacen a traves de Retiro.

        formato fecha: 'dd-mm-yyyy'
        """
        
        if inicio > fin:
            raise Exception(f"La semana debe empezar antes del {fin} o terminar despues del {inicio}")
        
        self.__inicio = datetime.strptime(f"{inicio}", "%d-%m-%Y")
        self.__fin = datetime.strptime(f"{fin}", "%d-%m-%Y")

        self._retiros = []

    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def fin(self):
        return self.__fin

    def bono_semanal(self):
        suscriptores = []
        for sus in self._retiros:
            retiro_semanal = self._retiros.count(sus)
            if retiro_semanal >= 3 and sus not in suscriptores:
                suscriptores.append(sus)
        for sub in suscriptores:
            sumar_pts(sub,10)

    def __str__(self):
        return f"Semana del {self.__inicio.strftime("%d-%m-%Y")} al {self.__fin.strftime("%d-%m-%Y")}"
