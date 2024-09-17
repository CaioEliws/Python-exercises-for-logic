accWeight90 = 0
accPeople = 0
sumAge = 0
accPeopleAge18And60 = 0
countAge10To30 = 0

while True:
    age = int(input("Digite a sua idade: "))
    if age < 0:
        break
    weight = float(input("Digite o seu peso: "))

    if weight > 90:
        accWeight90 += 1

    accPeople += 1
    sumAge += age

    if age >= 18 and weight < 60:
        accPeopleAge18And60 += 1

    if 10 <= age <= 30:
        countAge10To30 += 1

if accPeople > 0:
    average = sumAge / accPeople
    percent = (countAge10To30 / accPeople) * 100
else:
    average = 0
    percent = 0

print(f"A quantidade de pessoas com mais de 90 quilos é: {accWeight90}")
print(f"A média das idades das pessoas é de: {average:.2f}")
print(f"A quantidade de pessoas maiores de idade e abaixo de 60 quilos é de: {accPeopleAge18And60}")
print(f"A porcentagem de pessoas com idade entre 10 e 30 anos é de: {percent:.2f}%")
