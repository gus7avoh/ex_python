import moedas
import os 
n = float(input("Digite o preço: R$ "))
os.system("cls")
print(f"O dobro do valor {moedas.moeda(n)}: {moedas.moeda(moedas.dobro(n))}")
print(f"A metaded do valor {moedas.moeda(n)}: {moedas.moeda(moedas.metade(n))}")
print(f"O valor {moedas.moeda(n)} com acrescimo de 10%: {moedas.moeda(moedas.aumentar(n, 10))}")
print(f"O valor {moedas.moeda(n)} com menos 13%: {moedas.moeda(moedas.reduzir(n, 13))}\n")


