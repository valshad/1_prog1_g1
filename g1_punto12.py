firsYear = int(input("Ingrese año de ingreso a la empresa: "))
noWorkDays = int(input("Ingrese los dias no trabajados: "))
salary = 47000
if firsYear < 2019 and noWorkDays == 0:
    salaryRise = salary + (salary * 0.30)
    print("Su salario es de:", salaryRise)
else:
    print("Su salario es de:", salary)
    