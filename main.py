from ejercicio_1.M1_cita import Cita
from ejercicio_1.M2_servicio import Coloracion, CorteCabello
from ejercicio_1.M3_agenda import Agenda
from ejercicio_4.M1_suscriptor import Suscriptor
from ejercicio_4.M2_retiro import Retiro
from ejercicio_4.M3_material import PapelCarton, Plastico, Vidrio
from ejercicio_4.M5_semana import Semana



print("\n\t==== Ejercicio 1 ====\n")

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

print("\n### Historiales")
lunes.ver_agenda()
cita10.ver_eventos()
cita14.ver_eventos()

# ==== Ejercicio 2 y 3 ====

# No hay ejecucion de los ejercicios porque no los termine. Solo arme la estructura
# pero no me alcanzo el tiempo y preferi priorizar terminar un ejercicio que pudiera entender

print("\n\t==== Ejercicio 4 ====\n")

# CLI visible en interfaz. Aqui solo muestro que funcionan las clases jj

sus1 = Suscriptor("Los Pinos #2211")
sus2 = Suscriptor("Los Pinos #2212")
sus3 = Suscriptor("Los Pinos #2213")
sus4 = Suscriptor("Los Pinos #2214")
sus5 = Suscriptor("Los Pinos #2215", "inhabilitado")

plastico = Plastico()
vidrio = Vidrio()
papel = PapelCarton()

# Fecha en rango
lunes = Retiro("13-10-2025")
jueves = Retiro("16-10-2025")
viernes = Retiro("19-10-2025")

rechazado = Retiro("13-10-2025", "rechazado")

# Fechas fuera de rango -> Error al intentar hacer el retiro
martes = Retiro("12-10-2025")
miercoles = Retiro("20-10-2025")

semana = Semana("13-10-2025","19-10-2025")

print("\n### Semana con error de fechas\n")
try:
    semana_error = Semana("13-10-2025","10-10-2025")
except Exception as e:
    print(e)


print("\n### Intentamos ingresar un retiro rechazado\n")
try:
    rechazado.validar_retiro(sus1, papel, 5, semana)
except Exception as e:
    print(e)


print("\n### Excedemos el peso por material\n")
try:
    lunes.validar_retiro(sus1, papel, 9, semana)
except Exception as e:
    print(e)


print("\n### Ahora tenemos que rectificar el retiro")
print("### Intentaremos con un suscriptor que no este inhabilitado\n")
# omg ya se que esta es la peor manera de rectificar, pero insisto, no tenia tiempo TvT
try:
    lunes.rectificar_peso(sus2, papel, 5, semana)
except Exception as e:
    print(e)


print("\n### Intentaremos con el mismo peso que se habia rechazado\n")
try:
    lunes.rectificar_peso(sus1, papel, 9, semana)
except Exception as e:
    print(e)

print("\n### Rectificamos de manera correcta\n")
print(lunes.rectificar_peso(sus1, papel, 5, semana))

print("\n### Validamos retiros\n")
print(lunes.validar_retiro(sus1, vidrio, 3.5,semana))
print(lunes.validar_retiro(sus2, papel, 4.8, semana))
print(viernes.validar_retiro(sus1, vidrio, 3.5,semana))
print(jueves.validar_retiro(sus1, vidrio, 3.5,semana))

print("\n### Aplicamos el bono\n")
print(semana.bono_semanal())

print("\n### Revisamos eventos\n")
sus1.eventos_suscriptor()
print()
lunes.eventos_retiro()
print()
viernes.eventos_retiro()
print()
jueves.eventos_retiro()









