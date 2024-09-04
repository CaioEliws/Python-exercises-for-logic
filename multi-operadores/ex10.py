cap = float(input("Digite o capital inicial: "))
jur = float(input("Digite a taxa de juros em porcentagem: "))
temp = int(input("Digite o tempo em anos: "))

i = jur / 100

mont = cap + (cap * i * temp)

print(f"Apos aplicar seu juros simples o montante final ficou: {mont}")