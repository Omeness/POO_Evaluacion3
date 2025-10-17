# Modelo 2 — CalendarioCancha
# Propósito: encapsular la indisponibilidad por mantención.
# Datos mínimos
# • mantencion[]: lista de intervalos {inicio, fin} (no solapados entre sí).
# Operaciones (enunciado)
# • agregar(inicio, fin) → valida inicio < fin y no solape con bloques existentes.
# • intersecta(inicio, fin) -> bool → true si el intervalo propuesto cae total o parcialmente
# en mantención.

class CalendarioCancha:
    def __init__(self):
        
        # lista de intervalos {inicio, fin} (no solapados entre sí).
        self.mantencion = []

    def agregar(self, inicio, fin):
        # valida inicio < fin y no solape con bloques existentes
        pass

    def intersecta(self, inicio, fin) -> bool:
        # true si el intervalo propuesto cae total o parcialmente en mantención.
        pass