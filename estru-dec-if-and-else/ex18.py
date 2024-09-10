num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

som = num1 + num2

if som > 1000:
    print("A soma dos numeros e maior do que 1000")

elif som < 1000:
    print("A soma dos numeros e menor do que 1000")

elif som == 1000:
    print("A soma dos numeros e igual a 1000")

print(f"A soma dos numeros e: {som}")