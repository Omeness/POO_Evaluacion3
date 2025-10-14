class Colaborador:
    def __init__(self, nombre:str, horas_semana_max:int, preferencia:str):
        
        # TODO: validaciones

        self.nombre = nombre
        self.horas_semana_max = horas_semana_max
        self.preferencia = preferencia
        self.no_disponible = []
        self._historial_eventos = []
        self._horas_asignadas_semana = 0

    