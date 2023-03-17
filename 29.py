import random

cores = {'vermelho':'\033[1;31m',
         'azul': '\033[1;34m',
         'nulo' : '\033[m'
}

n = int(input('Digite um numero: '))
resultado=random.randint(1,5)


if n == resultado:
    print('{}Voce acertou o numero!!!{}'.format(cores['azul'],cores['nulo']))
else :
    print ('{}O resultado correto era {} {}'.format(cores['vermelho'],resultado,cores['nulo']))