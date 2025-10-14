# Propósito: bloque horario a cubrir en un día específico
# Atributos (obligatorios):
# • franja (referencia a Franja)
# • responsable (referencia a Colaborador)
# • marcado_forzado (bool) — true si rompe preferencia o regla de política
# • historial_eventos (solo lectura: {timestamp, tipo, detalle})
# Derivados (solo lectura):
# • duracion_horas (tomado de franja.duracion_horas)


class TurnoAsignado:
    def __init__(self, franja:object, responsable:object):
        # ??? marcado_forzado (bool) — true si rompe preferencia o regla de política
        self._historial_eventos = []
        
        # ???
        self.franja = franja
        self.responsable = responsable

    def duracion_horas(self):
        return self.franja.duracion_horas()
    
    