name = input("nombre: ")
cuota = 7000
career = input("carrera: ")
city = input("ciudad de recidencia: ")
if career == "electromecanica" and city != "rio cuarto":
    cuotaDesc = cuota - (cuota * 0.15)
    print("Alumno",name,"De la ciudad", city,"de la carrera", career,"Su cuota es de", cuotaDesc)
else:
    print("Alumno",name,"De la ciudad", city,"de la carrera", career,"Su cuota es de", cuota) 