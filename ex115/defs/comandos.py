from time import sleep
import os

def limparTerminal():
    os.system("cls")

def titulo(txt):
    texto = str(txt).upper()
    print('\033[1;34m-\033[m'*50)
    print(f'\033[1;34m{texto}\033[m'.center(60))
    print('\033[1;34m-\033[m'*50)  
    
def cadastrar():
    titulo('cadastrar')
    print("Carregando.....")
    sleep(1)
    limparTerminal()
    while True:
        while True:
            
            nome = str(input("\033[1;32mDigite seu nome: \033[m")).strip().lower()
            if nome == "":
                print('\033[1;31mErro!!! Valor invalido\033[m')
            else:
                break
        while True:
            try:
                idade = int(input("\033[1;32mIdade: \033[m"))
            except:
                print('\033[1;31mErro!!! valor invalido\033[m')
            else:
                break
        with open('C:\\Users\\Gustavo\\Desktop\\python\\py\\ex115\\cadastro.txt', 'a') as arquivo:
            arquivo.write(f"Nome: {nome}".ljust(30) + f"Idade: {idade}\n")

        while True:    
            n = input("\033[1;32mQuer cadastrar mais pessoas? (s/n) \033[m").strip().lower()
            if n in ['s','n']:
                break
            else:
                print('\033[1;31mErro!!! valor invalido\033[m')
        if n not in ['s', 'sim']:
            break
    print('\033[1;34m-\033[m'*50)


def leitura():
    print("Caregando ...")
    sleep(1)
    limparTerminal()
    titulo('salvos')
    with open('C:\\Users\\Gustavo\\Desktop\\python\\py\\ex115\\cadastro.txt', 'r') as arquivo: 
        conteudo = arquivo.read()  
        print(conteudo)
    print('\033[1;34m-\033[m'*50)


def menu():

    while True:
        sleep(1)
        titulo('menu principal')
        print('\033[1;31m1\033[m','\033[1;33m - Ver pessoas cadastradas\033[m')
        print('\033[1;31m2\033[m','\033[1;33m - Cadastrar novas pessoas\033[m')
        print('\033[1;31m3\033[m','\033[1;33m - Sair do sistema\033[m')
        print('\033[1;34m-\033[m'*50)

        while True:
            pergunta = int(input("\033[1;32mDigite o indice refente ao que voce deseja fazer:\033[m"))
            if pergunta in [1, 2, 3]:
                break
            else:
                print('\033[1;31mErro!!! indice invalido\033[m')

        if pergunta ==  1:
            leitura()
        elif pergunta == 2:
            cadastrar()
        elif pergunta == 3:
            print("\033[1;32mObrigado por participar\033[m.".center(175))
            break
 

