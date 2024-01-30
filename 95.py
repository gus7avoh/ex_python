import os
jogadores = []
while True:
    os.system("cls")
    gols = []
    jogador = {}
    print("-"*50)
    jogador["nome"] = str(input("Nome: "))
    jogador["jogos"] = int(input("Numero de jogos: "))
    for c in range(jogador["jogos"]):
        gols.append(int(input(f"Numero de gols na {c+1} partida: ")))
        jogador["gols"] = gols[:]
        jogador["total"] = sum(gols)
    jogadores.append(jogador.copy())
    print("-"*50)
    add = str(input("Deseja adicionar mais algum (S/N): "))
    if add not in ['s', 'ss', "sim", "y"]:
        break
contador = 0
os.system("cls") 
print("-="*50)
print("Indice".ljust(10), "Nome".ljust(20), "gols".ljust(30), "total".ljust(10),)
print("="*100)
for j in jogadores:
    contador += 1
    print(f"{contador}".ljust(10),  f"{j['nome']}".ljust(20), f"gols: {j['gols']}".ljust(30), f"total: {j['total']}".ljust(10))
print("-="*50)

while True:
    indice = str(input("Quer ver o levantmentod de qual jogador: "))

    



