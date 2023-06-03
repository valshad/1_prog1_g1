numberStudents = int(input("Cuantos estudiantes se van a inscribir?: "))
for i in range(numberStudents):
    name = input("nombre: ")
    cuota = 14000
    career = input("carrera: ")
    city = input("ciudad de recidencia: ")
    if career == "electromecanica" and city != "rio cuarto":
        cuotaDesc = 14000 - (14000 * 0.15)
        print("Alumno",name,"De la ciudad", city,"de la carrera", career,"Su cuota es de", cuotaDesc)
    else:
        print("Alumno",name,"De la ciudad", city,"de la carrera", career,"Su cuota es de", cuota)  