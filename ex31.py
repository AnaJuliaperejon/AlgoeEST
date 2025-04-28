
base=int(input("insira o valor"))
inicio=int(input("insira o valor de inicio"))
fim=int(input("insira o valor de fim"))
def tabuada (base, inicio, fim):
    print(f"tabuada do {base} de {inicio} de {fim}:")
    for i in range (inicio, fim +1):
        print(F"{base} x {i} = {base * i}")

tabuada(base, inicio, fim)
