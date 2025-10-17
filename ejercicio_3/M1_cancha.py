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