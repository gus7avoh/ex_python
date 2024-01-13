from random import randint,choice
print("-="*79)
print("JOGO DA FORCA".center(140))
print("\033[1;34m0\033[m".center(150))
print(" "*68 + "\033[1;34m/|\033[m",end="")
print("\033[1;34m\ \033[m")
print(" "*68 + "\033[1;34m/.\033[m",end="")
print("\033[1;34m\ \033[m")
print("-="*79)
while True:
    modo = str(input("\nDigite qual modo de jogo voce quer jogar (Automatico/Manual): ")).strip().lower()
    if modo in ["a","aut","automatico"]:
        jogos = ["mario kart","mortal kombat","mario","need for speed","forza","sonic"]
        obj = ["caneta", "papel", "tesoura", "caderno", "computador"]
        filmes = ["tartarugas ninja", "kung fu panda", "barbie", "batman", "joves titans"]
        cep = ["belo horizonte", "minas gerais", "bahia", "salvador","fortaleza","rio de janeiro"]
        nomes = ["gustavo","joao","pedro","daiane","paulo","laura","helena"]
        escolhido = []
        escolhidoSemEsp = []
        print("="*157)
        print("TEMAS".center(140))
        print("1 - jogos")
        print("2 - objetos")
        print("3 - desenhos e filmes")
        print("4 - cidades/estados")
        print("5 - nomes")
        tema= int(input("\033[1;33mQual o indice do tema da partida? \033[m"))
        if tema == 1:
            sorteador = choice(jogos)
            for letras in sorteador:
                escolhido.append(letras)
                if letras != " ":
                    escolhidoSemEsp.append(letras)
                

        elif tema == 2:
            sorteador = choice(obj)
            for letras in sorteador:
                escolhido.append(letras)
                if letras != " ":
                    escolhidoSemEsp.append(letras)

        elif tema == 3:
            sorteador = choice(filmes)
            for letras in sorteador:
                escolhido.append(letras)
                if letras != " ":
                    escolhidoSemEsp.append(letras)

        elif tema == 4:
            sorteador = choice(cep)
            for letras in sorteador:
                escolhido.append(letras)
                if letras != " ":
                    escolhidoSemEsp.append(letras)

        elif tema == 5:
            sorteador = choice(nomes)
            for letras in sorteador:
                escolhido.append(letras)
                if letras != " ":
                    escolhidoSemEsp.append(letras)

        print("="*157)
        print("\033[1;34mBem vindo a partida e boa sorte!!\033[m")
        print(f"\033[1;34mA palavra sorteada tem _{len(escolhido)}_ letras \033[m")
        print("\033[1;34mVoce tem 5 tentativas\033[m")
        resposta =  []
        for c in range (len(escolhido)):
            resposta.append(" ")
        for i, letras in enumerate(escolhido):
            if letras == " ":
                resposta[i] = ("__")
        print(resposta)     
        erros = 0
        win = False
        totLetrasCertas = 0
        dica = 0


        while erros < 5:
            LetrasCertas = 0

            if totLetrasCertas == len(escolhidoSemEsp):
                print("\033[1;39m-=\033[m"*79)
                print("\033[1;39mVOCE venceu\033[m".center(150))
                print("\033[1;39m-=\033[m"*79)          
                break

            chute = str(input(f"\nDigite a sua tentativa (Se quiser uma dica digite DICA): ")).strip().lower()

            if chute == "dica":
                
                if len(escolhido) < 6 and dica == 0:
                    print("\033[1;33mVocê tem somente uma dica\033[m")
                    valida = []
                    for c in range(2):
                        sortear = randint(0, len(escolhido)-1)
                        while sortear in valida or escolhido[sortear] == " ":
                            sortear = randint(0, len(escolhido)-1)
                        valida.append(sortear)
                        resposta[sortear] = escolhido[sortear]
                    print("\nAqui está a sua dica")
                    print(resposta)

                elif len(escolhido) >= 6 and dica < 2:
                    if dica == 0:
                        print("\033[1;33mVocê tem duas dicas\033[m")
                    elif dica == 1:
                        print("\033[1;33mVocê só tem mais uma dica\033[m")
                    valida = []
                    for c in range(2):
                        sortear = randint(0, len(escolhido)-1)
                        while sortear in valida or escolhido[sortear] == " ":
                            sortear = randint(0, len(escolhido)-1)
                        valida.append(sortear)
                        resposta[sortear] = escolhido[sortear]
                    print("\nAqui está a sua dica")
                    print(resposta)

                else:
                    print("\033[1;31mSuas dicas terminaram\033[m")
                dica += 1

            else:
                for i, letra in enumerate(escolhido):
                    if letra == chute:
                        resposta[i] = chute
                        LetrasCertas += 1
                        totLetrasCertas += 1

                if LetrasCertas != 0:
                    print(f"\n\033[1;34mTemos {LetrasCertas} letras {chute} na palavra.\033[m")
                    print(resposta)

                elif LetrasCertas == 0:
                    erros += 1
                    if erros == 1:
                        print(" "*104+"\033[1;34m0\033[m")
                        print("\n")
                    elif erros == 2:
                        print(" "*104+"\033[1;34m0\033[m")
                        print(" "*103 + "\033[1;34m/|\033[m")
                    elif erros == 3:
                        print(" "*104+"\033[1;34m0\033[m")
                        print(" "*103 + "\033[1;34m/|\033[m",end="")
                        print("\033[1;34m\ \033[m")
                        print("\n")
                    elif erros == 4:
                        print(" "*104+"\033[1;34m0\033[m")
                        print(" "*103 + "\033[1;34m/|\033[m",end="")
                        print("\033[1;34m\ \033[m")
                        print(" "*103 + "\033[1;34m/.\033[m",end="")
                        print("\n")
                    elif erros == 5:
                        print(" "*104+"\033[1;34m0\033[m")
                        print(" "*103 + "\033[1;34m/|\033[m",end="")
                        print("\033[1;34m\ \033[m")
                        print(" "*103 + "\033[1;34m/.\033[m",end="")
                        print("\033[1;34m\ \033[m")
                        print("\033[1;35m-=\033[m"*79)
                        print("\033[1;35mVOCE PERDEU\033[m".center(150))
                        print("\033[1;35m-=\033[m"*79)
                    
                    


                
    elif modo in ["m","man","manual"]:
        print("")
            

            
