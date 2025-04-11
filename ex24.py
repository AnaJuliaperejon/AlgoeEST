numeros=[]

for i in range(1,6): 
    numero=int(input(f"insira {i}° número:\n"))
    numeros.append(numero)

maior= numeros[0]
menor= numeros[0]

for numero in numeros: 
    if numero>maior:
        maior=numero
    elif numero<menor:
        menor=numero
    

print(f"{maior} maior e {menor} é menor")
