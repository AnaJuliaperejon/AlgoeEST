nota1=int(input("insira 1° nota"))
nota2=int(input("insira 2° nota"))
nota3=int(input("insira 3° nota"))
media=(nota1+nota2+nota3)/3
print(f"{media}")
if media>=7:
    print("aprovado")
elif media==6 or media<7:
    print("recuperação")
else:
    print("reprovado")