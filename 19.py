f = str(input('Digite a frase: ')).strip().lower()

print ('A frase tem  {} ledras "a"'.format(f.count('a')+1))
print('A primeira vez que a letra "a" aparece eh na posicao {}'.format(f.find('a')+1))
print('A ultima vez que o "a" aparece eh na posicao {}'.format(f.rfind('a')+1))