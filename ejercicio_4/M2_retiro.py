# Modelo 2 — Retiro
# Propósito: registro de material entregado para reciclaje.
# Datos mínimos
# • id_retiro (único)
# • suscriptor (ref. a Suscriptor)
# • fecha (datetime)
# • material (ref. a Material)
# • kg (decimal > 0)
# • estado ∈ {registrado, validado, rechazado} (por defecto registrado)
# • historial_eventos (solo lectura): {timestamp, tipo, detalle}
# Derivados (solo lectura)
# • puntos_calculados (≥ 0; definido al validar)
# • fecha_ultimo_cambio (último timestamp del historial)

from datetime import datetime
from math import trunc


class Retiro:
    _id_retiro = 100

    def __init__(self, fecha:str, estado="registrado"):
        """Registro de material entregado para reciclaje.

        formato fecha: 'dd-mm-yyyy'
        """

        self.id_retiro = type(self)._id_retiro
        type(self)._id_retiro += 1

        self.fecha = datetime.strptime(f"{fecha}", "%d-%m-%Y")

        # Solo lectura
        self._estado = estado
        self._historial_eventos = []

    def _registrar_evento(self, tipo, detalle):
        fecha = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        self._historial_eventos.append(f"[{fecha}] [{tipo}] [{detalle}]")

    @property
    def estado(self):
        return self._estado
    
    def __fecha_en_rango(self, semana:object):
        'Verifica que la fecha de retiro esté dentro del rango de la semana'

        if self._estado == "rechazado":
            raise Exception("No se puede verificar. El retiro esta rechazado")
        
        if self.fecha > semana.inicio and self.fecha < semana.fin:
            return True
        return False
    
    def __registrar_retiro(self, semana:object, suscriptor:object):
        if suscriptor.estado == "inhabilitado":
            raise Exception("No se pueden registrar suscriptores inhabilitados")
        semana._retiros.append(suscriptor)
    
    def hacer_retiro(self, suscriptor: object, material:object, peso:float, semana: object) -> str:
        """
        Si el peso excede el maximo el retiro cambiará a rechazado y el suscriptor quedará 
        inhabilitado.
         
        Se deberá rectificar el peso para habilitar al suscriptor.
        """
        id_s = suscriptor.id_sub
        if peso <= 0: 
            return "El peso debe ser mayor a cero"
        if suscriptor.estado == "inhabilitado":
            raise Exception("El suscriptor esta inhabilitado")
        if material.max_kg_por_bolsa() < peso:
            self._estado = "rechazado"
            suscriptor.cambiar_estado = "Retiro rechazado"
            self._registrar_evento("Retiro Rechazado", f"Suscriptor ID : {id_s} | Peso excede el limite")
            raise Exception("El peso excede el maximo permitido. Se rechazara el retiro")
        if not self.__fecha_en_rango(semana):
            return "La fecha no esta dentro del rango de la semana"
        
        self._estado = "validado"

        puntos = trunc(material.puntos(peso))
        suscriptor._sumar_pts = puntos
        fecha = self.fecha.strftime("%d-%m-%Y")
        
        self.__registrar_retiro(semana,suscriptor)
        suscriptor.registrar_evento("Retiro realizado", f"Material: {material} | Fecha: {fecha}")
        self._registrar_evento("Retiro Validado", f"Suscriptor ID : {id_s} | Material: {material} | Fecha: {fecha}")
        return "Retiro realizado con exito"
    
    def rectificar_peso(self, suscriptor: object, material:object, peso:float, semana: object):
        """
        Solo se pueden rectificar retiros rechazados y/o suscriptores inhabilitados
        """
        if self._estado != "rechazado":
            return "Solo se pueden rectificar retiros rechazados"
        if suscriptor.estado == "habilitado":
            return "Solo se pueden rectificar retiros de suscriptores inhabilitados"
        if material.max_kg_por_bolsa() < peso:
            return(f"El peso sigue exediendo el maximo de {material.max_kg_por_bolsa()}. "
                            f"Intente de nuevo")
        
        suscriptor.cambiar_estado = "Rectificacion peso retiro"
        self._estado = "validado"
        self.hacer_retiro(suscriptor, material, peso, semana)
        return "Retiro rectificado con exito"
        
    def ver(self):
        for i in self._historial_eventos:
            print(i)
