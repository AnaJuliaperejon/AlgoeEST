# 27. Lista de Nomes
# - Crie uma lista chamada nomes e insira os nomes de 5 amigos.
# - exibir os nomes em ordem alfabética.

nomes=[]

for i in range(1,6):
    nome=input("insira o {i}° nome")
    nomes.append(nome)

nomes.sort()
print(f"{nomes}")
