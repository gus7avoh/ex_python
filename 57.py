pergunta = str(input("Digite se que jogar (s/n): "))


while pergunta != "s" and pergunta != "n":
    print("\nvalor indesejado!! ")
    pergunta = str(input("\nDigite se que jogar (s/n): "))

if pergunta == "s":
    print("\ntudo certo ent vamos la")
else: 
    print("suave ent")