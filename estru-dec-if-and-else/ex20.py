prod = float(input("Digite o valor do produto: "))

if prod <= 1000:
    print("O desconto sera de 10%")
    desc = prod * 0.1
    acc = prod - desc
    print(f"O valor final sera de: {acc}")

elif prod > 1000 and prod <= 5000:
    print("O desconto sera de 20%")
    desc = prod * 0.2
    acc = prod - desc
    print(f"O valor final sera de: {acc}")

elif prod > 5000:
    print("O desconto sera de 30%")
    desc = prod * 0.3
    acc = prod - desc
    print(f"O valor final sera de: {acc}")