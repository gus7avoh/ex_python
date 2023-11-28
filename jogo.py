from random import choice 

lista = ["pedra","papel","tesoura"]

q = str(input("deseja jogar? ")).lower().strip()


while q == "s" or q == "sim":

    a = choice(lista)
    r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()

    if r == "pedra":

        while a != "tesoura":
            print("\033[1;31m A maquina jogou {} e voce nao venceu \033[m".format(a) )
            q = str(input("quer jogar denovo? ")).lower().strip()
            r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()
        else:
            print("\033[1;34m A maquina jogou {} e voce venceu!!!\033[m".format(a) )


    elif r == "papel":
        while a != "pedra":
            print("\033[1;31m A maquina jogou {} e voce nao venceu \033[m".format(a) )
            q = str(input("quer jogar denovo? ")).lower().strip()
        else:
            print("\033[1;34m A maquina jogou {} e voce venceu!!!\033[m".format(a) )


    elif r == "tesoura":
        while a != "papel":
            print("\033[1;31m A maquina jogou {} e voce nao venceu \033[m".format(a) )
            q = str(input("quer jogar denovo? ")).lower().strip()
        else:
            print("\033[1;34m A maquina jogou {} e voce venceu!!!\033[m".format(a) )

else:
    print("Obrigado por jogar!!!!")




















