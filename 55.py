lista = []
contador = 0

while contador < 5:
    peso = int(input(("Digite o peso da pessoa: ")))
    lista.append(peso)

    contador += 1

lista.sort()

print("o menor peso foi: {}".format(lista[0]))
print("o maior peso foi: {}".format(lista[4]))