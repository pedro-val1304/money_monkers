surList = ["Becerra", "Facio", "Jimenez", "Rodriguez", "Gutierrez", "Valenzuela", "Vidrio", "Mora", "Valdivia", "Ibarra", "Ornelas", "Zepeda", "Granados", "Alvarez"]
codeList = ["224164515", "219439208", "220520973", "221925365", "221453145", "221568619", "224164513", "221964573", "216548448", "224164491", " 218466716", "220571586", " 218220776","221851264"]
nameList = ["Emiliano", "Allison","Naomi","Natalia","Pedro","Jose","Diego", "Abril","Grecia","Misael","Alberto","Elias","Angel", "Gloria"]
pList = [80, 90] #Programación
fList = [60, 100] #Física
qList = [70, 80, 100, 90, 100, 90, 100, 90,  ] #Química
cList = [90, 70] #CB
asisList = [15, 16] #Asistencia
absList = [2, 1] #Faltas
ageList = [19, 20] #Edad
carList = ["LTBI", "LTBI"] #Carrera

borrar=str
caP = float
caf=float
caQ = float
caC = float
Pro = float
mod = int
asis = int

while True:
    try:
        print ("1: Agregar nuevo estudiante")
        print ("2: Datos de estudiante")
        print ("3: Eliminar estudiante")
        print ("4: Modificar información de estudiante")
        print ("5: Mostrar lista de estudiantes")
        print ("6: Almacenar las notas de un estudiante")
        print ("7: Promedio de estudiante")
        print ("8: Generar un reporte de notas de un estudiante")
        print ("9: Almacenar asistencia de un estudiante")
        print ("10: Generar un reporte de asistencia de un estudiante")
        print ("11: Para cerrar el programa")
        print ("")
        opcion = int(input("¿Qué desea hacer?: "))

    #Agregar nuevo 1
        if opcion == 1:
            nameList.append(str(input("Ingrese su nombre: "))) #Lo que hace esto es que va a guardar todo en la posición que sigue, en este caso 2.
            surList.append(str(input("Ingrese su apellido: ")))
            codeList.append(str(input("Ingrese su código: ")))
            ageList.append(str(input("Ingrese su edad: ")))
            carList.append(str(input("Ingrese su carrera (LTBI, LCD, LDIA, LCS, LIF): ")))
            pList.append(float(input("Ingrese su calificación de Programación 1: ")))
            fList.append(float(input("Ingrese su calificación de Física: ")))
            qList.append(float(input("Ingrese su calificación de Química: ")))
            cList.append(float(input("Ingrese su calificación de Ciencias Biológicas: ")))
            asisList.append(int(input("Ingrese las asistencias del estudiante: ")))
            absList.append(int(input("Ingrese las faltas del estudiante: ")))

    #Identificar 2
        elif opcion == 2:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                 print("Su nombre es:", nameList[nameList.index(ident)]) #nameList[nameList.index(ident)] Hace que en la lista de nombres se imprima el de la posición del nombre o código que se pone
                 print("Su apellido es:", surList[nameList.index(ident)]) #ident es la variable que se utiliza para saber la posición en la que está el input. Osea, allison es la posición 1
                 print("Su código es:", codeList[nameList.index(ident)]) # entonces se va a imprimir todo lo de las bases de datos de la posición 1
                 print("Su edad es:", ageList[nameList.index(ident)])
                 print("Su carrera es:", carList[nameList.index(ident)])
            elif ident in surList:
                 print("Su nombre es:", nameList[surList.index(ident)])
                 print("Su apellido es:", surList[surList.index(ident)])
                 print("Su código es:", codeList[surList.index(ident)])
                 print("Su edad es:", ageList[surList.index(ident)])
                 print("Su carrera es:", carList[surList.index(ident)])
            elif ident in codeList:
                 print("Su nombre es:", nameList[codeList.index(ident)])
                 print("Su apellido es:", surList[codeList.index(ident)])
                 print("Su código es:", codeList[codeList.index(ident)])
                 print("Su edad es:", ageList[codeList.index(ident)])
                 print("Su carrera es:", carList[codeList.index(ident)])
            else:
                print("El estudiante no se encuentra en la lista")

    #Eliminar 3
        elif opcion == 3:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("El estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)], "ha sido borrado")
                borrar = nameList.index(ident)
                nameList.pop(borrar)
                surList.pop(borrar)
                codeList.pop(borrar)
                pList.pop(borrar)
                fList.pop(borrar)
                qList.pop(borrar)
                cList.pop(borrar)
                asisList.pop(borrar)
                absList.pop(borrar)
                ageList.pop(borrar)
                carList.pop(borrar)

            elif ident in surList:
                print("El estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)], "ha sido borrado")
                borrar = surList.index(ident)
                nameList.pop(borrar)
                surList.pop(borrar)
                codeList.pop(borrar)
                pList.pop(borrar)
                fList.pop(borrar)
                qList.pop(borrar)
                cList.pop(borrar)
                asisList.pop(borrar)
                absList.pop(borrar)
                ageList.pop(borrar)
                carList.pop(borrar)

            elif ident in codeList:
                print("El estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)], "ha sido borrado")
                borrar = codeList.index(ident)
                nameList.pop(borrar)
                surList.pop(borrar)
                codeList.pop(borrar)
                pList.pop(borrar)
                fList.pop(borrar)
                qList.pop(borrar)
                cList.pop(borrar)
                asisList.pop(borrar)
                absList.pop(borrar)
                ageList.pop(borrar)
                carList.pop(borrar)

            else:
                print("El estudiante no se encuentra en la lista")

    #Modificar 4
        elif opcion == 4:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                mod=nameList.index(ident)
                nameList[mod]=input(str("Ingrese nuevo nombre: ")) #Va a modificar todo lo de la posicón en la que esta el ident. Mod es una variable que se iguala a la posición en la
                surList[mod]=input(str("Ingrese nuevo apellido: ")) #que se encuentra el ident. Es decir, si el input esta en la posición 2, se van a modificar todas las listas
                codeList[mod]=input(str("Ingrese nuevo código: ")) #en la posición 2. Se va a modificar la carrera de la posición 2, el nombre de la posición 2 y todas las listas de la posición 2
                ageList[mod]=input(int("Ingrese su nueva edad: "))
                carList[mod]=input(str("Ingrese su nueva carrera: "))
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
                asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                absList[mod]=int(input("Ingrese nuevas faltas: "))
            elif ident in surList:
                mod=surList.index(ident)
                nameList[mod]=input(str("Ingrese nuevo nombre: "))
                surList[mod]=input(str("Ingrese nuevo apellido: "))
                codeList[mod]=input(str("Ingrese nuevo código: "))
                ageList[mod]=input(int("Ingrese su nueva edad: "))
                carList[mod]=input(str("Ingrese su nueva carrera: "))
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
                asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                absList[mod]=int(input("Ingrese nuevas faltas: "))
            elif ident in codeList:
                mod=codeList.index(ident)
                nameList[mod]=input(str("Ingrese nuevo nombre: "))
                surList[mod]=input(str("Ingrese nuevo apellido: "))
                codeList[mod]=input(str("Ingrese nuevo código: "))
                ageList[mod]=input(int("Ingrese su nueva edad: "))
                carList[mod]=input(str("Ingrese su nueva carrera: "))
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
                asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                absList[mod]=int(input("Ingrese nuevas faltas: "))
            else:
                print("El estudiante no se encuentra en la lista")

    #Lista de estudiantes 5
        elif opcion == 5:
            nombre_completo = [f"{nombre} {apellido}" for nombre, apellido in zip(nameList, surList)]
            print(nombre_completo)
            
    #Almacenar calificaciones 6
        elif opcion == 6:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                mod=nameList.index(ident)
                print("Almacenando calificaciones del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
            elif ident in surList:
                mod=surList.index(ident)
                print("Almacenando calificaciones del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
            elif ident in codeList:
                mod=codeList.index(ident)
                print("Almacenando calificaciones del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
            else:
                print("El estudiante no se encuentra en la lista")
                
    #Promedio de estudiante 7
        elif opcion == 7:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                caP = pList[nameList.index(ident)] #Aquí son variables que se igualan a la calificación, definida por la posición en la que el ident encuentra. Como ha estado funcionando el código en general
                caF = fList[nameList.index(ident)]
                caQ = qList[nameList.index(ident)]
                caC = cList[nameList.index(ident)]
                Pro = (caP+caF+caQ+caC)/4
                print("El promedio de", nameList[nameList.index(ident)], surList[nameList.index(ident)], "es:")
                print(Pro)
            elif ident in surList:
                caP = pList[surList.index(ident)]
                caF = fList[surList.index(ident)]
                caQ = qList[surList.index(ident)]
                caC = cList[surList.index(ident)]
                Pro = (caP+caF+caQ+caC)/4
                print("El promedio de", nameList[surList.index(ident)], surList[surList.index(ident)], "es:")
                print(Pro)    
            elif ident in codeList:
                caP = pList[codeList.index(ident)]
                caF = fList[codeList.index(ident)]
                caQ = qList[codeList.index(ident)]
                caC = cList[codeList.index(ident)]
                Pro = (caP+caF+caQ+caC)/4
                print("El promedio de", nameList[codeList.index(ident)], surList[codeList.index(ident)], "es:")
                print(Pro)
            else:
                print("El estudiante no se encuentra en la lista")

    #Generar reporte 8
        elif opcion == 8:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Reporte de calificaciones del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                print("Su calificación de programación 1 es:", pList[nameList.index(ident)])
                print("Su calificación de Física es:", fList[nameList.index(ident)])
                print("Su calificación de Química es:", qList[nameList.index(ident)])
                print("Su calificación de Ciencias Biológicas es:", cList[nameList.index(ident)])
            elif ident in surList:
                print("Reporte de calificaciones del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                print("Su calificación de programación 1 es:", pList[surList.index(ident)])
                print("Su calificación de Física es:", fList[surList.index(ident)])
                print("Su calificación de Química es:", qList[surList.index(ident)])
                print("Su calificación de Ciencias Biológicas es:", cList[surList.index(ident)])
            elif ident in codeList:
                print("Reporte de calificaciones del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                print("Su calificación de programación 1 es:", pList[codeList.index(ident)])
                print("Su calificación de Física es:", fList[codeList.index(ident)])
                print("Su calificación de Química es:", qList[codeList.index(ident)])
                print("Su calificación de Ciencias Biológicas es:", cList[codeList.index(ident)])
            else:
                print("El estudiante no se encuentra en la lista")

    #Asistencia 9
        elif opcion == 9:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                asis=nameList.index(ident)
                print("Almacenando asistencias del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                asisList[asis]=int(input("Ingrese nuevas asistencias: "))
                absList[asis]=int(input("Ingrese nuevas faltas: "))
            elif ident in surList:
                asis=surList.index(ident)
                print("Almacenando asistencias del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                asisList[asis]=int(input("Ingrese nuevas asistencias: "))
                absList[asis]=int(input("Ingrese nuevas faltas: "))
            elif ident in codeList:
                asis=codeList.index(ident)
                print("Almacenando asistencias del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                asisList[asis]=int(input("Ingrese nuevas asistencias: "))
                absList[asis]=int(input("Ingrese nuevas faltas: "))
            else:
                print("El estudiante no se encuentra en la lista")

    #Reporte de Asistencia 10
        elif opcion == 10:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Reporte de asistencias del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                print("Sus asistencias son:", asisList[nameList.index(ident)])
                print("Sus faltas son: ", absList[nameList.index(ident)])
            elif ident in surList:
                print("Reporte de asistencias del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                print("Sus asistencias son:", asisList[surList.index(ident)])
                print("Sus faltas son:", absList[surList.index(ident)])
            elif ident in codeList:
                print("Reporte de asistencias del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                print("Sus asistencias son:", asisList[codeList.index(ident)])
                print("Sus faltas son:", absList[codeList.index(ident)])

    #Cerrar
        elif opcion == 11:
            print("¡Hasta luego!")
            break

        print("---------------------------------------------------------------------")

    except ValueError:
        print("Elija un valor valido")
        print("---------------------------------------------------------------------")
