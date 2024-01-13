num = [[], []]
for valores in range(0,7):
    numero = int(input(f"Digite o {valores+1}° numero: "))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
print(f"Pares: {sorted(num[0])}")
print(f"Impares: {sorted(num[1])}")