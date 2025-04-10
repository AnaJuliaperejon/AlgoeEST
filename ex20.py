idade=int(input("insira sua idade"))
membro=input("é membro? insira sim ou não")
junto=input("está acompanhado de um membro?")
if idade>18 and membro=="sim":
    print(" pode entrar")
elif idade <18:
    print("não pode entrar")
elif membro=="não" and junto=="sim":
    print("paga meia entrada")
else:
    print("paga entrada inteira")

