from datetime import datetime


class Reserva:
    _id_reserva = 100

    def __init__(self, cancha:object, cliente:str, inicio:str, fin:str, estado="creada"):
        if not cliente.split():
            raise Exception("El nombre del cliente no puede estar vacio")
        
        inicio = datetime.strptime(f"{inicio}", "%H:%M")
        fin = datetime.strptime(f"{fin}", "%H:%M")

        if inicio > fin:
            raise Exception(f"La hora de fin debe ser despues de las {inicio} hrs.")

        self.id_reserva = type(self)._id_reserva
        type(self)._id_reserva += 1

        self.cancha = cancha
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        
        # Atributos solo lectura 
        self.estado = estado #{creada, confirmada, cancelada, no_show}
        self.importe = None #(solo lectura; fijado por cotización/confirmación).
        self.desglose_tarife = [] #lista de tramos con {desde, hasta, tipo_tarifa, minutos, valor_hora, subtotal} cuando aplique)
        self.historial_eventos = []

    def cotizar(self, tarifa):
        # calcula y fija importe (solo lectura) y desglose_tarifa; evento cotizada.
        pass

    def confirmar(self, motivo):
        # valida solape y mantención; cambia a confirmada; evento.
        pass

    def cancelar(self, motivo, politica):
        # calcula penalización (politica.penalizacion(horas_previas, importe)), cambia a cancelada; evento con monto
        pass

    def marchar_no_show(self):
        # cambia a no_show (si procede); evento (y penalización si existe política para inasistencia)
        pass