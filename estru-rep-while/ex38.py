sumSalary = 0
sumPeople = 0

minAge = float('inf')
maxAge = float('-inf')
minSalary = float('inf')

minSalaryAge = None # Poderia usar 0 porém terá problemas no futuro
minSalaryGender = None # Poderia usar '' porém terá problemas no futuro

accFemale = 0
accMale = 0

while True:
    age = int(input("Digite a sua idade: "))
    if age < 0:
        break
    sumPeople += 1
    gender = str(input("Digite o seu sexo: (M | F): "))
    salary = float(input("Digite o seu salario: "))

    # A média dos salários do grupo:
    sumSalary += salary
    accSalary = sumSalary / sumPeople

    # A maior e a menor idade do grupo:
    if age < minAge:
        minAge = age
    if age > maxAge:
        maxAge = age

    # A quantidade de mulheres na região:
    if gender == "F":
        accFemale += 1

    # A idade e o sexo da pessoa que possui o menor salário:
    if salary < minSalary:
        minSalary = salary
        minSalaryAge = age
        minSalaryGender = gender


print(f"A media de salarios do grupo e de: {accSalary:.2f}")

print(f"A menor idade do grupo e de: {minAge}")
print(f"A maior idade do grupo e de: {maxAge}")

print(f"A quantidade de mulheres na regiao e de: {accFemale}")

print(f"A pessoa com menor salario de: {minSalary} tem a idade: {minSalaryAge}, e o sexo: {minSalaryGender}")