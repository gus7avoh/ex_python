jogar = str(input("Deseja jogar? "))
valores = []

while jogar == "s":
    for c in range(3):
        n = int(input("Digite os valores: "))
        valores.append(n)

    jogar = str(input("Deseja adicionar mais valores? "))

valores_org = sorted(valores)

if valores:
    media = sum(valores) / len(valores)
    print("A média de todos os valores adicionados é: {:.2f}".format(media))
    print("O maior valor adicionado é: {}".format(valores_org[-1]))
    print("O menor valor adicionado é: {}".format(valores_org[0]))
else:
    print("Nenhum valor foi adicionado.")