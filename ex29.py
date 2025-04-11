# 29. Multiplicação de Elementos da Lista
# - Crie uma lista chamada valores com 4 números inteiros fornecidos pelo usuário.
# - Peça ao usuário um número adicional e multiplique cada elemento da lista pelo número fornecido, usando um laço for.
# - Exiba os novos valores da lista.

valores=[]
novosvalores=[]
for i in range(1,5):
    valor=int(input("insira o valor"))
    valores.append(valor)

adicional=int(input("insira o numero que vai multiplicar "))
for valor in valores:
    novosvalores.append(valor*adicional)
print(f"os valores são {novosvalores}")
    