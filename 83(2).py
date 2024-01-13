while True:
    text = input("Digite o texto: ")

    # Contadores de chaves abertas e fechadas
    chave_A = 0
    chave_F = 0

    # Flag para verificar a ordem das chaves
    ordem_correta = True

    for caractere in text:
        if caractere == "{":
            chave_A += 1
        elif caractere == "}":
            chave_F += 1

            # Verifica se há uma chave fechada antes de uma chave aberta
            if chave_F > chave_A:
                ordem_correta = False

    # Verifica se o número de chaves abertas é igual ao número de chaves fechadas
    if chave_A == chave_F and ordem_correta:
        print("A preposição está correta!")
    else:
        print("Incorreta!")     
    add = input("Quer adicionar mais um texto (s/n)? ")
    if add.lower() != "s":
        break
