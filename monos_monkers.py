nameList = ["Emi", "Misa"]
surList = ["Bece", "Iba"]
codeList = ["224", "124"]
pList = [80, 90] #Programación
fList = [60, 100] #Física
qList = [70, 80] #Química
cList = [90, 70] #CB
asisList = [15, 16]
absList = [2, 1]

borrar=int
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
        print ("6: Promedio de estudiante")
        print ("7: Generar un reporte de notas de un estudiante")
        print ("8: Almacenar las notas de un estudiante")
        print ("9: Almacenar asistencia de un estudiante")
        print ("10: Generar un reporte de asistencia de un estudiante")
        print ("11: Para cerrar el programa")
        print ("")
        opcion = int(input("¿Qué desea hacer?: "))

    #Agregar nuevo 1
        if opcion == 1:
            nameList.append(str(input("Ingrese su nombre: ")))
            surList.append(str(input("Ingrese su apellido: ")))
            codeList.append(str(input("Ingrese su código: ")))
            pList.append(float(input("Ingrese su calificación de Programación 1: ")))
            fList.append(float(input("Ingrese su calificación de Física: ")))
            qList.append(float(input("Ingrese su calificación de Química: ")))
            cList.append(float(input("Ingrese su calificación de Ciencias Biológicas: ")))
            asisList.append(int(input("Ingrese las asistencias del estudiante: ")))
            absList.append(int(input("Ingrese las faltas del estudiante:")))

    #Identificar 2
        elif opcion == 2:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                 print("Su nombre es:", nameList[nameList.index(ident)])
                 print("Su apellido es:", surList[nameList.index(ident)])
                 print("Su código es:", codeList[nameList.index(ident)])
            elif ident in surList:
                 print("Su nombre es:", nameList[surList.index(ident)])
                 print("Su apellido es:", surList[surList.index(ident)])
                 print("Su código es:", codeList[surList.index(ident)])
            elif ident in codeList:
                 print("Su nombre es:", nameList[codeList.index(ident)])
                 print("Su apellido es:", surList[codeList.index(ident)])
                 print("Su código es:", codeList[codeList.index(ident)])
            else:
                print("El estudiante no se encuentra en la lista")

    #Eliminar 3
        elif opcion == 3:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                borrar = nameList.index(ident)
                print(borrar)         
                nameList.pop(borrar)
                surList.pop(borrar)
                codeList.pop(borrar)
                pList.pop(borrar)
                fList.pop(borrar)
                qList.pop(borrar)
                cList.pop(borrar)
                asisList.pop(borrar)
                absList.pop(borrar)
            elif ident in surList:
                borrar = surList.index(ident)
                print(borrar)     
                nameList.pop(borrar)
                surList.pop(borrar)
                codeList.pop(borrar)
                pList.pop(borrar)
                fList.pop(borrar)
                qList.pop(borrar)
                cList.pop(borrar)
                asisList.pop(borrar)
                absList.pop(borrar)
            elif ident in codeList:
                borrar = codeList.index(ident)
                print(borrar)  
                nameList.pop(borrar)
                surList.pop(borrar)
                codeList.pop(borrar)
                pList.pop(borrar)
                fList.pop(borrar)
                qList.pop(borrar)
                cList.pop(borrar)
                asisList.pop(borrar)
                absList.pop(borrar)
            else:
                print("El estudiante no se encuentra en la lista")
    #Modificar 4
        elif opcion == 4:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Name", ident, "is found in position", nameList.index(ident), "in the name list.")
                mod=nameList.index(ident)
                nameList[mod]=input(str("Ingrese nuevo nombre: "))
                surList[mod]=input(str("Ingrese nuevo apellido: "))
                codeList[mod]=input(str("Ingrese nuevo código: "))
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
                asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                absList[mod]=int(input("Ingrese nuevas faltas: "))
            elif ident in surList:
                print("Name", ident, "is found in position", surList.index(ident), "in the name list.")
                mod=surList.index(ident)
                nameList[mod]=input(str("Ingrese nuevo nombre: "))
                surList[mod]=input(str("Ingrese nuevo apellido: "))
                codeList[mod]=input(str("Ingrese nuevo código: "))
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
                asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                absList[mod]=int(input("Ingrese nuevas faltas: "))
            elif ident in codeList:
                print("Name", ident, "is found in position", codeList.index(ident), "in the name list.")
                mod=codeList.index(ident)
                nameList[mod]=input(str("Ingrese nuevo nombre: "))
                surList[mod]=input(str("Ingrese nuevo apellido: "))
                codeList[mod]=input(str("Ingrese nuevo código: "))
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

    #Promedio de estudiante 6
        elif opcion == 6:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Name", ident, "is found in position", nameList.index(ident), "in the name list.")
                caP = pList[nameList.index(ident)]
                caF = fList[nameList.index(ident)]
                caQ = qList[nameList.index(ident)]
                caC = cList[nameList.index(ident)]
                Pro = (caP+caF+caQ+caC)/4
                print(Pro)
            elif ident in surList:
                print("Surname", ident, "is found in position", surList.index(ident), "in the surname list.")
                caP = pList[surList.index(ident)]
                caF = fList[surList.index(ident)]
                caQ = qList[surList.index(ident)]
                caC = cList[surList.index(ident)]
                Pro = (caP+caF+caQ+caC)/4
                print(Pro)    
            elif ident in codeList:
                print("Code", ident, "is found in position", codeList.index(ident), "in the name list.")
                caP = pList[codeList.index(ident)]
                caF = fList[codeList.index(ident)]
                caQ = qList[codeList.index(ident)]
                caC = cList[codeList.index(ident)]
                Pro = (caP+caF+caQ+caC)/4
                print(Pro)
            else:
                print("El estudiante no se encuentra en la lista")

    #Generar reporte 7
        elif opcion == 7:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Name", ident, "is found in position", nameList.index(ident), "in the name list.")
                print("Su calificación de programación 1 es: ", pList[nameList.index(ident)])
                print("Su calificación de Física es: ", fList[nameList.index(ident)])
                print("Su calificación de Química es: ", qList[nameList.index(ident)])
                print("Su calificación de Ciencias Biológicas es: ", cList[nameList.index(ident)])
            elif ident in surList:
                print("Surname", ident, "is found in position", surList.index(ident), "in the surname list.")
                print("Su calificación de programación 1 es: ", pList[surList.index(ident)])
                print("Su calificación de Física es: ", fList[surList.index(ident)])
                print("Su calificación de Química es: ", qList[surList.index(ident)])
                print("Su calificación de Ciencias Biológicas es: ", cList[surList.index(ident)])
            elif ident in codeList:
                print("Code", ident, "is found in position", codeList.index(ident), "in the name list.")
                print("Su calificación de programación 1 es: ", pList[codeList.index(ident)])
                print("Su calificación de Física es: ", fList[codeList.index(ident)])
                print("Su calificación de Química es: ", qList[codeList.index(ident)])
                print("Su calificación de Ciencias Biológicas es: ", cList[codeList.index(ident)])
            else:
                print("El estudiante no se encuentra en la lista")

    #Almacenar calificaciones 8
        elif opcion == 8:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Name", ident, "is found in position", nameList.index(ident), "in the name list.")
                mod=nameList.index(ident)
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
            elif ident in surList:
                print("Name", ident, "is found in position", surList.index(ident), "in the name list.")
                mod=surList.index(ident)
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
            elif ident in codeList:
                print("Name", ident, "is found in position", codeList.index(ident), "in the name list.")
                mod=codeList.index(ident)
                pList[mod]=float(input("Ingrese nueva calificación de Programación 1: "))
                fList[mod]=float(input("Ingrese nueva calificación de Física: "))
                qList[mod]=float(input("Ingrese nueva calificación de Química: "))
                cList[mod]=float(input("Ingrese nueva calificación de Biología: "))
            else:
                print("El estudiante no se encuentra en la lista")

    #Asistencia 9
        elif opcion == 9:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Name", ident, "is found in position", nameList.index(ident), "in the name list.")
                asis=nameList.index(ident)
                asisList[asis]=int(input("Ingrese nuevas asistencias: "))
                absList[asis]=int(input("Ingrese nuevas faltas: "))
            elif ident in surList:
                print("Name", ident, "is found in position", surList.index(ident), "in the name list.")
                asis=surList.index(ident)
                asisList[asis]=int(input("Ingrese nuevas asistencias: "))
                absList[asis]=int(input("Ingrese nuevas faltas: "))
            elif ident in codeList:
                print("Name", ident, "is found in position", codeList.index(ident), "in the name list.")
                asis=codeList.index(ident)
                asisList[asis]=int(input("Ingrese nuevas asistencias: "))
                absList[asis]=int(input("Ingrese nuevas faltas: "))
            else:
                print("El estudiante no se encuentra en la lista")

    #Reporte de Asistencia 10
        elif opcion == 10:
            ident = input("Ingresa el identificador: ")
            if ident in nameList:
                print("Name", ident, "is found in position", nameList.index(ident), "in the name list.")
                print("Sus asistencias son: ", asisList[nameList.index(ident)])
                print("Sus faltas son: ", absList[nameList.index(ident)])
            elif ident in surList:
                print("Surname", ident, "is found in position", surList.index(ident), "in the surname list.")
                print("Sus asistencias son: ", asisList[surList.index(ident)])
                print("Sus faltas son: ", absList[surList.index(ident)])
            elif ident in codeList:
                print("Code", ident, "is found in position", codeList.index(ident), "in the name list.")
                print("Sus asistencias son: ", asisList[codeList.index(ident)])
                print("Sus faltas son: ", absList[codeList.index(ident)])

    #Cerrar
        elif opcion == 11:
            print("¡Hasta luego!")
            break

        print("---------------------------------------------------------------------")

    except ValueError:
        print("Elija un valor valido")
        print("---------------------------------------------------------------------")
