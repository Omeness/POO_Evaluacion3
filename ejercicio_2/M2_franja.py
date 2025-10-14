class Franja:
    def __init__(self, dia, hora_inicio, hora_fin):
        
        #TODO: validar: hora_fin (HH:MM) — debe ser > hora_inicio

        # ??? eso es todo? what
        #TODO i guess: deberia haber un retorno or something para usar esta informacion
        self._duracion_horas = hora_inicio - hora_fin

    def duracion_horas(self):
        return self._duracion_horas