lista = []
pares = []
impares = []
while True:
    lista.append(int(input("digite um numero: ")))
    pergunta = str(input("quer adicionar mais um numero? ")).strip().lower()
    if pergunta != "s":
        break
for numeros in lista:
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
print(f"\nTotal de numeros: {lista}")
print(f"\nNumeros pares: {pares}")
print(f"\nNumeros impares: {impares}")
