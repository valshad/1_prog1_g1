#Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
num1 = float(input("Ingrese un numero = "))
num2 = float(input("Ingrese un segundo numero="))
print("Los numeros ingresados son:")
print("     1_ ", num1)
print("     2_ ", num2)
input("Continuar (presione cualquier tecla)")
print("¿Que operacion desea realizar?:")
print("     1)_ Sumar (Primer numero + segundo numero)")
print("     2)_ Restar (Primer numero - segundo numero)")
opcion1 = input("Coloque numero de operación (1 o 2):")
if opcion1 == "1":
    print("El resultado de la suma es:")
    print(num1, "+", num2, "=", num1 + num2)
else:
    print("El resultado de la resta es:")
    print(num1, "-", num2, "=", num1 - num2)
