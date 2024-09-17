limite_inferior = int(input("Digite o limite inferior do intervalo: "))
limite_superior = int(input("Digite o limite superior do intervalo: "))

somatorio = 0

for num in range(limite_inferior + 1, limite_superior):
    if num % 2 == 0:
        print(num)
        somatorio += num 

print("Somatório dos números pares:", somatorio)