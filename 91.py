from random import randint
import os

def limparTerminal():
    os.system("cls")

biblioteca = {}

biblioteca["jogador 1"] = randint(1, 6)
biblioteca["jogador 2"] = randint(1, 6)
biblioteca["jogador 3"] = randint(1, 6)
biblioteca["jogador 4"] = randint(1, 6)

limparTerminal()

organizada = sorted(biblioteca.items(), key=lambda x: x[1], reverse=True)

for k, v in organizada:
    print(f"O {k} tirou: {v}")
