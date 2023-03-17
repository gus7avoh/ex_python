n = str(input('Digite o nome da pessoa: ')).strip().lower()
s = n.split()

print('O primeiro nome da pessoa eh : {} '.format(s[0]))
print('O ultimo nome da pessoa eh: {}'.format(s[len(s)-1]))