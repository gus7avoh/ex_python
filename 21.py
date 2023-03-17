import random
resposta = random.randint(0,5)

numero= int(input('digite o numero para o sorteio: '))

if resposta == numero:
    print('Parabens, voce acertou o resultado!!')
else:
    print('tente novamente')
    print('a resposta correta era {}'.format(resposta))