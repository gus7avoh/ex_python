from random import choice, randint
sup = True
while sup == True:
    new = True
    while new == True:
        print("-="*79)
        print("LISTA DE JOGOS".center(140))
        print("\n1 - Pedra papel e tesoura ")
        print("2 - jogo da forca ")
        print("3 - Par ou impar ")
        print("4 - Adivinhe um numero ")
        p = int(input("\n\033[1;34mDigite o numero referente ao jogo que deseja jogar: \033[m"))
        while p not in [1,2,3,4]:
            print("\n\033[1;31mOpçao invalida! \033[m")
            p = int(input("\n\033[1;34mDigite o numero referente ao jogo que deseja jogar: \033[m"))
        if p == 1:
            print("\033[1;35m-=\033[m"*79)
            print("PEDRA PAPEL OU TESOURA".center(140))
            print("\033[1;35m-=\033[m"*79)
            contador = 0
            vi = 0
            de = 0
            enpa = 0     
            lista = ["pedra", "papel", "tesoura"]           
            while True:    
                r = str(input('\nDigite a sua escolha, "pedra","papel" ou "tesoura": ')).strip().lower()
                contador += 1
                a = choice(lista)
                if (r in ['pedra','pe','ped'] and a == "tesoura") or (r in ['papel','pap','pa'] and a == "pedra") or (r in ['tesoura','tes','te','t'] and a == "papel"):
                    print("\033[1;34mA máquina jogou {} e você venceu!!!\033[m".format(a))
                    vi += 1
                    q = str(input("Quer jogar novamente? ")).lower().strip()
                elif (r in ['pedra','pe','ped'] and a == "pedra") or (r in ['papel','pap','pa'] and a == "papel") or (r in ['tesoura','tes','te','t'] and a == "tesoura"):
                    print("\033[1;33mA máquina jogou {} e você empatou.\033[m".format(a))
                    enpa += 1
                    q = str(input("Quer jogar novamente? ")).lower().strip()
                elif (r in ['pedra','pe','ped'] and a == "papel") or (r in ['papel','pap','pa'] and a == "tesoura") or (r in ['tesoura','tes','te','t'] and a == "pedra"):
                    print("\033[1;31mA máquina jogou {} e você perdeu.\033[m".format(a))
                    de += 1
                    q = str(input("Quer jogar novamente? ")).lower().strip()
                if q not in ["s","ss","sim"]:
                    break
            tabela = str(input("Quer ver a tabela de resultados? "))
            if tabela in ["s", "ss", "sim"]:
                print("="*50)
                print(f"Numero de rodadas:".ljust(25) +f"{contador}")
                print(f"Numero de vitorias:".ljust(25) +f"{vi}")
                print(f"Numero de Derrotas:".ljust(25) +f"{de}")
                print(f"Numero de impates:".ljust(25) +f"{enpa}" )
                print("="*50)
                print("\033[1;35m-=\033[m"*79)
                print("Obrigado por jogar pedra papel e tesoura!!!".center(140))
                print("\033[1;35m-=\033[m"*79)
                pergunta = str(input("Quer jogar outro jogo? "))
                if pergunta in ["s", "ss", "sim"]:
                    new = False
                elif pergunta not in ["s", "ss", "sim"]:
                    sup = False
                    new = False
            else:
                print("\033[1;35m-=\033[m"*79)
                print("Obrigado por jogar pedra papel e tesoura!!!".center(140))
                print("\033[1;35m-=\033[m"*79)
                pergunta = str(input("Quer jogar outro jogo? ")).strip().lower()
                if pergunta in ["s", "ss", "sim"]:
                    new = False
                elif pergunta not in ["s", "ss", "sim"]:
                    sup = False
                    new = False     
        elif p == 2:
                print()


        elif p == 3:
            print("\033[1;35m-=\033[m"*79)
            print("PAR OU IMPAR".center(140))
            print("\033[1;35m-=\033[m"*79)
            v = 0
            d = 0
            while True:
                rand = randint(1,2)
                pi = str(input("\nPar ou impar (p/i)? "))
                per = int(input("\nDigite um numero: "))             
                if ((rand + per) % 2 == 0 and pi in ["p","par"]) or ((rand + per) % 2 != 0 and pi in ["i","impar"]) :
                    print("\033[1;34mvoce venceu!!!\033[m")
                    v+=1
                    print (f"A maquina jogou: {rand}")
                else:
                    print("\033[1;31mvoce perdeu\033[m")
                    d+=1
                    print (f"A maquina jogou: {rand}")
                nov = str(input("\nQuer jogar novamente? "))
                if nov not in ["s", "ss", "sim"]:
                    break
            tabela = str(input("Quer ver a tabela? "))
            if tabela in ["s", "ss", "sim"]:
                print("="*20)
                print(f"Vitorias: ".ljust(10)+f"{v}")
                print(f"Derrotas: ".ljust(10)+f"{d}")
                print("="*20)
                print("\033[1;35m-=\033[m"*79)
                print("Obrigado por jogar Par ou Impar!!!!".center(140))
                print("\033[1;35m-=\033[m"*79)
                pergunta = str(input("Quer jogar outro jogo? "))
                if pergunta in ["s", "ss", "sim"]:
                    new = False
                elif pergunta not in ["s", "ss", "sim"]:
                    sup = False
                    new = False
            else:
                pergunta = str(input("Quer jogar outro jogo? "))
                if pergunta in ["s", "ss", "sim"]:
                    new = False
                elif pergunta not in ["s", "ss", "sim"]:
                    sup = False
                    new = False
        elif p == 4:
            print("\033[1;35m-=\033[m"*79)
            print("ADIVINHE UM NUMERO".center(140))
            print("\033[1;35m-=\033[m"*79)
            cont_v = 0
            cont_d = 0            
            while True:                
                a = int(input("Digite ate q numero vai ser sorteado: "))
                n = int(input("Digite o seu chute: "))
                ran = randint(1,a)
                if n == ran:
                    print("\033[1;34mvoce venceu!!!\033[m")
                    print(f"A maquina jogou {ran}") 
                    cont_v+=1 
                else:
                    print("\033[1;31mvoce perdeu\033[m")
                    print(f"A maquina jogou {ran}")
                    cont_d+=1
                q = str(input("Quer jogar de novo? "))
                if q not in ["s", "ss", "sim"]:
                    break
            tabela = str(input("Quer ver a tabela? "))
            if tabela in ["s", "ss", "sim"]:
                print("="*20)
                print(f"Vitorias: ".ljust(10)+f"{cont_v}")
                print(f"Derrotas: ".ljust(10)+f"{cont_d}")
                print("="*20)
                print("\033[1;35m-=\033[m"*79)
                print("Obrigado por jogar acerte o numero!!!!".center(140))
                print("\033[1;35m-=\033[m"*79)
                pergunta = str(input("Quer jogar outro jogo? "))
                if pergunta in ["s", "ss", "sim"]:
                    new = False
    
                elif pergunta not in ["s", "ss", "sim"]:
                    sup = False
                    new = False
    

            else:
                pergunta = str(input("Quer jogar outro jogo? "))
                if pergunta in ["s", "ss", "sim"]:
                    new = False
                elif pergunta not in ["s", "ss", "sim"]:
                    sup = False
                    new = False
                

                
        

