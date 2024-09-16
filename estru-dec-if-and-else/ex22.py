A = 3.68
D = 5.95
G = 5.87

fuel = input("Digite o tipo de combustivel: (A | D | G) ")
l = float(input("Digite a quantidade deseja de litros: "))

if fuel == "A":
    acc = A * l
    print(f"O preço a ser pago ira ser de: {acc}")

elif fuel == "D":
    acc = D * l
    print(f"O preço a ser pago ira ser de: {acc}")

elif fuel == "G":
    acc = G * l
    print(f"O preço a ser pago ira ser de: {acc}")