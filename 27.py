s= float(input('digite o salario do funcionario: '))

if s <= (1250):
    print('O salario do funcionario com o reajuste sera de: {:.2f}'.format((s*0.15)+s))
else:
     print('O salario do funcionario com o reajuste sera de: {:.2f}'.format((s*0.1)+s))