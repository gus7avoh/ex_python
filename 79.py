tabela = []
while True:
    for quantidade in range(4):
        n = int(input("digite um numero: "))
        if n not in tabela:
            tabela.append(n)
        else:
            print(f"o valor {n} adicionado ja esta na tabela...")
    per = str(input("deseja adicionar mais algum numero? (s/n)")).lower().strip()
    if per == ("n"):
        break
print(sorted(tabela))
