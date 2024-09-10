price = float(input("Digite o valor da compra: "))

if price < 20:
    print("O lucro sera de 45%")
    profit = 0.45

elif price >= 20:
    print("O lucro sera de 30%")
    profit = 0.30

sell = price * (1 + profit)

print(f"O valor da venda do produto sera de: {sell}")