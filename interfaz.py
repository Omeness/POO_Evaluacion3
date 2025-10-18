from datetime import datetime
from ejercicio_4.M1_suscriptor import Suscriptor
from ejercicio_4.M2_retiro import Retiro
from ejercicio_4.M3_material import PapelCarton, Plastico, Vidrio
from ejercicio_4.M5_semana import Semana
from funciones import menu, limpiar_pantalla, continuar, buscar_suscriptor, buscar_retiro


lista_sus = [Suscriptor("El mirador #213"), Suscriptor("El canelo #453"), Suscriptor("Miraflores #456")]

agenda = Semana("13-10-2025", "19-10-2025")

retiros = [
    Retiro("13-10-2025"),
    Retiro("14-10-2025"),
    Retiro("15-10-2025"),
    Retiro("16-10-2025"),
    Retiro("17-10-2025"),
    Retiro("18-10-2025"),
    Retiro("19-10-2025")
    ]

while True:
    limpiar_pantalla()
    menu()
    try:
        while True:
            opcion = int(input("Ingresa el numero de opcion: "))

            if opcion < 1 or opcion > 10:
                limpiar_pantalla()
                print("\n[Error] Opcion invalida, ingresa un numero del 1 al 10\n")
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
                retiro = buscar_retiro(dia, retiros)
                
                if retiro is None:
                    raise Exception("La fecha no esta en el rango de la semana")
        
                if retiro.estado == "rechazado":
                    raise Exception("El retiro esta rechazado. Rectificar para cambiar.")

                while True:
                    id_susb = int(input("Ingresa el ID del suscriptor: "))
                    sus = buscar_suscriptor(id_susb, lista_sus)
                    if sus is None:
                        print("El suscriptor no esta inscrito")
                        print(f"Suscriptores disponibles: {[i.id_sub for i in lista_sus]}")
                    else:
                        break
                
                if sus.estado == "inhabilitado":
                    raise Exception("El suscriptor esta inhabilitado")
                
                while True:
                    materiales = ("plastico", "vidrio", "papel y carton")
                    material = input(f"Ingresa el material\n"
                                f"Opciones: plastico, vidrio, papel y carton: ").lower()
                    if material not in materiales:
                        print("Opcion invalida, elige una de las tres opciones")
                    else:
                        break
                    
                if material == "plastico":
                    material = Plastico()
                elif material == "vidrio":
                    material = Vidrio()
                else:
                    material = PapelCarton()

                peso = float(input("Ingresa el peso (decimal > 0): "))
                print(retiro.validar_retiro(sus, material, peso, agenda)) 
                continuar()

            except Exception as e:
                print("[Error]",e)
                continuar()

        if opcion == 5:
            limpiar_pantalla()
            print("=== Opcion 5 ===")
            print("Rectificar retiro\n")

            try:
                dia = datetime.strptime(f"{input("Ingresa la fecha del dia: ")}", "%d-%m-%Y")
                retiro = buscar_retiro(dia, retiros)
                
                if retiro is None:
                    raise Exception("La fecha no esta en el rango de la semana")

                while True:
                    id_susb = int(input("Ingresa el ID del suscriptor: "))
                    sus = buscar_suscriptor(id_susb, lista_sus)
                    if sus is None:
                        print("El suscriptor no esta inscrito")
                        print(f"Suscriptores disponibles: {[i.id_sub for i in lista_sus]}")
                    else:
                        break
                
                while True:
                    materiales = ("plastico", "vidrio", "papel y carton")
                    material = input(f"Ingresa el material\n"
                                f"Opciones: plastico, vidrio, papel y carton: ").lower()
                    if material not in materiales:
                        print("Opcion invalida, elige una de las tres opciones")
                    else:
                        break
                    
                if material == "plastico":
                    material = Plastico()
                elif material == "vidrio":
                    material = Vidrio()
                else:
                    material = PapelCarton()   

                peso = float(input("Ingresa el peso (decimal > 0): "))

                try:
                    print(retiro.rectificar_peso(sus, material, peso, agenda))
                    continuar()

                except Exception as e:
                    print(e)
                    continuar()
                
            except Exception as e:
                print(e) 
                continuar()          

        if opcion == 6:
            limpiar_pantalla()
            print("=== Opcion 6 ===")
            print("Ver semana\n")

            print(agenda,"\n")

            for i in retiros:
                print(f"{i.fecha.strftime("%A"):10}",i.fecha.strftime("%d-%m-%Y"))
            continuar()  

        if opcion == 7:
            limpiar_pantalla()
            print("=== Opcion 7 ===")
            print("Aplicar Bono\n")

            print("Seguro que quieres aplicar el bono?")
            bono = input("'s' para aplicar, cualquier otra letra para cancelar: ").lower()
            if bono == 's':
                print(agenda.bono_semanal())
                continuar()
            else:
                print("Bono cancelado")
                continuar()

        if opcion == 8:
            limpiar_pantalla()
            print("=== Opcion 8 ===")
            print("Ver registros\n")

            print("Ver registros de fecha(1) o suscriptor(2)?")
            op = input("Elige una opcion: ")

            if op == '1':
                while True:
                    dia = datetime.strptime(f"{input("Ingresa la fecha del dia: ")}", "%d-%m-%Y")
                    retiro = buscar_retiro(dia, retiros)
                    if retiro is None:
                        print("La fecha no esta en rango")
                        print(agenda)
                    else:
                        break
                retiro.eventos_retiro()
                continuar()

            elif op == '2':
                while True:
                    op_id = int(input("Ingresa el ID del suscriptor: "))
                    sus = buscar_suscriptor(op_id, lista_sus)
                    if sus is None:
                        print("El suscriptor no esta inscrito")
                        print(f"Suscriptores disponibles: {[i.id_sub for i in lista_sus]}")
                    else:
                        break
                sus.eventos_suscriptor()
                continuar()
            
            else:
                print("Opcion invalida")
                continuar()
                    
        if opcion == 9:
            limpiar_pantalla()
            print("=== Opcion 9 ===")
            print("Ver todos los registro\n")

            check = None
            for i in retiros:
                if i._historial_eventos:
                    i.eventos_retiro()
                    print()
                    check = 1

            for i in lista_sus:
                if i._historial_eventos:
                    i.eventos_suscriptor()
                    print()
                    check = 1

            if check is None: print("No hay registros")
            continuar()
        
        if opcion == 10:
            limpiar_pantalla()
            print("-----------------------")
            print("\nSee you in space cowboy\n")
            input("Saliendo...")
            break

    except ValueError:
        print("[Error] Debes ingresar un numero entero")
        continuar()