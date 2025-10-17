# Modelo 4 — PlanSemanal
# Propósito: resultado de la planificación para una semana.
# Atributos (obligatorios):
# • semana (rango de fechas continuo)
# • franjas[] (lista de Franja a cubrir)
# • turnos_asignados[] (lista de TurnoAsignado)
# • historial_eventos (solo lectura: {timestamp, tipo, detalle})
# Derivados (solo lectura):
# • cobertura_% = (turnos_cubiertos / turnos_totales) × 100
# • valido (bool) — true si todas las franjas tienen responsable y nadie supera
# horas_semana_max


class PlanSemanal:
    def __init__(self, semana, franjas:list, turnos_asignados:list):
        """Resultado de la planificación para una semana
        """
        
        self.semana = semana
        self.franjas = franjas
        self.turnos_asignados = turnos_asignados
        self._historial_eventos = []

    def cobertura(self):
        cobertura = (self.turnos_asignados / self.franjas) * 100
        return f"Nivel de cobertura: {cobertura}%"
    
    # TODO:
    # valido (bool) — true si todas las franjas tienen responsable y 
    # nadie supera horas_semana_max