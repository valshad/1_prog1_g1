#Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.

segTotal = int(input("Ingrese la cantidad de segundos:"))
segXdia = 24 * 60 * 60
dia = segTotal // segXdia
sobr1 = segTotal - (dia * segXdia)
segXhor = 60 * 60
hor = sobr1 // segXhor
sobr2 = sobr1 - (hor * segXhor)
segXmin = 60
min = sobr2 // segXmin
seg = sobr2 - (min * segXmin)
print("El resultado es:")
print("     -Dias = ", dia)
print("     -Horas = ", hor)
print("     -Minutos = ", min)
print("     -segundos = ", seg)