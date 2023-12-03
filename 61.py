pa= int(input("digite o numero que deseja ver sua Pa: "))
ra= int(input("digite a razao dessa Pa: "))
primeiros = []
while len(primeiros) < 10:
    pa = pa+ra

    primeiros.append(pa)

print("os 10 primeiros termos dessa PA sao: {}".format(primeiros))
print("e a razao da PA eh {}".format(ra))