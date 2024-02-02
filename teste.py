def validar():
    novamente = str(input("Deseja jogar novamente? (S/N)")).upper()
    if novamente in 'SN':
        break
    else:
        print("Digite (S/N)")

while True:
    print("vamos fazer um teste\n\n")
    validar()
