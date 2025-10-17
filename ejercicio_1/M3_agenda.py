class Agenda:
    def __init__(self):
        self._citas = []
        self._cita_solapada = None

    @property
    def cita_solapada(self):
        return self._cita_solapada

    def existe_solape(self, profesional, inicio, fin) -> bool:
        cita_solapada = None
        for cita in self._citas:
            if profesional == cita.profesional:
                if inicio < cita.fin and cita.inicio < fin:
                    cita_solapada = cita.id_cita
        if cita_solapada is None:
            return False
        else:
            self._cita_solapada = f"ID: {cita_solapada}"
            return True
                
    def agregar(self, cita: object):
        """Para agregar una cita primero se debe asignar un servicio y confirmar"""
        # NOTE: La validacion de solapamiento se hace desde Cita.confirmar()
        # Aqui solo se valida que la cita este confirmada

        if cita._estado != "confirmada":
            raise Exception("La cita debe estar confirmada para agregarse")
        if cita.id_cita in [obj.id_cita for obj in self._citas]:
            raise Exception(f"La cita con ID: {cita.id_cita}  ya esta registrada")

        self._citas.append(cita)
        detalle = f"Desde: {cita.inicio.strftime("%H:%M")} hrs. Hasta: {cita.fin.strftime("%H:%M")} hrs."
        cita._registrar_evento("Cita agregada la agenda", detalle)
        return "Cita agendada con exito"
    
    def ver_agenda(self):
        print("\n--- AGENDA ---\n")
        for cita in self._citas:
            print(f"[ID: {cita.id_cita}] Desde: {cita.inicio.strftime("%H:%M")} hrs."
                  f" Hasta: {cita.fin.strftime("%H:%M")} hrs. | "
                  f"Profesional: {cita.profesional} - Servicio: {cita.servicio}")


