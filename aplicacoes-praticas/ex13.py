num1 = float(input("Digite o num 1 para a soma: "))
num2 = float(input("Digite o num 2 para a soma: "))
calc = input("Digite a operacao desejada: ( + | - | / | * ): ")

if calc == "+":
    som = num1 + num2
    print(f"A soma dos numeros e: {som}")

elif calc == "-":
    sub = num1 - num2
    print(f"A subtracao dos numeros e: {sub}")

elif calc == "/":
    div = num1 / num2
    print(f"A divisao dos numeros e: {div}")

elif calc == "*":
    mult = num1 * num2
    print(f"A multiplicacao dos numeros e: {mult}")