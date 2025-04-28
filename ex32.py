#código em python para exibir as tabuadas de 7, 8 e 9
numero=int(input("insria o valor"))
def tabuada (numero):
    print(f"tabuada do {numero}:")
    for i in range (1,11):
        print(F"{numero} x {i} = {numero * i}")

# # exibindo as tabuadas
tabuada(numero)
