r1= int(input('Digite tamanho da primeira reta: '))
r2= int(input('Digite tamanho da primeira reta: '))
r3= int(input('Digite tamanho da primeira reta: '))

list=[r1,r2,r3]
list.sort()

v=list[1]-list[0]

if  list[2] > v and list[2] < list[1]+list[0]:
    

    if r1 == r2 == r3:
        print('\033[1;34m um treiangulo pode ser formado e ele sera equilatero!!\033[m')
    
    elif r1==r2 and r1 != r3 or r2==r3 and r2 != r1 or r3==r1 and r2 != r1:
        print('\033[1;34m um treiangulo pode ser formado e ele sera isoceles!!\033[m')
    
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('\033[1;34m um treiangulo pode ser formado e ele sera escaleno!!\033[m')

else:
    print('\033[1;31m um triangulo nao pode ser formado \033[m')