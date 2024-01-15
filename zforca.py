from random import randint,choice
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def restartGame():
    limpar_terminal()
    jogo = False
print("-="*79)
print("JOGO DA FORCA".center(140))
print("\033[1;34m0\033[m".center(150))
print(" "*68 + "\033[1;34m/|\033[m",end="")
print("\033[1;34m\ \033[m")
print(" "*68 + "\033[1;34m/.\033[m",end="")
print("\033[1;34m\ \033[m")
print("-="*79)
JogoGeral = True
while JogoGeral == True:
    jogo = True
    while jogo == True:
        modo = str(input("\nDigite qual modo de jogo voce quer jogar (Automatico/Manual): ")).strip().lower()
        if modo in ["a","aut","automatico"]:
            jogos = ["The Legend of Zelda: Breath of the Wild","Super Mario Odyssey","Red Dead Redemption 2","The Witcher 3: Wild Hunt","Fortnite","Minecraft","Grand Theft Auto V","Overwatch","Doom Eternal","Call of Duty: Warzone","Assassin's Creed Valhalla","Cyberpunk 2077","FIFA 22","League of Legends","Dota 2","Apex Legends","World of Warcraft","Mortal Kombat 11","Destiny 2","Valorant","Among Us","Super Smash Bros. Ultimate","Hollow Knight","Fallout 4","The Elder Scrolls V: Skyrim","Spider-Man: Miles Morales","God of War","Uncharted 4: A Thief's End","Dark Souls III","Fortnite","Battlefield V","Rainbow Six Siege","Rocket League","Hades","Stardew Valley","Cuphead","The Last of Us Part II","Resident Evil Village","Monster Hunter: World","Sekiro: Shadows Die Twice","Genshin Impact"]
            obj = ["Caneta","Notebook","Relógio","Óculos de sol","Garrafa de água","Chave de fenda","Câmera","Mochila","Guarda-chuva","Fone de ouvido","Bolsa","Mouse","Copo","Lanterna","Bloco de notas","Carregador","Faca","Cadeira","Escova de dentes","Livro","Pendrive","Cesto de lixo","Tênis","Chapéu","Caneca","Piano","Bicicleta","Escova de cabelo","Almofada","Caixa de ferramentas","Teclado","Porta-retratos","Abajur","Colar","Cesto de roupa suja","Mesa","Vaso de flores","Cobertor","Travesseiro","Espelho"]
            filmes = ["O Poderoso Chefão","Cidadão Kane","Casablanca","E o Vento Levou","Titanic","Matrix","Star Wars: Uma Nova Esperança","O Senhor dos Anéis: A Sociedade do Anel","O Rei Leão","Toy Story","Procurando Nemo","Harry Potter e a Pedra Filosofal","Pulp Fiction","Forrest Gump","Avatar","Jurassic Park","Vingadores: Ultimato","Pantera Negra","Coco","Frozen: Uma Aventura Congelante","Tom e Jerry","Pica-Pau","Os Simpsons","Bob Esponja","Scooby-Doo","Dragon Ball Z","Pokémon","Mickey Mouse","A Bela e a Fera","Aladdin","Mulan","Os Incríveis","Shrek","Madagascar","A Era do Gelo","Monstros S.A.","Up: Altas Aventuras","Ratatouille","Wall-E"]
            cep = [  "Rio de Janeiro","São Paulo","Brasília","Belo Horizonte","Salvador","Recife","Fortaleza","Curitiba","Manaus","Porto Alegre","Belém","Goiânia","Florianópolis","Natal","João Pessoa","Cuiabá","Campo Grande","Teresina","Palmas","Macapá","Porto Velho","São Luís","Aracaju","Maceió","Vitória","Rio Branco","Boa Vista","Santarém","Petrolina","Criciúma","Erechim","São Mateus","San Juan","Paris","Berlim","Tóquio","Pequim","Londres","Roma","Buenos Aires","Cidade do México"]
            nomes = ["Ana","João","Maria","Pedro","Mariana","Carlos","Fernanda","Rafael","Juliana","Lucas","Gabriela","Daniel","Isabela","Anderson","Amanda","Roberto","Cristina","Matheus","Larissa","Diego","Camila","Gustavo","Laura","Ricardo","Tatiane","Renato","Carolina","Felipe","Patrícia","Vinícius","Mônica","Eduardo","Letícia","Alexandre","Beatriz","Leandro","Thaís","Hugo","Aline","Luciana","Victor"]
            escolhido = []
            escolhidoSemEsp = []
            print("="*157)
            print("TEMAS".center(140))
            print("1 - jogos")
            print("2 - objetos")
            print("3 - desenhos e filmes")
            print("4 - cidades/estados")
            print("5 - nomes")
            tema= int(input("\n\033[1;33mQual o indice do tema da partida? \033[m"))
            limpar_terminal()
            if tema == 1:
                sorteador = choice(jogos)
                for letras in sorteador:
                    escolhido.append(letras.lower())
                    if letras != " ":
                        escolhidoSemEsp.append(letras.lower())
            elif tema == 2:
                sorteador = choice(obj)
                for letras in sorteador:
                    escolhido.append(letras.lower())
                    if letras != " ":
                        escolhidoSemEsp.append(letras.lower())
            elif tema == 3:
                sorteador = choice(filmes)
                for letras in sorteador:
                    escolhido.append(letras.lower())
                    if letras != " ":
                        escolhidoSemEsp.append(letras.lower())
            elif tema == 4:
                sorteador = choice(cep)
                for letras in sorteador:
                    escolhido.append(letras.lower())
                    if letras != " ":
                        escolhidoSemEsp.append(letras.lower())
            elif tema == 5:
                sorteador = choice(nomes)
                for letras in sorteador:
                    escolhido.append(letras.lower())
                    if letras != " ":
                        escolhidoSemEsp.append(letras.lower())
            print("="*157)
            print("\033[1;34mBem vindo a partida e boa sorte!!\033[m")
            print(f"\033[1;34mA palavra sorteada tem _{len(escolhido)}_ letras \033[m")
            print("\033[1;34mVoce tem 5 tentativas\033[m")
            resposta =  []
            for c in range (len(escolhido)):
                resposta.append("__")
            for i, letras in enumerate(escolhido):
                if letras == " ":
                    resposta[i] = (" ")
            print(' '.join(resposta))  
            erros = 0
            win = False
            totLetrasCertas = 0
            dica = 0
            while erros < 5:
                LetrasCertas = 0
                Nquebra = 0 
                dicasCorretas = 0       
                if totLetrasCertas == len(escolhidoSemEsp):
                    print("\033[1;39m-=\033[m"*79)
                    print("\033[1;39mVOCE venceu\033[m".center(160))
                    print("\033[1;39m-=\033[m"*79)       
                    break
                chute = str(input(f"\nDigite a sua tentativa (Se quiser uma dica digite DICA): ")).strip().lower()#
                if chute == "dica":                
                    if len(escolhido) < 6 and dica == 0:
                        print("\033[1;33mVocê tem somente uma dica\033[m")
                        valida = []
                        while dicasCorretas != 2:
                            sortear = randint(0, len(escolhido)-1)
                            while sortear in valida or escolhido[sortear] == "__" or resposta[sortear] not in ["__"]:  
                                sortear = randint(0, len(escolhido)-1)
                            valida.append(sortear)
                            resposta[sortear] = escolhido[sortear]
                            totLetrasCertas += 1
                            dicasCorretas+=1
                        print("\nAqui está a sua dica")
                        print(' '.join(resposta))
                    elif len(escolhido) >= 6 and dica < 2: 
                        if dica == 0:
                            print("\033[1;33mVocê tem duas dicas\033[m")
                        elif dica == 1:
                            print("\033[1;33mVocê só tem mais uma dica\033[m")
                        valida = []
                        while dicasCorretas != 2:
                            sortear = randint(0, len(escolhido)-1)
                            while sortear in valida or escolhido[sortear] == "__" or resposta[sortear] not in ["__"]: 
                                sortear = randint(0, len(escolhido)-1)
                            valida.append(sortear)
                            resposta[sortear] = escolhido[sortear]
                            totLetrasCertas += 1
                            dicasCorretas+=1
                        print("\nAqui está a sua dica")
                        print(' '.join(resposta))
                    else:
                        print("\033[1;31mSuas dicas terminaram\033[m")
                    dica += 1
                else:
                    for i, letra in enumerate(escolhido):
                        if letra == chute:
                            if resposta[i] != chute:
                                resposta[i] = chute
                                LetrasCertas += 1
                                totLetrasCertas += 1
                            else:
                                print("\033[1;31mEssa letra ja foi adicionada\033[m")
                                Nquebra += 1                           
                    if LetrasCertas != 0:
                        print(f"\n\033[1;34mTemos {LetrasCertas} letras {chute} na palavra.\033[m")
                        print("\n")
                        print(' '.join(resposta))
                        print("\n\n")
                    elif LetrasCertas == 0 and Nquebra == 0:
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
                            print("\n")  
                            print(f"\033[1;35mA resposta correta era {' '.join(escolhido)}\033[m".center(150))
                            print("\n")
                            print("\033[1;35m-=\033[m"*79)
                            print("\033[1;35mVOCE PERDEU\033[m".center(150))
                            print("\033[1;35m-=\033[m"*79)
            JogarNovamente = str(input("\nQuer jogar novamente? ")).strip().lower()
            if JogarNovamente in ["sim","ss","s"]:
                restartGame()
            else:
                limpar_terminal()
                print("\n")
                print("\033[1;34mObrigado Por Jogar\033[m".center(150))
                print("\n")
                jogo = False
                JogoGeral = False

        elif modo in ["m","man","manual"]:
            escolhidoSemEsp = []
            escolhido = []
            limpar_terminal()
            palavra = str(input("\033[1;34m\nDigite a palavra para que a outra pessoa tente acertar: \033[m"))
            limpar_terminal()
            for letras in palavra:
                escolhido.append(letras)
                if letras != " ":
                    escolhidoSemEsp.append(letras)
            print("\n")
            print("="*157)
            print("\033[1;34mBem vindo a partida e boa sorte!!\033[m")
            print(f"\033[1;34mA palavra sorteada tem _{len(escolhido)}_ letras \033[m")
            print("\033[1;34mVoce tem 5 tentativas\033[m")
            resposta =  []
            for c in range (len(escolhido)):
                resposta.append("__")
            for i, letras in enumerate(escolhido):
                if letras == " ":
                    resposta[i] = (" ")
            print(' '.join(resposta))     
            erros = 0
            win = False
            totLetrasCertas = 0
            dica = 0
            while erros < 5:
                LetrasCertas = 0
                Nquebra = 0 
                dicasCorretas = 0       
                if totLetrasCertas == len(escolhidoSemEsp):
                    print("\033[1;39m-=\033[m"*79)
                    print("\033[1;39mVOCE venceu\033[m".center(160))
                    print("\033[1;39m-=\033[m"*79)          
                    break
                chute = str(input(f"\nDigite a sua tentativa (Se quiser uma dica digite DICA): ")).strip().lower()
                if chute == "dica":                
                    if len(escolhido) < 6 and dica == 0:
                        print("\033[1;33mVocê tem somente uma dica\033[m")
                        valida = []
                        while dicasCorretas != 2:
                            sortear = randint(0, len(escolhido)-1)
                            while sortear in valida or escolhido[sortear] == "__" or resposta[sortear] not in ["__"]: 
                                sortear = randint(0, len(escolhido)-1)
                            valida.append(sortear)
                            resposta[sortear] = escolhido[sortear]
                            totLetrasCertas += 1
                            dicasCorretas+=1
                        print("\nAqui está a sua dica")
                        print(' '.join(resposta))
                    elif len(escolhido) >= 6 and dica < 2:
                        if dica == 0:
                            print("\033[1;33mVocê tem duas dicas\033[m")
                        elif dica == 1:
                            print("\033[1;33mVocê só tem mais uma dica\033[m")
                        valida = []
                        while dicasCorretas != 2:
                            sortear = randint(0, len(escolhido)-1)
                            while sortear in valida or escolhido[sortear] == "__" or resposta[sortear] not in ["__"]:
                                sortear = randint(0, len(escolhido)-1)
                            valida.append(sortear)
                            resposta[sortear] = escolhido[sortear]
                            totLetrasCertas += 1
                            dicasCorretas+=1
                        print("\nAqui está a sua dica")
                        print(' '.join(resposta))
                    else:
                        print("\033[1;31mSuas dicas terminaram\033[m")
                    dica += 1
                else:
                    for i, letra in enumerate(escolhido):
                        if letra == chute:
                            if resposta[i] != chute:
                                resposta[i] = chute
                                LetrasCertas += 1
                                totLetrasCertas += 1
                            else:
                                print("\033[1;31mEssa letra ja foi adicionada\033[m")
                                Nquebra += 1                           
                    if LetrasCertas != 0:
                        print(f"\n\033[1;34mTemos {LetrasCertas} letras {chute} na palavra.\033[m")
                        print("\n")
                        print(' '.join(resposta))
                        print(f"\n\n")
                    elif LetrasCertas == 0 and Nquebra == 0:
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
                            print("\n")
                            print(f"\033[1;35mA resposta correta era {' '.join(escolhido)}\033[m".center(150))
                            print("\n")
                            print("\033[1;35m-=\033[m"*79)
                            print("\033[1;35mVOCE PERDEU\033[m".center(150))
                            print("\033[1;35m-=\033[m"*79)
            JogarNovamente = str(input("\nQuer jogar novamente? ")).strip().lower()
            if JogarNovamente in ["sim","ss","s"]:
                restartGame()
            else:
                limpar_terminal()
                print("\n")
                print("\033[1;34mObrigado Por Jogar\033[m".center(150))
                print("\n")
                jogo = False
                JogoGeral = False  