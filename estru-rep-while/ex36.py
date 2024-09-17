import random

number = 0

numberRandom = random.randint(1,100)

while number != numberRandom:
    number = int(input("Digite um numero ate acertar: "))

    if number == numberRandom:
        print(f"Parabens o numero aleatorio era: {numberRandom}")

    else:
        print("Voce errou o numero tente novamente: ")