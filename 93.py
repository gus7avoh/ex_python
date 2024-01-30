import os
os.system("cls")
jogador = {}
gols = []
jogador["nome"] = str(input("Nome: ")).strip().lower()
jogador["jogos"] = int(input("Numero de jogos: "))
for c in range(jogador["jogos"]):
    gols.append(int(input(f"Numero de gols na {c+1} partida: ")))
jogador["gols"] = gols
jogador["total"] = sum(gols)
print("=-"*50)
print(jogador)
print("=-"*50)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=-"*50)
print(f"o jogador {jogador['nome']} jogou {jogador['jogos']} partidas.")
for c in range(len(gols)):
    print(f" => Na partida {c+1} fez {gols[c]}".center(50))
print("=-"*50)
print(f"Foi um total de {jogador['total']} gols.")
print()

