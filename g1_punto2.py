#Pedir tres notas, calcular el promedio y mostrarlo.
print("Calculadora de promedios")
nota1 = float(input("Ingrese Primera Nota ="))
nota2 = float(input("Ingrese Segunda Nota ="))
nota3 = float(input("Ingrese Tercera Nota ="))
result1 = (nota1 + nota2 + nota3)/3
print("Su Promedio es =", round(result1, 2))