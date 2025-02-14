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

while True:
    print("\n¿Qué desea hacer?")
    print("1. Buscar por nombre al alumno: ")
    print("2. Buscar por apellidos al alumno: ")
    print("3. Buscar por código al alumno: ")
    print("4. Eliminar alumno.")
    print("5. Modificar información del alumno.")
    print("6. Mostrar lista de alumnos.")
    
    
    opcion = int(input("Ingrese una opción (1-6): "))

  #hay que poner el codigo y la carrera del alumno donde dice codigo_alumno y carrera_alumno
    if opcion == 1:
        nombre = input("Ingrese el nombre o apellido del alumno ")
        if nombre in nombre_alumno: 
            print(f"El nombre del alumno es:{nombre}, su código es: {codigo_alumno} y su carrera es: {carrera_alumno}")
        else:
            print("Lo siento, no hay un alumno con ese nombre en la base de datos.")
