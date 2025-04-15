ano=int(input("insira o ano em que nasceu"))
ano_atual=int(input("insira o ano atual"))
idade=ano_atual-ano
if idade>=18:
    print("é maior de idade")
else:
    print("menor de idade")