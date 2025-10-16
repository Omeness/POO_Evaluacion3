from ejercicio_1.M1_cita import Cita
from ejercicio_1.M2_servicio import Coloracion, CorteCabello
from ejercicio_1.M3_agenda import Agenda


inicio = "14:30"
cliente = "diego"
pro = "rovin"

color = Coloracion()
corte = CorteCabello()
agenda = Agenda()


a = Cita(cliente, pro , inicio,)
print(a.asignar_servicio(color))
print(a.asignar_servicio(corte))

print(a.confirmar("confirmacion telefonica", agenda))
print(a.cancelar("porquesi"))
a.ver_eventos()

b = Cita(cliente, pro,"19:00")
print(b.asignar_servicio(corte))
print(b.confirmar("sisi", agenda))
print(agenda.agregar(b))
print(b.fin)
agenda.ver_agenda()

