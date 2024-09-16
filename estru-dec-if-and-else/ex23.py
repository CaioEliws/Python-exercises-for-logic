vel = int(input("Digite a velocidade do veiculo: "))

if vel <= 60:
    print("Sem penalidade")

elif vel > 60 and vel <= 80:
    print("Multa leve")

elif vel > 80 and vel <= 100:
    print("Multa grave")

elif vel > 100 and vel <= 120:
    print("Multa gravissima")

elif vel > 120:
    print("Detencao do condutor")