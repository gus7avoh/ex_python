tabela = []
while True:
    n = int(input("Digite um numero (parar com 999): "))
    if n == 999:
        break
    tabela.append(n)
print(f"A soma dos {len(tabela)} valores adicionados foi {sum(tabela)}")