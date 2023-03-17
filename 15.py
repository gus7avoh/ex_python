frase = str(input('Digite a frase para receber as alteracoes: ')).strip()

print('sua frase em letras minusculas eh {}'.format(frase.lower()))
print('sua frase em letras maiusculas eh {}'.format(frase.upper()))
print('sua frase tem {} letras excluindo os espacos'.format(len(frase) - frase.count(' ')))

corte=frase.split()

print('a primeira palavra da frase eh "{}" e ela tem {} letras'.format(corte[0], len(corte[0])))

