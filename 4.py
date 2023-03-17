largura =  float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area= largura*altura
tinta= area/2

print('A area da parede eh {} e  precisara de {} litros de tinta para ser pintada'.format(area,tinta))