# 28. Filtrando Números Pares e Ímpares
# - Crie uma lista chamada numeros com 8 números inteiros escolhidos pelo usuário.
# - Use um laço for para dividir os números em duas listas: pares e impares.

numeros=[]
pares=[]
impares=[]
for i in range(1,9):
    numero=int(input(f"insira o {i}° valor"))
    numeros.append(numero)

for numero in numeros:
    m=numero % 2
    if m==0:
        par=numero
        pares.append(par)
    else:
        impar=numero
        impares.append(impar)

print(f"{pares} são os pares e {impares} são os impares")


