from datetime import datetime, timedelta


class Test:
    def __init__(self,nn, num_id, ini, fin):
        self.nn = nn
        self.num_id = num_id
        self.ini =ini
        self.fin = fin
        self.lt = []

    def solape(self, item):
        solape = None
        for obj in self.lt:
            if item.num_id == obj.num_id:
                if item.ini < obj.fin and item.fin > obj.ini:
                    solape = f"[ix:{obj.nn} {item.nn}] {item.ini} < {obj.fin} y {item.fin} > {obj.ini}"
        if solape is None:
            return False
        else:
            print(solape)
            return True
        
    def agregar(self, item):
        self.lt.append(item)

mom = Test(0,0,100,100)

f = Test(6,1,18,19)
a = Test(1,1,10,15)

b = Test(2, 1,16,17)
c = Test(3, 1,17.5,19)
d = Test(4,4,17,21)
e = Test(5,4,22,23)

g = Test(7,4,18,22)
#mom.agregar(a)
mom.agregar(b)
mom.agregar(c)
mom.agregar(d)
mom.agregar(e)
mom.agregar(f)

mom.solape(g)
mom.solape(a)
# if a.num_id in [x.num_id for x in lt]:
#     print("sis")
# else:
#     print("non") 

tiempo1 = datetime.strptime("19:45", "%H:%M")
tiempo2 = datetime.strptime("19:55", "%H:%M")
suma = timedelta(minutes=30)
total = tiempo1 + suma
print(total)
if tiempo1 > tiempo2:
    print(tiempo1)
else:
    print(tiempo2)

print("\n-----\n")


# fecha en formato legible (string)
fecha_str = datetime.strptime("11-10-2025", "%d-%m-%Y").strftime("%d-%m-%Y")
print(fecha_str)

fecha = datetime.strptime("16-10-2025", "%d-%m-%Y")

lunes = datetime.strptime("13-10-2025", "%d-%m-%Y")
domingo = lunes + timedelta(days=6)

print(lunes)
print(domingo)

if fecha > lunes and fecha < domingo:
    print("fecha dentro de la semana")
else:
    print("no en semana")

print(fecha.strftime("%m"))

