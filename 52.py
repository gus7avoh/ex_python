import string



pergunta = str(input("deseja descobrir se o texrto eh um polindromo ? "))

while pergunta == "sim":
    tex = str(input("Digite seu texto: "))
    sla = tex.translate({ord(c): None for c in string.whitespace})

    if list(reversed(sla)) == list(sla):
        print("esse texto eh um polindromo")
    else:
        print("o texto '{}' nao eh um pondromo ".format(tex))

    pergunta = input("deseja jogar novamente? ")
else:
    print("ok")