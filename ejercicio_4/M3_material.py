# Modelo 3 — Material (abstracto) y subtipos
# Propósito: definir puntaje y límite por bolsa según tipo (abstracción/polimorfismo)..
# Contrato (abstracto)
# • puntos(kg: decimal > 0) -> decimal ≥ 0
# • max_kg_por_bolsa() -> decimal > 0
# Subtipos requeridos (cada uno implementa el contrato)
# • Plastico — puntos altos por kg, max_kg_por_bolsa definido (p. ej., 8 kg)
# • Vidrio — puntos menores por kg, límite más bajo por seguridad (p. ej., 5 kg)
# • PapelCarton — puntos intermedios, puede contemplar merma (si se define en reglas)
# Nota: el sistema aplicará una única estrategia frente a kg > max_kg_por_bolsa() (rechazo o partición
# automática). La estrategia elegida no pertenece al material; se define a nivel de reglas del dominio

from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def puntos(self, kg:float):
        'kg: decimal ≥ 0'
        pass

    @abstractmethod
    def max_kg_por_bolsa(self):
        pass


class Plastico(Material):  
    #hasta 80 pts
    def puntos(self, kg:float) -> float:
        if kg <= 0:
            raise Exception("El valor de los kg debe ser mayor a cero")
        PUNTOS = 10
        return PUNTOS * kg

    def max_kg_por_bolsa(self) -> float:
        return 8.0
    
    def __str__(self):
        return 'Plastico'
    

class Vidrio(Material): 
    # hasta 30 pts
    def puntos(self, kg:float) -> float:
        if kg <= 0:
            raise Exception("El valor de los kg debe ser mayor a cero")
        PUNTOS = 6
        return PUNTOS * kg

    def max_kg_por_bolsa(self) -> float:
        return 5.0
    
    def __str__(self):
        return 'Vidrio'
    

class PapelCarton(Material): 
    # hasta 42 pts
    def puntos(self, kg:float) -> float:
        if kg <= 0:
            raise Exception("El valor de los kg debe ser mayor a cero")
        PUNTOS = 7
        return PUNTOS * kg
    
    def max_kg_por_bolsa(self) -> float:
        return 6.0
    
    def __str__(self):
        return 'Papel y Carton'