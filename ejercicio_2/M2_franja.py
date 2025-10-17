# Modelo 2 — Franja
# Propósito: bloque horario a cubrir en un día específico.
# Atributos (obligatorios):
# • dia (fecha o nombre de día dentro de la semana)
# • hora_inicio (HH:MM)
# • hora_fin (HH:MM) — debe ser > hora_inicio
# Derivados (solo lectura):
# • duracion_horas = hora_fin − hora_inicio


from datetime import datetime


class Franja:
    def __init__(self, dia:str, hora_inicio:str, hora_fin:str):
        """Bloque horario a cubrir en un día específico

        Formatos: dia -> 'dddd' | hora -> 'HH:MM'"""

        hora_inicio = datetime.strptime(f"{hora_inicio}", "%H:%M")
        hora_fin = datetime.strptime(f"{hora_fin}", "%H:%M")

        if hora_fin < hora_inicio:
            raise Exception(f"La hora de finalizacion debe ser despues de las {hora_inicio.strftime("%H:%M")}")

        self.dia = dia.upper()
        self.hora_inicio = hora_fin
        self.hora_fin = hora_fin
        self._duracion_horas =  hora_fin - hora_inicio 

    def duracion_horas(self):
        return self._duracion_horas


a = Franja("LUNES", "10:20", "10:40")
print(a.duracion_horas())
