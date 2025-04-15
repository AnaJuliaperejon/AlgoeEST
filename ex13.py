nome=input("insira seu nome")
idade=int(input("insira sua idade"))
turma=input("insira sua turma")
print(f"Aluno cadastrado com sucesso: {nome},{idade} anos,turma {turma}")
if idade>= 6:
    print("matricula validada")
else:
    print("matricula não validada")
