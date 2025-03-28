compra=int(input("isnira o valor total de sua compra"))
if compra>100:
    print("recebe desconto de 10%")
    desconto=compra*0.9
    print(f"valor da compra: {desconto} ")
else:
    print("sem desconto")