from ejercicio_1.M1_cita import Cita
from ejercicio_1.M2_servicio import Coloracion, CorteCabello
from ejercicio_1.M3_agenda import Agenda
from ejercicio_4.M1_suscriptor import Suscriptor
from ejercicio_4.M2_retiro import Retiro
from ejercicio_4.M3_material import PapelCarton, Plastico, Vidrio
from ejercicio_4.M5_semana import Semana


# inicio = "14:30"
# cliente = "diego"
# pro = "rovin"

# color = Coloracion()
# corte = CorteCabello()
# agenda = Agenda()


# a = Cita(cliente, pro , inicio,)
# print(a.asignar_servicio(color))
# print(a.asignar_servicio(corte))

# print(a.confirmar("confirmacion telefonica", agenda))
# print(a.cancelar("porquesi"))
# a.ver_eventos()

# b = Cita(cliente, pro,"19:00")
# print(b.asignar_servicio(corte))
# print(b.confirmar("sisi", agenda))
# print(agenda.agregar(b))
# print(b.fin)
# agenda.ver_agenda()


sub = Suscriptor("El ombu")
ret = Retiro("13-10-2025")
sem = Semana("10-10-2025", "15-10-2025")
mat = Plastico()

sub1 = Suscriptor("El ombu")
ret1 = Retiro("11-10-2025")
mat1 = Vidrio()

sub2 = Suscriptor("El ombu")
ret2 = Retiro("12-10-2025")
mat2 = PapelCarton()

print(ret.hacer_retiro(sub, mat, 4.5, sem))
try:
    ret.hacer_retiro(sub1,mat,10,sem)
except Exception as e:
    print(e)
try:
    ret.hacer_retiro(sub1,mat,7.5,sem)
except Exception as e:
    print(e)

print(sub1.estado)
print(ret.rectificar_peso(sub1,mat,7.5,sem))
print(ret.hacer_retiro(sub, mat1,2.5,sem))
print(ret2.hacer_retiro(sub, mat1,2.5,sem))
print(ret2.hacer_retiro(sub, mat1,2.5,sem))
print(ret2.hacer_retiro(sub1, mat1,2.5,sem))
print(ret2.hacer_retiro(sub1, mat1,2.5,sem))
print(ret2.hacer_retiro(sub2, mat1,2.5,sem))

print("----")
sem.ver()
print("----")
sub1.ver()
print("----")
sub.ver()
print("----")
sub2.ver()
print("----")
ret.ver()
print("----")
print(sub.saldo_pts, sub1.saldo_pts, sub2.saldo_pts)
print("----")
sem.bono_semanal()

print(sub.saldo_pts, sub1.saldo_pts, sub2.saldo_pts)