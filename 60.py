sla = input("deseja jogar? ")
while sla == "s":
    n = int(input("digite o numero que deseja ver o fatorial: "))
    for c in range (1,n):
        n= n*c
    print("o numero fatorial eh: {}".format(n))
    sla = input("deseja jogar dnv? ")
else:
    print("ok")