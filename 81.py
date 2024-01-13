lista = []
while True:
    lista.append(int(input("digite um numero: ")))
    pergunta = str(input("Deseja adicionar outro numero (s/n)? ")).strip().lower()
    if pergunta != "s":
        break
print(f"\nO numero de elementos na lista eh {len(lista)}")
print(f"A lista ordenada do maior para o menor eh: {sorted(lista, reverse=True)}")
if 5 in lista:
    print("o numero 5 esta na lista! ")
else:
    print("O numero 5 nao esta na lista.")

#aa_ordenado = tuple(sorted(aa, reverse=True)) #está pegando a união ordenada e organizando ela do maior para o menor.