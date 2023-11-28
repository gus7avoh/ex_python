a = int(input("digite a idade a primeira pessoa "))
b = int(input("digite a idade a segunda pessoa "))
c = int(input("digite a idade a tereceira pessoa "))
d = int(input("digite a idade a quarta pessoa "))
e = int(input("digite a idade a quinta pessoa "))
f = int(input("digite a idade a sexta pessoa "))
g = int(input("digite a idade a setima pessoa "))

listama = []
listame = []

if a >= 18:
    listama.append(a)
else:
    listame.append(a)


if b >= 18:
    listama.append(b)
else:
    listame.append(b)


if c >= 18:
    listama.append(c)
else:
    listame.append(c)


if d >= 18:
    listama.append(d)
else:
    listame.append(d)


if e >= 18:
    listama.append(e)
else:
    listame.append(e)


if f >= 18:
    listama.append(f)
else:
    listame.append(f)


if g >= 18:
    listama.append(g)
else:
    listame.append(g)

print ("O numero de alumos maiorers de idade eh {}".format(len(listama)))
print ("O numero de alumos menores de idade eh {}".format(len(listame)))