import datetime
ano = int(input('Digite o ano que deseja analizar e para analizar o ano atual coloque "0": '))

if ano == (0):
    ano = datetime.date.today().year

if ano % 4 == (0) and ano % 100 != (0) or ano % 400 == (0):
    print('o ano {} eh bissexto!!'.format())
else:
    print('o ano {} nao eh bissexto'.format(ano))