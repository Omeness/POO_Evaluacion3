from datetime import datetime


# sorri I quit

class Colaborador:
    # A diferencia del primer ejercicio, aqui el historial de eventos es por clase.
    # Asi podemos acceder a todos lo eventos registrados
    _id_colaborador = 10
    _historial_eventos = []

    def __init__(self, nombre:str, horas_semana_max:int, preferencia:str):
        'Persona elegible para cubrir franjas del plan semanal'

        # Validaciones de atributos
        if not nombre.split():
            raise Exception("EL nombre no puede estar vacio")
        if not isinstance(horas_semana_max,int):
            raise Exception("La cantidad de horas debe ser un numero entero")
        if horas_semana_max <= 0:
            raise Exception("La cantidad de horas debe ser mayor a cero")

        self.id_colaborador = type(self)._id_colaborador
        type(self)._id_colaborador += 1

        self.nombre = nombre
        self.horas_semana_max = horas_semana_max
        self.preferencia = preferencia

        # Solo lectura
        self.no_disponible = []
        self._horas_asignadas_semana = 0

    def registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        type(self)._historial_eventos.append(f"[{fecha}] [{tipo}] [{detalle}]")    

