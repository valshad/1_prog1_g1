for i in range(3):
    emplo
    name = input("Name: ")
    startYear = int(input("Start year at the company: "))
    daysWidoutWork = int(input("absences: "))
    Salary = 100_000
    if daysWidoutWork == 0 and 2023 - startYear > 5:
        Salary = Salary * 1.3
    print(name, "earns", Salary)