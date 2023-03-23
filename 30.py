salario = float(input('Digite o seu salario: '))
imovel = float(input('Digite o valor do imovel que deseja comprar: '))
parcelas = int(input('digite em quantos anos voce quer pagar o imove: '))

p = imovel/(parcelas*12)

s = (salario*0.3)

if p > s:
    print('\033[1;31m O valor da parcela {:.2f} excede 30% do salario {:.2f} \033[m '.format(p,s))
else:
    print('\033[1;34m O emprestimo foi a provado e as parcelas serao de {:.2f} e serao pagas em {:.2f} meses \033[m'.format(p,parcelas*12))
