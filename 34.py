n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))

m =(n1+n2+n3)/3

if m >= (7):
    print('\033[1;34m O aluno for aprovado com uma media de {:.2f} pts\033[m'.format(m))

elif m < (5):
    print('\033[1;31m O aluno foi reprovadocom uma media de {:.2f} pts\033[m'.format(m))

elif m < (6.5) and m > (5):
    print('\033[1;33m O aluno esta de recuperacao, devido a media de {:.2f} pts\033[m'.format(m))