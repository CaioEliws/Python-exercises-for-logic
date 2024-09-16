GrossSalary = float(input("Digite o seu salario bruto: "))
pres = float(input("Digite o valor desejado da prestacao: "))

acc = (GrossSalary * 30) / 100

if pres <= acc:
    print(f"O emprestimo pode ser concedido")

else:
    print(f"O emprestimo nao pode ser concedido")