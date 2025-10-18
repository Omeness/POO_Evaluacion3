import os


def menu():
    print("""== Retiro de materiales ==
Escoja una opcion:

1) Crear suscriptor
2) Ver puntos de suscriptor
3) Ver suscriptores
4) Hacer retiro
5) Rectificar retiro
6) Ver semana
7) Aplicar bono semanal
8) Ver registro (suscriptor/retiro)
9) Ver todos los registros
10) Salir
    """)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    print("\nVolviendo al menu...")
    input("Enter para continuar")

def buscar_suscriptor(id_suscriptor, lista_suscriptores):
    suscriptor = None
    for sus in lista_suscriptores:
        if sus.id_sub == id_suscriptor:
            suscriptor = sus
            break
    return suscriptor

def buscar_retiro(fecha, lista_retiros):
    retiro = None
    for r in lista_retiros:
        if fecha == r.fecha:
            retiro = r
            break
    return retiro
