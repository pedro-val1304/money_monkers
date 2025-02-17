C_B = [9.8, 8.9, 7.7]
F_B = [9.8, 8.9, 7.7]
Q_U = [9.8, 8.9, 7.7]
x = -1
y = -1
#Nota los primeros 3 nombres no son modificalbles, son ejemplo, no mover
alumnos = {"Juan Gonzales": f"Ciencias biológicas: {C_B[0]} Física biomédica: {F_B[0]} Química bilógica: {Q_U[0]}",
           "Carlos Perez" : f"Ciencias biológicas: {C_B[1]} Física biomédica: {F_B[1]} Química bilógica: {Q_U[1]}",
           "Luis Sanchez" : f"Ciencias biológicas: {C_B[2]} Física biomédica: {F_B[2]} Química bilógica: {Q_U[2]}",
    }


while True:
    action = int(input('\n'"1. Agregar alumno"'\n'
                   "2. Eliminar alumno"'\n'
                   "3. Cambiar calificacoines"'\n'
                   "4. Buscar alumno"'\n'
                   "5. Salir"'\n'
                   "Qué desaseas hacer?"'\n'))
                   
    for key, value in alumnos.items():
        print(key, ":", value)


#Agregar al diccionario
    if action == 1:
        for key in alumnos.keys():
            x +=1
            y +=1
        x +=1
        #print (x)
        #print (y)
        nombre_nuevo = input(str("Nombre del alumno: "))
        C_B.append (float(input("Calfición Ciencias biológicas: ")))
        F_B.append (float(input("Calificación Fisica biólogica: ")))
        Q_U.append (float(input("Calificación Química: ")))
        print (Q_U)
        print (F_B)
        print (C_B)
        cal_nueva = f"Ciencias biológicas: {C_B[x]} Física biomédica: {F_B[x]} Química bilógica: {Q_U[x]}",
        alumnos.update({nombre_nuevo:cal_nueva })
        x = -1
        y = -1
        for key, value in alumnos.items():
            print (key, ":", value)
#Eliminar alumno
    elif action == 2:
        nombre_elim = input(str("Nombre del alumno: "))
        for key in alumnos.keys():
            x +=1
            y +=1
            if key == nombre_elim:
                break
        alumnos.update({nombre_elim:"/////"})
        alumnos[f"////"] = alumnos[nombre_elim]
        del alumnos[nombre_elim]
        for key, value in alumnos.items():
            print (key, ":", value)
        x = -1
        y = -1
#Actualizar alumno    
    elif action == 3:
        nombre_mod = input(str("Nombre del alumno: "))
        for key in alumnos.keys():
            x +=1
            y +=1
            if key == nombre_mod:
                break
        print (x)
        C_B[x]= float(input("Calfición Ciencias biológicas: "))
        F_B[x]= float(input("Calificación Fisica biólogica: "))
        Q_U[x]= float(input("Calificación Química: "))
        cal_mod = f"Ciencias biológicas: {C_B[x]} Física biomédica: {F_B[x]} Química bilógica: {Q_U[x]}",
        alumnos.update({nombre_mod:cal_mod})
        for key, value in alumnos.items():
            print (key, ":", value)
        x = -1
        y = -1

# Consultar califiación
    elif action == 4:
        print("Calificaciones: ", alumnos.get(input(str( "Alumnos: "))))

    elif action == 5:
        print ("Hasta luego")
        break
    else:
        print ("Opción no valida")

