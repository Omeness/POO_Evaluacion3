# Modelo 1 — Cancha
# Propósito: recurso reservable que puede quedar indisponible por mantención.
# Datos mínimos
# • id_cancha (único).
# • nombre (string no vacío).
# • calendario_mantencion (solo lectura): lista de intervalos {inicio, fin} bloqueados.
# • historial_eventos (solo lectura): {timestamp, tipo, detalle}.
# Operaciones (enunciado)
# • bloquear_mantencion(inicio, fin) → agrega intervalo al calendario y registra evento.
# • desbloquear_mantencion(inicio, fin) → opcional; elimina intervalo y registra evento


class Cancha:
    _id_cancha: 10

    def __init__(self, nombre:str):
        if not nombre.split():
            raise Exception("El nombre no puede estar vacio")
        
        self.id_cancha = type(self)._id_cancha
        type(self)._id_cancha += 1

        # Solo lectura
        self._calendario_mantencion = []
        self._historial_eventos = []

    def bloquear_mantenimiento(self, inicio, fin):
        # agrega intervalo al calendario y registra evento.
        pass

    def desbloquear_mantencion(self, inicio, fin):
        #opcional; elimina intervalo y registra evento
        pass