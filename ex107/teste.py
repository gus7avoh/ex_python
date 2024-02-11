import moedas

n = float(input("Digite o preço: R$ "))
print(f"O dobro do valor {n}: {moedas.dobro(n)}")
print(f"A metaded do valor {n}: {moedas.metade(n)}")
print(f"O valor {n} com acrescimo de 10%: {moedas.aumentar(n, 10)}")
print(f"O valor {n} com menos 13%: {moedas.reduzir(n, 13)}")

