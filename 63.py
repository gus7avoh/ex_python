antigo = 0
n = int(input("Digite o número para ver sua sequência: "))
fibo = [0]
aaa = 1

while fibo[-1] < n:
    aaa = aaa + antigo
    antigo = fibo[-1]
    fibo.append(aaa)

print(fibo)