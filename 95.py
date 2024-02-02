import os

jogadores = []

while True:
    os.system("cls")  
    gols = []
    jogador = {}
    print("-" * 50)
    jogador["nome"] = input("Nome: ")
    jogador["jogos"] = int(input("Número de jogos: "))

    for c in range(jogador["jogos"]):
        gols.append(int(input(f"Número de gols na {c+1}ª partida: ")))

    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    jogadores.append(jogador.copy())
    print("-" * 50)
    
    add = input("Deseja adicionar mais algum (S/N): ").lower()
    if add not in ['s', 'ss', "sim", "y"]:
        break

os.system("cls") 

print("-=" * 50)
print("Índice".ljust(10), "Nome".ljust(20), "Gols".ljust(30), "Total".ljust(10))
print("=" * 100)

for indice, j in enumerate(jogadores):
    print(f"{indice}".ljust(10), f"{j['nome']}".ljust(20), f"Gols: {j['gols']}".ljust(30), f"Total: {j['total']}".ljust(10))

print("-=" * 50)

while True:
    indice = input("Quer ver o levantamento de qual jogador (parar 999): ")

    if indice == '999':
        break

    try:
        indice = int(indice)
        jogador = jogadores[indice]

        print(f"\nLevantamento do jogador {jogador['nome']}:")
        for c in range(len(jogador['gols'])):
            print(f"Na {c+1}ª partida fez: {jogador['gols'][c]}")
        print(f"Total: {jogador['total']}")
    except (ValueError, IndexError):
        print("\nÍndice inválido. Tente novamente.")


