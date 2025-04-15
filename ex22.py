palavras=[]
soma=0
for i in range(1,7):
    palavra= input("insira uma palavra")
    palavras.append(palavra)

for palavra in palavras:
    print(len(palavra))

    if len(palavra)>5:
        soma=soma+1
    print(f"a quantidade de palvras com 5 caractres é: {soma}")
    print(palavras)
    