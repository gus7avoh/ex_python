lista = []
for n in range(5):
    lista.append(int(input(f"digite o {n+1} valor: ")))
print(lista)
print(f"O maior valor na lista eh {max(lista)} que esta na posiçao: {lista.index(max(lista))}")
print(f"O menor valor na lista eh {min(lista)} que esta nas posiçao: {lista.index(min(lista))}")