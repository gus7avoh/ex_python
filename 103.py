def ficha(nome, gols=0):
    if not nome: 
        nome = '<desconhecido>' 
    print(f"O jogador {nome} fez {gols} gol(S)")

while True:
    n = input("Nome: ")
    g = input("Gols: ")

    
    if g.isdigit():
        g = int(g)  
    else:
        g = 0  

    ficha(nome=n, gols=g)

    novamente = input("Mais um (S/N)? ").strip().lower()[0]
    while novamente not in ['s', 'n']:
        print("\n(S/N)\n")
        novamente = input("\nMais um (S/N)? ").strip().lower()[0]
    if novamente == 'n':
        break
