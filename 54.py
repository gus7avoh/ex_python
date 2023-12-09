contador = 0
listama = []
listame = []
while contador < 7:
    idade = int(input("Digite a idade da pessoa: "))
    if idade > 21:
        listama.append(idade)
    else:
        listame.append(idade)
    contador += 1
print("o numero de pessoa maiores de idade eh: {}".format(len(listama)))
print("o numero de pessoa menores de idade eh {}".format(len(listame)))