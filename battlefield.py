from datetime import datetime, timedelta
from typing import Optional


# class Cita:
#     _id_cita = 10
#     # tiempo minimo de anticipacion para crear una cita
#     _MIN_ANTICIPACION = timedelta(minutes=30)

#     def __init__(self, cliente, profesional, inicio: datetime, estado="creada"):

#         # Validaciones de los atributos
#         if not cliente.split():
#             raise ErrorCita("El nombre de cliente no puede estar vacio")
#         if not profesional.split():
#             raise ErrorCita("El nombre del profesional no puede estar vacio")
        
#         _ahora = datetime.now()
#         if _ahora < inicio + self._MIN_ANTICIPACION:
#             raise ErrorCita("Las citas deben tomarse con 30 minutos de anticipacion")

class Test:
    @property
    def duracion(self):
        return 30
    def nn(self, entero: Optional[int]):
        if entero:
            print("entero")
        else:
            print("no hay pan")

c = Test()

test = None
ahora = datetime.now()
min = timedelta(minutes=c.duracion)
inicio = datetime.strptime("19:30", "%H:%M")
fin = inicio+min
if ahora < inicio:
    print("papa")
else:
    print("caca")
test = fin
print("------")
print(ahora.strftime("%H:%M"))
print("------")
print(inicio.strftime("%H:%M"))
print("------")
print(ahora+min)
print("------")
print(inicio+min)
print("------")
print(fin.strftime("%H:%M"))
print(test)
