acc = 0
acc2 = 0

for i in range(6):
    num = int(input("Digite os numeros: "))

    if num > 0:
        acc+=num

    elif num < 0:
        acc2+=num

print(f"A soma dos numeros positivos e: {acc}")
print(f"A soma dos numeros negativos e: {acc2}")