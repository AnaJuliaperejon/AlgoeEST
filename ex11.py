senha_certa= input("cadastre sua senha")
(len(senha_certa))
if len(senha_certa)<8:
    print("senha deve ter no mínimo 8 caracteres")
else:
    print("senha efetuada com sucesso")
email_certo=input("cadastre seu email")
emailminusculo=email_certo.lower()
print(emailminusculo)
email=input("insira seu email")
senha=input("insira sua senha")
if email==emailminusculo and senha==senha_certa:
    print("login concluido com sucesso")
else:
    print("senha ou email incorretos")