password = ""

while password != "python123":
    password = input("Digite a senha: ")
    
    if password == "python123":
        print("Acesso concedido")
    
    else:
        print("Acesso Negado")