# Modelo 1 — Suscriptor
# Propósito: titular del servicio y acumulador de puntos.
# Datos mínimos
# • id_suscriptor (único)
# • direccion (string no vacío)
# • saldo_puntos (solo lectura, ≥ 0)
# • estado ∈ {habilitado, inhabilitado} (por defecto habilitado)
# • historial_eventos (solo lectura): {timestamp, tipo, detalle}
# Derivados (solo lectura)
# • retiros_validados_semana (conteo en la semana calendario vigente)

from datetime import datetime


class Suscriptor:
    _id_sub = 10

    def __init__(self, direccion:str, estado="habilitado"):
        'titular del servicio y acumulador de puntos.'

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

    # Con este metodo tambien registraremos los retiros hechos al suscriptor
    def registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(f"[{fecha}] [{tipo}] [{detalle}]")

    @property
    def saldo_pts(self):
        return self._saldo_pts
    
    @saldo_pts.setter
    def _sumar_pts(self, puntos):
        if puntos <= 0:
            raise Exception("El valor de los puntos a agregar debe ser mayor a cero")
        
        detalle = f"Puntos anteriores: {self._saldo_pts}. Nuevo saldo: {self._saldo_pts + puntos}"
        self.registrar_evento("Actualizacion Puntos", detalle)
        self._saldo_pts += puntos
        return f"Puntos asignados con exito. Sumas {puntos} nuevos!"
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def cambiar_estado(self, motivo):
        if self._estado == "habilitado":
            self._estado = "inhabilitado"
            self.registrar_evento("Cambio Estado a inhabilitado", motivo)
        else:
            self._estado = "habilitado"
            self.registrar_evento("Cambio Estado a habilitado", motivo)

    def ver(self):
        for i in self._historial_eventos:
            print(i)

    def __str__(self):
        return f'ID Suscriptor: {self.id_sub}'