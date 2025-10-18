"""
Funciones de uso interno en Retiro y Semana, sentia que era mejor que no hubiera un acceso directo a estas 
a traves del objeto y que era mejor sacarlas y usarlas dentro de otras clases y que las modificaciones 
fueran de manera indirecta
"""


def fecha_en_rango(fecha, semana:object):
    """Verifica que la fecha esté dentro del rango de la semana"""

    if fecha >= semana.inicio and fecha <= semana.fin:
        return True
    return False


def registrar_retiro(semana:object, suscriptor:object):
    """Registra en Semana los retiros hechos por el suscriptor"""

    semana._retiros.append(suscriptor)


def cambiar_estado(suscriptor, motivo):
    """Cambia el estado del suscriptor"""

    if suscriptor.estado == "habilitado":
        suscriptor._estado = "inhabilitado"
        suscriptor._registrar_evento("Cambio Estado a inhabilitado", motivo)
    else:
        suscriptor._estado = "habilitado"
        suscriptor._registrar_evento("Cambio Estado a habilitado", motivo)


def sumar_pts(suscriptor, puntos):
    """Suma puntos al suscriptor"""

    detalle = f"Puntos anteriores: {suscriptor.saldo_pts}. Nuevo saldo: {suscriptor.saldo_pts + puntos}"
    suscriptor._registrar_evento("Actualizacion Puntos", detalle)
    suscriptor._saldo_pts += puntos
    return f"Puntos asignados con exito. Sumas {puntos} nuevos!"


def menor_igual_cero(num) -> bool:
    """Devuelve True si el numero es menor o igual a cero"""
    if num <= 0:
        return True
    return False