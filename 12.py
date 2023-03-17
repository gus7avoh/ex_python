import math
num= int(input('Digite o angulo: '))

sen= math.sin(math.radians(num))
coseno= math.cos(math.radians(num))
tangente= math.tan(math.radians(num))

print('seno de {} = {:.2f} \n cosseno de {} = {:.2f} \n tangente de {} = {:.2f}'.format(num,sen,num,coseno,num,tangente))