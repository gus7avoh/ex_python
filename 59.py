jogar= input(str("deseja jogar? "))
v1 = int(input("Digite o primero valor: "))
v2 = int(input("Digite o segundo valor: "))

while jogar == "s":

    print("-_-"*10)
    print(" 1 - Somar")
    print(" 2 - Multiplicar")
    print(" 3 - Maior")
    print(" 4 - Novos numeros")
    print(" 5 - Sair do programa")
    print("-_-"*10)
    v3 = int(input("oq deseja fazer: ")) 


    if v3 == 1:
        print("\n{}+{}={}".format(v1,v2,v1+v2))
        jogar = str(input("quer fazer outra coisa?"))

    elif v3 == 2:
        print("\n{}+{}={}".format(v1,v2,v1*v2))
        jogar = str(input("quer fazer outra coisa?"))  

    elif v3 == 3:
        if v1 > v2:
            print("o maior eh: ",v1)
            jogar = str(input("quer fazer outra coisa?"))
        else:
            print("o maior eh: ",v2)
            jogar = str(input("quer fazer outra coisa?"))

    elif v3 == 4:
        v1 = int(input("Digite um novo valor para o primeiro: "))
        v2 = int(input("Digite um novo valor para o segundo: "))
        jogar = str(input("quer fazer outra coisa?"))

    elif v3 == 5:
        print("vl por calcualar")
        jogar = "n"
else:
    print("vl por calcualar")




