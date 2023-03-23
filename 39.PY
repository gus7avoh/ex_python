from random import choice 


lista = ["pedra","papel","tesoura"]
a = choice(lista)

r= str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()


if r == ("pedra") and a == ("papel"):
    print('\033[1;31m A maquina jogou {} e venceu \033[m'.format(a))

elif r == ("pedra") and a == ("pedra"):
    print('\033[1;33m A maquina jogou {} e voces empataram \033[m'.format(a))

elif r == ("pedra") and a == ("tesoura"):
    print('\033[1;34m A maquina jogou {} e voce venceu!!!\033[m'.format(a))


elif r == ("papel") and a == ("tesoura"):
    print('\033[1;31m A maquina jogou {} e venceu \033[m'.format(a))

elif r == ("papel") and a == ("papel"):
    print('\033[1;33m A maquina jogou {} e voces empataram \033[m'.format(a))

elif r == ("papel") and a == ("pedra"):
    print('\033[1;34m A maquina jogou {} e voce venceu!!!\033[m'.format(a))


elif r == ("pedra") and a == ("papel"):
    print('\033[1;31m A maquina jogou {} e venceu \033[m'.format(a))

elif r == ("pedra") and a == ("pedra"):
    print('\033[1;33m A maquina jogou {} e voces empataram \033[m'.format(a))

elif r == ("pedra") and a == ("tesoura"):
    print('\033[1;34m A maquina jogou {} e voce venceu!!!\033[m'.format(a))