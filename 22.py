velociade= int(input('digite a velociade do veiculo: '))

if velociade >= (80):
    print('voce sera multado em R$ {}'.format((velociade-80)*7))
else:
    print('Voce esta dentro do limite de velociade permitido!')