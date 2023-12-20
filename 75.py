i = int(input("Digite um número: "))
d = int(input("Digite um número: "))
g = int(input("Digite um número: "))
j = int(input("Digite um número: "))

tupla = (i, d, g, j)

print("Tupla:", tupla)


print("Quantidade de vezes que o número 9 aparece:", tupla.count(9))

try:
    index_3 = tupla.index(3)
    print("Índice do primeiro número 3 na tupla:", index_3)
except ValueError:
    print("O número 3 não está presente na tupla.")

for numero in tupla:
    if numero % 2 == 0:
        print(f"O número {numero} é par")
else:
    print("Nao tem numeros pares na tupla. ")



