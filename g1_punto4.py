#Leer dos números y decir cuál es el mayor.
num1 = int(input("Ingrese un numero = "))
num2 = int(input("Ingrese un segundo numero = "))
print("Los numeros ingresados son:")
print("     - Primer numero = ", num1)
print("     - Segundo numero =", num2)
#Pausa para que el usuario confirme los datos ingresados
input("Presione cualquier tecla para continuar") 
if num1 > num2:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")
