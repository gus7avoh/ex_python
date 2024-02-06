import random

numeros = []

def sorteia():
    for c in range(5):
        numeros.append(random.randint(1, 6))

def somaPar(*nume):
    soma = []
    i = list(nume) #Quando eu peço para o sistema receber os valores da tabela, eles são inseridos em uma tupla, ent preciso converter.
    for num in i:
        if num % 2 == 0:
            soma.append(num)
    return sum(soma)

sorteia()

print("Generated numbers:", numeros)
print("Sum of even numbers:", somaPar(*numeros))


