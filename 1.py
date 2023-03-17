print('Calculadora')
print('digite qual tipo de operação deseja realizar')

n1=int(input('primeiro numero: '))
operacao=input('igite qual tipo de operação deseja realizar (+,-,*,/) ? ')

n2=int(input("digite o segundo numero: "))

resultado=0

if operacao ==('+'):
    resultado = float(n1+n2)
    print(n1,'+',n2,'=',resultado)

if operacao ==('-'):
    resultado=float(n1-n2)
    print(n1,'-',n2,'=',resultado)

if operacao ==('*'):
    resultado=float(n1*n2)
    print(n1,'*',n2,'=',resultado)

if operacao ==('/'):
    resultado=float(n1/n2)
    print('{} / {} = {}'.format(n1,n2,resultado))