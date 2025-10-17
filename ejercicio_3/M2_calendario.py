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