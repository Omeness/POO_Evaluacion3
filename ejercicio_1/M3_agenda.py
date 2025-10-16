from M1_cita import Cita


class Agenda:
    def __init__(self):
        self._citas = []

    def existe_solape(self, profesional, inicio, fin) -> bool:
        # Dos intervalos [A_inicio, A_fin) y [B_inicio, B_fin) se solapan si
        # • A_inicio < B_fin y B_inicio < A_fin.
        # verdadero si [inicio, fin) intersecta otro
        # intervalo no cancelado del mismo profesional.
        
        return False
    
    def agregar(self, cita: Cita):
        if cita.id_cita in [obj.id_cita for obj in self._citas]:
            raise Exception(f"La cita con ID: {cita.id_cita}  ya esta registrada")
        
        profesional = cita.profesional
        inicio = cita.inicio
        fin = cita.fin

        if self.existe_solape(profesional, inicio, fin):
            raise Exception("La cita se solapa con otra")
        
        self._citas.append(cita)
        return "Cita agendada con exito"

        # valida id único y ausencia de solape; incorpora la cita

