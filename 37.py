h = float(input('type the height of the person: '))
w = int(input('type the weight of the person: '))

imc = w/(h**2)

if imc < 18.5:
    print('the is person is under of the weight with {} pts of imc'.format(imc))

elif imc<25 and imc>18.5:
    print('the person is in the ideal weight with {} pts of imc'.format(imc))

elif imc<30 and imc>25:
    print('the person has overweight with {} pts of imc'.format(imc))

elif imc>30:
    print('the person has obesity with {} pts of imc'.format(imc))
    