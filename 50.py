r = int(input("digite a razao da PA: "))
i = int(input("digite o inicio da PA: "))
f = int(input("digite o final da PA: "))

for c in range(i,f,r):

    if c < 11:
        print("os 10 primeiros termos dessa PA sao {}\n".format(c))
        print("A razao da da PA eh {}\n".format(r))
        print("O primeiro termo dessa PA eh {}\n".format(i))
else:
    print("tem n")


