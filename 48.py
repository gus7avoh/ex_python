
pergunta = "sim"
n = 0
p = str(input("Deseja ver a tabuada de algum numero? (sim ou nao): "))

if p == ("sim"):

    while pergunta == ("sim"):

        tabuada = int(input("A tabuada de qual numero voce deseja saber? "))
        n = tabuada

        for mult in range(1,10,1):
    
            tabuada = n * mult
            print("{}X{}= {}".format(n, mult, tabuada))



        pergunta = str(input("quer calcular denovo (sim, nao): "))


    else:
        print(" Obrigado por calcular")

else:
    print(" ok")