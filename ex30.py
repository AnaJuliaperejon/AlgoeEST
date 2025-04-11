
# 30. Encontrando Palíndromos
# - Crie uma lista chamada palavras com 5 palavras fornecidas pelo usuário.
# - Use um laço for para verificar quais palavras são palíndromos (ou seja, que podem ser lidas da mesma forma de trás para frente, como "arara").
# - Exiba as palavras palíndromas no final.
palindromos=[]
palavras=[]
for i in range (1,6):
    palavra=input("insira a palavra")
    palavras.append(palavra)

palavrareversa=""
for  palavra in palavras:
    palavrareversa=palavra[::-1]
    if palavra==palavrareversa:
        palindromos.append(palavra)
        
print (palindromos)


