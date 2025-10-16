


class Agenda:
    # NOTE: no se si esto deberia ser un atributo de clase o estar dentro del constructor
    def __init__(self):
        self._citas = {}

    def agregar(self, cita):
        # valida id único y ausencia de solape; incorpora la cita
        pass

    def cancelar(self, cita):
        #cancela una cita agendada
        pass

    def existe_solape(self, profesional, inicio, fin) -> bool:
        print(profesional, inicio, fin)
        # verdadero si [inicio, fin) intersecta otro
        # intervalo no cancelado del mismo profesional.
        return False
