a = int(input("digite a idade da primeira pessoa "))
b = int(input("digite a idade da segunda pessoa "))
c = int(input("digite a idade da tereceira pessoa "))
d = int(input("digite a idade da quarta pessoa "))
e = int(input("digite a idade da quinta pessoa "))
f = int(input("digite a idade da sexta pessoa "))
g = int(input("digite a idade da setima pessoa "))
listama = []
listame = []
if a >= 21:
    listama.append(a)
else:
    listame.append(a)
if b >= 21:
    listama.append(b)
else:
    listame.append(b)
if c >= 21:
    listama.append(c)
else:
    listame.append(c)
if d >= 21:
    listama.append(d)
else:
    listame.append(d)
if e >= 21:
    listama.append(e)
else:
    listame.append(e)
if f >= 21:
    listama.append(f)
else:
    listame.append(f)
if g >= 21:
    listama.append(g)
else:
    listame.append(g)
print ("O numero de alumos maiorers de idade eh {}".format(len(listama)))
print ("O numero de alumos menores de idade eh {}".format(len(listame)))