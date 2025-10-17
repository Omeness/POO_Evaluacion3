# Propósito: bloque horario a cubrir en un día específico
# Atributos (obligatorios):
# • franja (referencia a Franja)
# • responsable (referencia a Colaborador)
# • marcado_forzado (bool) — true si rompe preferencia o regla de política
# • historial_eventos (solo lectura: {timestamp, tipo, detalle})
# Derivados (solo lectura):
# • duracion_horas (tomado de franja.duracion_horas)


from datetime import datetime


class TurnoAsignado:
    def __init__(self, franja:object, responsable:object):
        """Asignar una franja a un colaborador

        referencias: franja(Franja) - responsable(Colaborador)
        """

        # ??? marcado_forzado (bool) — true si rompe preferencia o regla de política
        self.franja = franja
        self.responsable = responsable
        self.marcado_forzado = None
        self._historial_eventos = []

    def duracion_horas(self):
        return self.franja.duracion_horas()
    



