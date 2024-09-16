hour = 19.50

work = int(input("Digite o numero de horas trabalhado: "))

salary = hour * work

if salary >= 1500:
    acc = salary - (salary / 10)
    print(f"O seu salario liquido foi de: {acc}")

else:
    print(f"O seu salario liquido foi de: {salary}")