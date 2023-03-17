d= int(input('Digite a distancia a ser percorrida: '))

if d <= (200):
    print('o valor da viagem sera R$ {}'.format(d*0.50))
else:
    print('o valor da viagem sera R$ {}'.format(d*0.45))