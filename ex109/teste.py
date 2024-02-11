from moedas import dobro,metade,aumentar,reduzir,moeda
import os 
n = float(input("Digite o preço: R$ "))
os.system("cls")
print(f"O dobro do valor {moeda(n)}: {dobro(n, True)}")
print(f"A metaded do valor {moeda(n)}: {metade(n, True)}")
print(f"O valor {moeda(n)} com acrescimo de 10%: {aumentar(n, 10, True)}")
print(f"O valor {moeda(n)} com menos 13%: {reduzir(n, 13, True)}\n")


