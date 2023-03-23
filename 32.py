n1= int(input('Digite um numero: '))
n2= int(input('Digite um numero: '))

if n1 > n2:
    print('O primeiro numero "{}" eh maior "{}"'.format(n1,n2))

elif n2 >n1:
    print('O segundo numero "{}" eh maior que o primeiro "{}"'.format(n2,n1))

else:
    print('Os numeros sao iguais ')