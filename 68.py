import random
contador = 0
while True:
    ale = random.randint(1,2)
    pi = str(input("Voce quer ser par ou impar? "))
    n1 = int(input("digite seu numero: "))
    if pi == "par" and ale+n1%2 == 0:
        print("Voce venceu !!")
        contador += 1   
    elif pi == "impar" and ale+n1%2 != 0:
        print("Voce venceu !!")
        contador += 1
    else:
        break
if contador > 0:
    print(f"Voce perdeu, porem voce venceu {contador} rodada(s)")
else:
    print("Voce perdeu.")