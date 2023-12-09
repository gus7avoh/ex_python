import random
resposta = random.randint(0,10)
chute = int(input("digite qual nume voce acha que sera o certo: "))
erros = 0
while chute != resposta:
    print("\nResposta errada !!!!")
    chute = int(input("tente novamente: "))

    erros +=1
print("\nParabens voce acertou!!!!!!!!!!!\ne para isso voce so precisou errar {} vezes".format(erros))