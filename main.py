from ejercicio_1.M1_cita import Cita
from ejercicio_1.M2_servicio import Coloracion, CorteCabello
from ejercicio_1.M3_agenda import Agenda
from ejercicio_4.M1_suscriptor import Suscriptor
from ejercicio_4.M2_retiro import Retiro
from ejercicio_4.M3_material import PapelCarton, Plastico, Vidrio
from ejercicio_4.M5_semana import Semana


# ===== Ejercicio 1 =======

# Creacion de citas

print("\n### Error por estar fuera de horario de atencion\n")
try:
    cita_error1 = Cita("Marisol", "Diego","07:50")
except Exception as error:
    print(error)

try:
    cita_error2 = Cita("Pablo", "Alondra","22:00")
except Exception as error:
    print(error)


cita10 = Cita("Camila", "Rovin","16:15")
cita11 = Cita("Daniela", "Diego","08:30")
cita12 = Cita("Sergio", "Rovin","12:50")
cita13 = Cita("Ana", "Rovin","14:30")
cita14 = Cita("Pedro", "Rovin","16:30")
cita15 = Cita("Miguel", "Diego","18:40")

# Creacion de servicios
corte = CorteCabello()
color = Coloracion()

# Creacion de la agenda
lunes = Agenda()

print("\n### Error al tratar de agregar una cita sin confirmar\n")
try:
    lunes.agregar(cita10)
except Exception as error:
    print(error)

print("\n### Confirmacion y agenda de citas\n")
print(cita10.asignar_servicio(corte))
print(cita10.confirmar("Confirmacion Telefonica", lunes))
print(lunes.agregar(cita10))

cita11.asignar_servicio(color)
cita11.confirmar("Confirmacion Telefonica", lunes)
lunes.agregar(cita11)

cita12.asignar_servicio(color)
cita12.confirmar("Confirmacion Telefonica", lunes)
lunes.agregar(cita12)

cita13.asignar_servicio(corte)
cita13.confirmar("Confirmacion Telefonica", lunes)
lunes.agregar(cita13)

print("\n### Error por solapamiento de citas\n")
try:
    cita14.asignar_servicio(color)
    cita14.confirmar("Confirmacion Telefonica", lunes)
except Exception as error:
    print(error)

print("\n### Error al tratar de confirmar sin haber asignado un servicio\n")
try:
    cita15.confirmar("Confirmacion Telefonica", lunes)
except Exception as error:
    print(error)

print("\n### Cancelacion de cita\n")
print(cita14.cancelar("Solape con otra cita"))

lunes.ver_agenda()
cita10.ver_eventos()
cita14.ver_eventos()