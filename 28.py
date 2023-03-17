r1= int(input('Digite tamanho da primeira reta: '))
r2= int(input('Digite tamanho da primeira reta: '))
r3= int(input('Digite tamanho da primeira reta: '))

list=[r1,r2,r3]
list.sort()

v=list[1]-list[0]

if  list[2] > v and list[2] < list[1]+list[0]:
    print('\033[1;34m um treiangulo pode ser formado!!\033[m')
else:
    print('\033[1;31m um triangulo nao pode ser formado \033[m')


