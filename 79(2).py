tabela = []
while True:
    for c in range (4):
        tabela.append(int(input("digite um numero: ")))
    pergunta = str(input("quer adicionar mais algum valor (s/n): ")).lower().strip()
    if pergunta == ("n"):
        break
print(set(tabela))


#tabela_set = set(tabela)
#for numeros in tabela:
#   tabela_set.add(numeros)
#print (tabela_set)