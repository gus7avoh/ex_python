
while True:
    funçao = str(input('\033[1;34m Funçao (Fim): \033[m')).strip().lower()
    if funçao == 'fim':
        break
    help(f'\033[1;34m{funçao}\033[m')


