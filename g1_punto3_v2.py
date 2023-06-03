#Leer un número real y emitir una leyenda informando si es mayor o igual a cero o bien es negativo (son TRES opciones).
numreal1 = float(input("Ingrese un numero real = "))
if numreal1 > 0:
    print("El numero es mayor a 0")
elif numreal1 == 0:
    print("El numero es igual a 0")
else:
    print("El numero es negativo")