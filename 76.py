
pp = "laranja",20,"tomate", 30,"alface",15,"abacaxi",30

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)
for pos in range(0, len(pp)):
    if pos%2 == 0:
        print(f"{pp[pos]:.<30}", end='')
    else:
        print(f"R${pp[pos]:>7.2f}")
print("-"*40)