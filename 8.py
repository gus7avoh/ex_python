dias= int(input('Quantidade de dias que o carro esta alugado: '))
km= float(input('digite  a quantidade de km que foram rodados no automovel: '))

valor= (dias*60)+(km*0.15)

print('pelos {} dias de aluguel e os {} km rodados o valokr final do carro sera de {:.2f}'.format(dias,km,valor))