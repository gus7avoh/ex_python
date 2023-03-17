import random
n1= str(input('digite o nuime do primeiro aluino: '))
n2= str(input('digite o nome do segundo aluno: '))
n3= str(input('digite o nome do terceiro aluno: '))
n4= str(input('digite o nome do quarto aluno: '))

lista= [n1,n2,n3,n4]

escolhido= random.choice(lista)

print('o escolhido para a tarefa sera {}'.format(escolhido))