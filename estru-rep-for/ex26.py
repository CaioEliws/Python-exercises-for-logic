acc = 0

for i in range(5):
    num = int(input("Digite um numero: "))

    if num > 30:
        acc = acc + 1
print(f"A quantidade de numeros que passaram de 30 foi: {acc}")