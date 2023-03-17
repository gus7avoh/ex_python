cidade= str(input('digite o nome da sua cidade: ')).strip().lower()
quebra= cidade.split()

print('o nome da sua ciadade comeca com "santo" = {}'.format(quebra[0] == 'santo'))