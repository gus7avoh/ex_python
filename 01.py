print('Calculadora')
print('Digite qual tipo de operação deseja realizar')

n1=int(input('Primeiro numero: '))
operacao=input('Digite qual tipo de operação deseja realizar (+,-,*,/) ? ').strip().lower()

n2=int(input("Digite o segundo numero: "))

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