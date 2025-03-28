saldo=float(input("insira o saldo atual da conta"))
if saldo>0 or saldo<0:
    saldo=True
    print("conta ativa")
else:
    saldo=False
    print("conta inativa")