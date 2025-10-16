from datetime import datetime, timedelta


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
        
        # Horario de agenda, no se pueden tomar horas fuera de este horario
        APERTURA = datetime.strptime("08:00", "%H:%M")
        CIERRE = datetime.strptime("19:00", "%H:%M")
        
        if inicio < APERTURA or inicio > CIERRE:
            raise Exception(f"No se pueden crear citas fuera del horario de agenda "
                            f"({APERTURA.strftime("%H:%M")} - {CIERRE.strftime("%H:%M")})")

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
        self._servicio = None

    def _registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(f"[{fecha}] [{tipo}] [{detalle}]")

    @property
    def profesional(self):
        return self.__profesional
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def inicio(self):
        return self._inicio
    
    @property
    def fin(self):
        return self._fin
    
    @property
    def servicio(self):
        return self._servicio

    def asignar_servicio(self, servicio: object):
        if self._estado != "creada":
            raise Exception(f"No se puede asignar servicio a una cita en estado'{self._estado}'")
        if servicio.duracion_min <= 0:
            raise Exception("La duracion del servicio debe ser mayor a cero")
        
        fin = self._inicio + timedelta(minutes=servicio.duracion_min)
        inicio = self._inicio.strftime("%H:%M")

        detalle = f'Hora inicio: {inicio} | Hora fin: {fin.strftime("%H:%M")} | Profesional: {self.__profesional}'
        self._registrar_evento(f"Servicio asignado: {servicio}", detalle)
        self._duracion_min = timedelta(minutes=servicio.duracion_min)
        self._fin = fin
        self._servicio = servicio
        return f"Se ha asignado el servicio {servicio} desde las {inicio} hrs. a las {fin.strftime("%H:%M")} hrs."

    def confirmar(self, motivo, agenda: object):
        if self._estado != "creada":
            raise Exception(f"No se puede confirmar una cita en estado '{self._estado}'")
        if self._servicio is None:
            raise Exception("Se debe asignar un servicio antes de confirmar la cita")
        if agenda.existe_solape(self.__profesional, self._inicio, self._fin):
            raise Exception(f"Existe solapamiento con cita {agenda.cita_solapada}")
        
        self._estado = "confirmada"
        detalle = f"ID Cita: {self.id_cita} | Cliente: {self.__cliente} | Motivo: {motivo}"
        self._registrar_evento(f"Confirmacion cita", detalle)
        return f"Cita {self.id_cita} confirmada con exito."
        
    def cancelar(self, motivo):
        if self._estado == "cancelada":
            return "La cita ya esta cancelada"
        else:
            detalle = f"ID Cita: {self.id_cita} | Cliente: {self.__cliente} | Motivo: {motivo}"
            self._registrar_evento("Cancelacion cita", detalle)
            self._estado = "cancelada"
            return f"Cita {self.id_cita} cancelada con exito."

    def ver_eventos(self):
        for evento in self._historial_eventos:
            print(evento)
