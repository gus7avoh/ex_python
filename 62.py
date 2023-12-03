
jogar = str(input("deseja jogar: "))

while jogar == "s":

    pa= int(input("digite o numero que deseja ver sua Pa: "))
    ra= int(input("digite a razao dessa Pa: "))
    termos = int(input("ate onde essa pa deve ir? "))
    primeiros = []

    if termos != 0:
        while len(primeiros) < termos:
            pa = pa+ra

            primeiros.append(pa)

        print("os 10 primeiros termos dessa PA sao: {}".format(primeiros))
        print("e a razao da PA eh {}".format(ra))
        jogar = str(input("deseja jogar novamente? "))
    else:
        jogar = "n"
else:
    print("\nblz")