i= int(input('Digite a idade do atleta: '))

if i <= 9:
    print('\033[1;34m Com {} anos,o atleta eh da categoria mirim \033[m'.format(i))

elif i > 9  and i <= 14 :
    print('\033[1;34m Com {} anos,o atleta eh da categoria infantil \033[m'.format(i))

elif i > 14 <= 19:
    print('\033[1;34m Com {} anos,o atleta eh da categoria junior \033[m'.format(i))

elif  i == 20:
    print('\033[1;34m Com {} anos,o atleta eh da categoria senior \033[m'.format(i))
    
elif  i > 20:
    print('\033[1;34m Com {} anos,o atleta eh da categoria master \033[m'.format(i))
