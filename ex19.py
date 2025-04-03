idade=int(input("insira sua idade"))
sexo=input("isnira o seu sexo: masculino ou feminino")
atleta=input("é atleta? insira sim ou não")
if idade<15:
    print("anuncio artigo infantil")
elif idade>=15 and idade<=21 and sexo=="feminino":
    print("anuncio de maquiagem e moda")
elif idade>=22 and idade<=32 and sexo=="feminino":
    print("anuncio de esporte e itens de casa")
elif idade>=15 and idade<=32 and sexo=="masculino" and atleta=="sim":
    print("anuncio de esporte")
elif idade>=15 and idade<=21 and sexo=="masculino" and atleta=="não":
    print("anuncio de videogame")
elif idade>=21 and idade<=32 and sexo=="masculino" and atleta=="não":
    print("anuncio de livro, jardinagem e eletrodomestico")
else:
    print("idade não compatível")



