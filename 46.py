r = int(input("digite a razao da PA"))
i = int(input("digite o inicio da PA"))
f = int(input("digite o final da PA"))

for c in range(i,f,r):
    if c <= 10:
        print(c)
        print("Esses sao todos os numeros pares em um intervalo de 1 ate 10".format(r))