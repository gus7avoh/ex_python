
j = input("deseja saber se algum numero eh primo? ")

while j == "sim":

    num = int(input("Digite um numero para descobrir se este eh primo: "))

    if num == 2 or num == 3 or num == 5 or num == 7:
        print("\033[1;34m esse numero eh primo !!!!!\033[m")
        j = input("deseja jogar dnv? ")

    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print("\033[1;31m esse numero nao eh primo \033[m ")
        j = input("deseja jogar dnv? ")

    else:
        print("\033[1;34m esse numero eh primo !!!!!\033[m")
        j = input("deseja jogar dnv? ")
else:
    print("ok")