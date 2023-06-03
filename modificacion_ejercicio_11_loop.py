n = "si"
while n == "si":
    pasaje = 2000
    nombre = input("nombre")
    edad = int(input("edad:"))
    if 5 <= edad <= 10 or edad > 65:
        pasajeDesc = pasaje * 1.4
        print (nombre, "valor de su pasaje:", pasajeDesc)
    else:
        print (nombre, "valor de su pasaje:", pasaje)
    n = input("¿Desea cargar un pasajero? (si/no): ")
