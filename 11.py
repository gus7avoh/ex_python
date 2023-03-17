import math
co= int(input('digite o cateto oposto: '))
ca= int(input('digite o cateto adjasente: '))

hp= (math.hypot(ca,ca))

print('a hipotenusa do triangulo com lados {} co,{} ca sera {}'.format(co,ca,hp))