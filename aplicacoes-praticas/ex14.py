price = float(input("Digite o preço: "))
desc = float(input("Digite a porcentagem do desconto: "))

offer = desc / 100
calc = price * offer
acc = price - calc

print(f"O valor final do produto e de: {acc}")