matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = []
stc = []
linha = 1
for c in range(3):
    for coluna in range(3):
        d = int(input(f"Digite o valor para a linha {linha} coluna {coluna+1}: "))
        matriz[linha-1][coluna] = d
        if d % 2 == 0:
            soma.append(d)
        if coluna == 2:
                linha +=1
        if coluna == 2:
             stc.append(d)             
print("-="*50)
for linhaa in matriz:
    print(linhaa) 
print("-="*50)  
if soma:
    print(f"A soma de todos os elementos pares foi {sum(soma)}")
else:
     print("Nao teve elementos pares para fazer a soma")
print(f"A soma dos elementos da terceira coluna foi {sum(stc)}")
print(f"O maior valor da segunda linha foi {max(matriz[1])}")