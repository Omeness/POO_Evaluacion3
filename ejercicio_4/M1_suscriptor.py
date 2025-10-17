from datetime import datetime


class Suscriptor:
    _id_sub = 10

    def __init__(self, direccion:str, estado="habilitado"):
        """titular del servicio y acumulador de puntos."""

        # Validaciones
        if not direccion.split():
            raise Exception("La direccion no puede estar vacia")

        self.id_sub = type(self)._id_sub
        type(self)._id_sub += 1

        # Keepit safe budy
        self.__direccion = direccion

        # Solo lectura:
        self._saldo_pts = 0
        self._estado = estado
        self._historial_eventos = []

    # Registra eventos en el historial
    def _registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(f"[{fecha}] [{tipo}] [{detalle}]")

    @property
    def saldo_pts(self):
        return self._saldo_pts
    
    @property
    def estado(self):
        return self._estado
    
    def eventos_suscriptor(self):
        if not self._historial_eventos:
            print("\nNo hay registros todavia")
        else:
            print(f"\t--- Historial Suscriptor ID: {self.id_sub} ---")
            print(f"Total registros: {len(self._historial_eventos)}\n")
            for evento in self._historial_eventos:
                print(evento)
            print("\n* Fin registros *")

    def __str__(self):
        return f'ID Suscriptor: {self.id_sub}'