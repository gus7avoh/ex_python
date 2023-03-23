n = int(input("""
digite 1 para fazer a conversao de um numero para binario,
digite 2 para fazer a conversao de um numero para octal,
digite 3 para fazer a conversao de um numero para hexadecimal: """))


if n == (1):
    c = int(input('\ndigite o numero que deseja ser convertido: '))
    print('\no numero {} convertido para binario eh {}'.format(c,bin(c)))

elif n ==(2):
    c = int(input('\ndigite o numero que deseja ser convertido: '))
    print('\no numero {} convertido para octal eh {}'.format(c,oct(c)))

elif n == (3):
    c = int(input('\ndigite o numero que deseja ser convertido: '))
    print('\no numero {} convertido para hexadecimal eh {}'.format(c,hex(c)))