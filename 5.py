valor= float(input('Digite o valor do produto: '))
desconto= valor*0.05
montante= valor-desconto


print('o produto com valor original {} R$, vai ter um desconto de {} R$, portanto tera um valor final de {} R$'.format(valor,desconto,montante))