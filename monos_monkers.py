nombre_alumno = {

}
edad_alumno = {

}
codigo_alumno = {

}
carrera_alumno = {

}
notas_alumno = {

}
nombre_alumno = {

}
apellido_alumno = {

}


#Menú de opciones
while True:
    print("\n¿Qué desea hacer?")
    print("1. Buscar por nombre al alumno: ")
    print("2. Buscar por apellidos al alumno: ")
    print("3. Buscar por código al alumno: ")
    print("4. Añadir estudiante: ")
    print("5. Eliminar alumno.")
    print("6. Modificar información del alumno.")
    print("7. Mostrar lista de alumnos.")
    
    
    opcion = int(input("Ingrese una opción (1-6): "))
# If representa la opción que se escogio
#hay que poner el codigo y la carrera del alumno donde dice codigo_alumno y carrera_alumno
    if opcion == 1:
        nombre = input("Ingrese el nombre alumno ")
        if nombre in nombre_alumno: 
            print(f"El nombre del alumno es:{nombre_alumno}, su código es: {codigo_alumno} y su carrera es: {carrera_alumno}")
        else:
            print("Lo siento, no hay un alumno con ese nombre en la base de datos.")

    if opcion == 2:
        apellido = input("Ingrese el apellido del alumno ")
        if apellido in apellido_alumno: 
            print(f"El nombre del alumno es:{nombre_alumno} {apellido:alumno}, su código es: {codigo_alumno} y su carrera es: {carrera_alumno}")
        else:
            print("Lo siento, no hay un alumno con ese nombre en la base de datos.")

