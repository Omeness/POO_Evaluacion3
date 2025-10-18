from datetime import datetime
from ejercicio_4.M1_suscriptor import Suscriptor
from ejercicio_4.M2_retiro import Retiro
from ejercicio_4.M3_material import PapelCarton, Plastico, Vidrio
from ejercicio_4.M5_semana import Semana
from funciones import menu, limpiar_pantalla, continuar, buscar_suscriptor, buscar_retiro


lista_sus = [Suscriptor("ddd"), Suscriptor("gggg"), Suscriptor("ffd", "inhabilitado")]

agenda = Semana("13-10-2025", "19-10-2025")
semana = [
    Retiro("13-10-2025"),
    Retiro("14-10-2025"),
    Retiro("15-10-2025"),
    Retiro("16-10-2025"),
    Retiro("17-10-2025"),
    Retiro("18-10-2025", 'validado'),
    Retiro("19-10-2025", 'rechazado')
    ]

while True:
    limpiar_pantalla()
    menu()
    try:
        while True:
            opcion = int(input("Ingresa el numero de opcion: "))
            if opcion < 1 or opcion > 8:
                limpiar_pantalla()
                print("\n[Error] Opcion invalida, ingresa un numero del 1 al 8\n")
                menu()
            else:
                break
        try:
            if opcion == 1:
                limpiar_pantalla()
                print("=== Opcion 1 ===")
                print("Crear suscriptor\n")

                direccion = input("Ingresa la direccion: ")
                sus = Suscriptor(direccion)
                lista_sus.append(sus)
                print("Suscriptor creado con exito")
                continuar()
                
        except Exception as error:
            print("[Error]",error)
            continuar()
            
        if opcion == 2:
            limpiar_pantalla()
            print("=== Opcion 2 ===")
            print("ver puntaje suscriptor\n")
            try:
                id_sus = int(input("Ingresa el ID del suscriptor: "))
                suscriptor = buscar_suscriptor(id_sus, lista_sus)
                    
                if suscriptor is None:
                    print(f"No se encontro al suscriptor '{id_sus}'")
                    continuar()
                else:
                    print("Total puntos:",suscriptor.saldo_pts)
                    continuar()
            except Exception:
                print(f"[Error] ID invalido. Opciones disponibles: {[i.id_sub for i in lista_sus]}")
                continuar()

        if opcion == 3:
            limpiar_pantalla()
            print("=== Opcion 3 ===")
            print("Ver suscriptores\n")

            print(f"Total suscriptores: {len(lista_sus)}")
            for i in lista_sus:
                print(f"ID: {i.id_sub} Puntos: {i.saldo_pts}")
            continuar()

        if opcion == 4:
            limpiar_pantalla()
            print("=== Opcion 4 ===")
            print("Hacer retiro\n")

            try:
                print(agenda)
                dia = datetime.strptime(f"{input("Ingresa la fecha del dia: ")}", "%d-%m-%Y")
                retiro = buscar_retiro(dia, semana)
                
                if retiro is None:
                    raise Exception("La fecha no esta en el rango de la semana")
        
                if retiro.estado == "rechazado":
                    raise Exception("El retiro esta rechazado. Rectificar para cambiar.")

                while True:
                    opcion = int(input("Ingresa el ID del suscriptor: "))
                    sus = buscar_suscriptor(opcion, lista_sus)
                    if sus is None:
                        print("El suscriptor no esta inscrito")
                        print(f"Suscriptores disponibles: {[i.id_sub for i in lista_sus]}")
                    else:
                        break
                
                if sus.estado == "inhabilitado":
                    raise Exception("El suscriptor esta inhabilitado")
                
                while True:
                    materiales = ("plastico", "vidrio", "papel y carton")
                    opcion = input(f"Ingresa el material\n"
                                f"Opciones: plastico, vidrio, papel y carton: ").lower()
                    if opcion not in materiales:
                        print("Opcion invalida, elige una de las tres opciones")
                    else:
                        break
                    
                if opcion == "plastico":
                    opcion = Plastico()
                elif opcion == "vidrio":
                    opcion = Vidrio()
                else:
                    opcion = PapelCarton()

                peso = float(input("Ingresa el peso (decimal > 0): "))
                print(retiro.validar_retiro(sus, opcion, peso, semana)) 
                continuar()

            except Exception as e:
                print("[Error]",e)
                continuar()

        if opcion == 5:
            print("Todavia no se ha implementado esta opcion")
            print("Saliendo del script...")
            break

        if opcion == 6:
            print("Todavia no se ha implementado esta opcion")
            print("Saliendo del script...")
            break

        if opcion == 7:
            print("Todavia no se ha implementado esta opcion")
            print("Saliendo del script...")
            break

        if opcion == 8:
            print("Todavia no se ha implementado esta opcion")
            print("Saliendo del script...")
            break

        if opcion == 9:
            print("Todavia no se ha implementado esta opcion")
            print("Saliendo del script...")
            break
        
        if opcion == 10:
            print("Todavia no se ha implementado esta opcion")
            print("Saliendo del script...")
            break

    except ValueError:
        print("[Error] Debes ingresar un numero entero")
        continuar()