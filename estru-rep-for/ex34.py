maior_altura = float('-inf')  # Menor possível inicialmente
menor_altura = float('inf')   # Maior possível inicialmente
soma_alturas_mulheres = 0
quantidade_mulheres = 0
soma_alturas_turma = 0

n = 10

for i in range(n):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    codigo_sexo = int(input(f"Digite o código do sexo da pessoa {i+1} (1 para masculino, 2 para feminino): "))
    
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    if codigo_sexo == 2:
        soma_alturas_mulheres += altura
        quantidade_mulheres += 1

    soma_alturas_turma += altura

media_altura_mulheres = soma_alturas_mulheres / quantidade_mulheres if quantidade_mulheres > 0 else 0

media_altura_turma = soma_alturas_turma / n

print(f"A maior altura da turma é: {maior_altura:.2f}")
print(f"A menor altura da turma é: {menor_altura:.2f}")
print(f"A média de altura das mulheres é: {media_altura_mulheres:.2f}")
print(f"A média de altura da turma é: {media_altura_turma:.2f}")
