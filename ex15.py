produto=input("insira o nome de um produto")
quantidade=int(input("insira a quantidade de compras"))
preco_uni=int(input("insira o preço"))
total=quantidade*preco_uni
if total>100:
    desconto=total*0.95
    print(f"total: R${desconto}")
else:
    print(f"total: R${total}")


