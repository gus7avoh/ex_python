simbolos = []

while True:
    text = str(input("Digite o texto: "))
    for caracteres in text:
        if caracteres == ("}") or caracteres == ("{") :
            simbolos.append(caracteres)
    chave_A = simbolos.count("{")
    chave_F = simbolos.count("}")

    tem_q_ser_abertas = len(simbolos)/2

    for chaves in range(0,tem_q_ser_abertas):
        if simbolos[chaves] == ("{") and chave_A == chave_F:
            print("a preposiçao esta correta!")
            print(f"Com {chave_A} chaves abertas e {chave_F} chaves fechadas")

        else:
            print("incorreta!")
            print(f"Com {chave_A} chaves abertas e {chave_F} chaves fechadas")

    add =  str(input("quer adicionar mais um texto (s/n)? "))

    if add != "s":
        break
    else:
        simbolos.clear()


#o numero de chaves dividido por dois, por ex com 4 chaves as duas primeiras tem q ser abertas