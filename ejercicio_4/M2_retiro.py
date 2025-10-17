from datetime import datetime
from math import trunc
from .M5_semana import Semana
from .M3_material import Material
from .M1_suscriptor import Suscriptor
from .validaciones import fecha_en_rango, registrar_retiro, cambiar_estado, sumar_pts


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
    
    def validar_retiro(self, suscriptor:Suscriptor, material:Material, peso:float, semana:Semana) -> str:
        """
        Si el peso excede el maximo el retiro cambiará a rechazado y el suscriptor quedará 
        inhabilitado.
         
        Se deberá rectificar el peso para habilitar al suscriptor.
        """
        # Meterial verifica que el peso sea mayor a cero
        id_s = suscriptor.id_sub
        if self._estado == "rechazado":
            raise Exception("No se puede verificar. El retiro esta rechazado")
        if suscriptor.estado == "inhabilitado":
            raise Exception("El suscriptor esta inhabilitado")
        if material.max_kg_por_bolsa() < peso:
            self._estado = "rechazado"
            cambiar_estado(suscriptor,"Retiro rechazado")
            self._registrar_evento("Retiro Rechazado", f"Suscriptor ID : {id_s} | Peso excede el limite")
            raise Exception("El peso excede el maximo permitido. Se rechazara el retiro")
        if not fecha_en_rango(self.fecha, semana):
            return "La fecha no esta dentro del rango de la semana"
        
        self._estado = "validado"

        puntos = trunc(material.puntos(peso))
        sumar_pts(suscriptor, puntos)
        fecha = self.fecha.strftime("%d-%m-%Y")
        
        registrar_retiro(semana,suscriptor)
        suscriptor._registrar_evento("Retiro realizado", f"Material: {material} | Fecha: {fecha}")
        self._registrar_evento("Retiro Validado", f"Suscriptor ID : {id_s} | Material: {material} | Fecha: {fecha}")
        return "Retiro realizado con exito"
    
    def rectificar_peso(self, suscriptor:Suscriptor, material:Material, peso:float, semana:Semana):
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
        
        cambiar_estado(suscriptor,"Rectificacion peso retiro")
        self._estado = "validado"
        self.validar_retiro(suscriptor, material, peso, semana)
        return "Retiro rectificado con exito"
        
    def eventos_retiro(self):
        if not self._historial_eventos:
            print("\nNo hay registros todavia")
        else:
            print("\t--- Historial Retiros ---")
            print(f"Total registros: {len(self._historial_eventos)}\n")
            for evento in self._historial_eventos:
                print(evento)
            print("\n* Fin registros *")


