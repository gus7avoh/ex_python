n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
n3=int(input('Digite o tereceiro numero: '))


list = [n1, n2, n3]
list.sort()


print('O menor deles eh {} e o maior eh {}'.format(list[0],list[2]))

