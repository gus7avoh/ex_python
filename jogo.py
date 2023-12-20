from random import choice 

lista = ["pedra","papel","tesoura"]

q = str(input("deseja jogar? ")).lower().strip()

while True:
    
    r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()

    if r == "pedra":
        while True:
            a = choice(lista)
            print("\033[1;31m A maquina jogou {} e voce nao venceu \033[m".format(a) )
            q = str(input("quer jogar denovo? ")).lower().strip()
            r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()
            if a == "tesoura":
                print("\033[1;34m A maquina jogou {} e voce venceu!!!\033[m".format(a) )
                break

    elif r == "papel":
        while True:
            a = choice(lista)
            print("\033[1;31m A maquina jogou {} e voce nao venceu \033[m".format(a) )
            q = str(input("quer jogar denovo? ")).lower().strip()
            r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()
            if a == "pedra":
                print("\033[1;34m A maquina jogou {} e voce venceu!!!\033[m".format(a) )
                break
        
    elif r == "tesoura":
        while True:
            a = choice(lista)
            print("\033[1;31m A maquina jogou {} e voce nao venceu \033[m".format(a) )
            q = str(input("quer jogar denovo? ")).lower().strip()
            r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()
            if a == "papel":
                print("\033[1;34m A maquina jogou {} e voce venceu!!!\033[m".format(a) )
                break
                  
    if q != "s" and q != "sim":
        break

print("Obrigado por jogar!!!!")




















