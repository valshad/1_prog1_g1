pasaje = 2000
nombre = input("nombre")
edad = int(input("edad:"))
if 5 <= edad <= 10 or edad > 65:
    pasajeDesc = pasaje - (pasaje * 0.4)
    print (nombre, "valor de su pasaje:", pasajeDesc)
else:
    print (nombre, "valor de su pasaje:", pasaje)