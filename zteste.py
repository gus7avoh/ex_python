tabela = []
for c in range(3):
    letra = str(input("Digite algumas letras: ")) 
    tabela.append(letra)

# Imprimir a tabela sem as aspas e vírgulas
print(' '.join(tabela))