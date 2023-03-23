s= str(input('digite "f" para sexo feminino e "m" para masculino: ')).strip().lower()

a= str(input('O jovem ja se alistou? (s ou n): ')).strip().lower()

if s == ('m'):
    i= int(input('digite a idade do jovem: '))

    if i == (18) and a == ('n'):
        print('Ja eh hora do jovem se alistar!! ')

    elif i < (18) and a == ('n'):
        print ('Ainda faltam {} anos para o jovem ter que se alistar'.format(18-i))
    
    elif i > 18 and a == ('n'):
        print('Ja se passaram {} anos do periodo do jovem se alistar'.format(i-18))

elif s == ('f'):
    print('Mulheres nao tem obrigatoriedade no servico militar!!')

elif s == ('m') and a == ('s'):
    print('Obrigado por cumprir o seu papel')
