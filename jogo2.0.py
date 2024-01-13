from random import choice
lista = ["pedra", "papel", "tesoura"]
q = str(input("Deseja jogar? ")).lower().strip()
while q == "s" or q == "sim":
    r = str(input('Digite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()
    a = choice(lista)
    if (r == "pedra" and a == "tesoura") or (r == "papel" and a == "pedra") or (r == "tesoura" and a == "papel"):
        print("\033[1;34mA máquina jogou {} e você venceu!!!\033[m".format(a))
    else:
        print("\033[1;31mA máquina jogou {} e você não venceu.\033[m".format(a))
    q = str(input("Quer jogar novamente? ")).lower().strip()
print("Obrigado por jogar!!!!")