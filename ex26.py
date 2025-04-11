# 26. Cálculo de Média
# - Crie uma lista chamada notas com as notas de 5 alunos fornecidas pelo usuário.
# - Use um laço for para calcular a média das notas.
# - Exiba a média no final.

notas=[]
for i in range(1,6): 
    nota=int(input(f"insira a {i}° nota:\n"))
    notas.append(nota)
soma=0
for nota in notas:
    soma=soma+nota

media=soma/5
print(f" A média é: {media}")

