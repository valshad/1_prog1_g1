#Leer dos números reales y mostrarlos en orden creciente.
num1 = int(input("Ingrese un numero real = "))
num2 = int(input("Ingrese un segundo numero real ="))
print("Los numeros ingresados son:")
print("     1_ ", num1)
print("     2_ ", num2)
input("presione cualquier tecla para ordenar de menor a mayor")
if num1 < num2:
    print(num1, ",", num2)
else:
    print(num2, ",", num1)
