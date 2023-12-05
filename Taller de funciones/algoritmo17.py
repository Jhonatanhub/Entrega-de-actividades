def CalificacionMedia(cant_estudiantes):
    notas = 0
    nombres_estudiantes = []
    notas_estudiantes = []
        
    for i in range(1, cant_estudiantes + 1, 1):
        nombre_estudiante = input("Ingrese el nombre del estudiante \n")
        nombres_estudiantes.append(nombre_estudiante)
        nota_estudiante = float(input("Ingrese la nota del estudiante \n"))
        notas_estudiantes.append(nota_estudiante)
        notas = notas + nota_estudiante
        media = notas / cant_estudiantes
    print("Nombre de cada estudiantes: " , nombres_estudiantes)
    print("Nota de cada estudiante: " , notas_estudiantes)
    print("Media de las notas: " , media)
     
    
cant_estudiantes = int(input("Ingrese cuántos estudiantes son \n"))
CalificacionMedia(cant_estudiantes)