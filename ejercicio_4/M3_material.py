from .validaciones import menor_igual_cero

from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def puntos(self, kg:float):
        """Calcula puntos dependiendo del peso y material"""
        pass

    @abstractmethod
    def max_kg_por_bolsa(self):
        pass


class Plastico(Material):  
    #hasta 80 pts
    def puntos(self, kg:float) -> float:
        if menor_igual_cero(kg):
            raise Exception("Los kg de plastico deben ser mayor a cero")
        PUNTOS = 10
        return PUNTOS * kg

    def max_kg_por_bolsa(self) -> float:
        return 8.0
    
    def __str__(self):
        return 'Plastico'
    

class Vidrio(Material): 
    # hasta 30 pts
    def puntos(self, kg:float) -> float:
        if menor_igual_cero(kg):
            raise Exception("Los kg de vidrio deben ser mayor a cero")
        PUNTOS = 6
        return PUNTOS * kg

    def max_kg_por_bolsa(self) -> float:
        return 5.0
    
    def __str__(self):
        return 'Vidrio'
    

class PapelCarton(Material): 
    # hasta 42 pts
    def puntos(self, kg:float) -> float:
        if menor_igual_cero(kg):
            raise Exception("Los kg de papel y carton deben ser mayor a cero")
        PUNTOS = 7
        return PUNTOS * kg
    
    def max_kg_por_bolsa(self) -> float:
        return 6.0
    
    def __str__(self):
        return 'Papel y Carton'