"""
Atributos derivados (solo lectura):
• fin = inicio + duracion_min.
"""

from datetime import datetime, timedelta
from M2_servicio import CorteCabello, Servicio
from M3_agenda import Agenda


class Cita:
    _id_cita = 10

    def __init__(self, cliente:str, profesional:str, inicio: str, estado="creada"):

        # Validaciones de los atributos
        if not cliente.split(): 
            raise Exception("El nombre de cliente no puede estar vacio")
        if not profesional.split():
            raise Exception("El nombre del profesional no puede estar vacio")
        
        # La hora de inicio se pide como str pero despues se transforma a datetime
        inicio = datetime.strptime(f"{inicio}", "%H:%M")

        # Validamos que la cita se tome en una hora posterior a la hora actual
        _hora_inicio = inicio.time()
        _hora_actual = datetime.now().time().replace(microsecond=0)
        if _hora_actual > _hora_inicio:
            raise Exception(f"Las citas pueden tomarse a partir de las {_hora_actual} hrs.")
        
        self.id_cita = type(self)._id_cita
        type(self)._id_cita += 1

        self.__cliente = cliente
        self.__profesional = profesional
        self._inicio = inicio
        self._fin = None

        # Parametros de solo lectura
        self._duracion_min = None
        self._estado = estado # creada, confirmada, cancelada
        self._historial_eventos = [] # read-only, timestamp, tipo, detalle

    def _registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(f"[{fecha}] [{tipo}] [{detalle}]")

    def fin_hora(self):
        return f"Final del servicio: {self._fin} hrs."

    def asignar_servicio(self, servicio: Servicio):
        if self._estado != "creada":
            raise Exception(f"No se puede asignar servicio a una cita en estado'{self._estado}'")
        if servicio.duracion_min <= 0:
            raise Exception("La duracion del servicio debe ser mayor a cero")
        
        fin = self._inicio + timedelta(minutes=servicio.duracion_min)
        inicio = self._inicio.strftime("%H:%M")

        detalle = f'Hora inicio: {inicio} | Hora fin: {fin.strftime("%H:%M")} | Profesional: {self.__profesional}'
        self._registrar_evento(f"Servicio asignado: {servicio}", detalle)
        self._duracion_min = servicio.duracion_min
        self._fin = fin.time().replace(microsecond=0)
        return f"Se ha asignado el servicio {servicio} desde las {inicio} hrs. a las {fin.strftime("%H:%M")} hrs."

    def confirmar(self, motivo, agenda: Agenda):
        if self._estado != "creada":
            raise Exception(f"No se puede confirmar una cita en estado '{self._estado}'")
        if self._duracion_min and self._fin is None:
            raise Exception("No se ha asignado un servicio todavia.")
        if agenda.existe_solape(self.__profesional, self._inicio, self._fin): # Devuelve True si hay solape
            raise Exception("Existe solapamiento entre citas")
        
        self._estado = "confirmada"
        detalle = f"ID Cita: {self.id_cita} | Cliente: {self.__cliente} | Motivo: {motivo}"
        self._registrar_evento(f"Confirmacion cita", detalle)
        return f"Cita {self.id_cita} confirmada con exito."
            
        # valida estado creada, servicio asignado y franja libre;
        # cambia a confirmada; registra evento
        
    def cancelar(self, motivo):
        if self._estado == "cancelada":
            return "La cita ya esta cancelada"
        else:
            detalle = f"ID Cita: {self.id_cita} | Cliente: {self.__cliente} | Motivo: {motivo}"
            self._registrar_evento("Cancelacion cita", detalle)
            self._estado = "cancelada"
            return f"Cita {self.id_cita} cancelada con exito."
        # valida estado (creada/confirmada); cambia a cancelada; registra evento.

    def ver_eventos(self):
        for evento in self._historial_eventos:
            print(evento)

inicio = "21:59"
g = Agenda()
c = Cita("dd","aa",inicio)
print(c.asignar_servicio(CorteCabello()))
print(c.confirmar("www", g))
print(c.cancelar("dd"))

print(c._inicio)
print(c.fin_hora())
c.ver_eventos()