"""
Atributos derivados (solo lectura):
• fin = inicio + duracion_min.
"""

from datetime import datetime
from M2_servicio import Servicio



class Cita(Servicio):
    _id_cita = 10
    def __init__(self, cliente, profesional, inicio, estado="creada"):

        # Validaciones de los atributos
        if not cliente.split():
            raise Exception("El nombre de cliente no puede estar vacio")
        if not profesional.split():
            raise Exception("El nombre del profesional no puede estar vacio")
        
        # NOTE: que pasa con servicio.duracion???

        self.id_cita = type(self)._id_cita
        type(self)._id_cita += 1
        self._duracion_min = 0
        self.__cliente = cliente
        self.__profesional = profesional
        self.inicio = inicio
        self.estado = estado # creada, confirmada, cancelada
        self._historial_eventos = [] # read-only, timestamp, tipo, detalle

    def _registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial.append(f"[{fecha}] [{tipo}] [{detalle}]")

    def asignar_servicio(self, servicio):
        # fija duracion_min desde el servicio; registra evento servicio_asignado.
        # Duración desde Servicio: duracion_min proviene exclusivamente de
        # Servicio.duracion_min().
        # La duración de la Cita se fija solo vía asignar_servicio(servicio) (no editable manualmente).
        pass

    def confirmar(self, motivo, agenda):
        if self.estado == "creada":
            pass
        # NOTE: que deberia poner en motivo y agenda :| se supone que asigno el servicio y despiues confirmo???
        # valida estado creada, servicio asignado y franja libre;
        # cambia a confirmada; registra evento
        

    def cancelar(self, motivo):
        # valida estado (creada/confirmada); cambia a cancelada; registra evento.
        pass

    def corte_cabello(self):
        # duracion_min = 30.
        pass

    def coloracion(self):
        # duracion_min = 90.
        pass
