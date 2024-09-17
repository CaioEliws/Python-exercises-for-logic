fat = 0
slim = 0
percent = 0
sum_age = 0

for i in range(7):
    age = int(input(f"Digite a idade da pessoa {i+1}: "))
    weight = float(input(f"Digite o peso da pessoa {i+1}: "))

    if weight >= 90:
        fat += 1

    sum_age += age

    if age >= 18 and weight < 60:
        slim += 1

    if age >= 10 and age <= 30:
        percent += 1

average = sum_age / 7
accPercent = float(percent / 7) * 100

print(f"A quantidade de pessoas com ou mais de 90 quilos e de: {fat}")
print(f"A média da idade das pessoas é de: {average:.2f}")
print(f"A quantidade de pessoas de maior idade e abaixo dos 60 quilos é de: {slim}")
print(f"A porcentagem de pessoas com a idade entre 10 e 30 anos é de: {accPercent:.2f}%")