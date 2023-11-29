contador = 0
nome = []
idade = []
masculino = []
feminino = []
uniao = []
sexos= []
aa = []
bb = []

while contador < 4:

    nome.append(str(input("\nDigite o nome da pessoa: ")))
    idade.append(int(input("Digite a idade da pessoa: ")))
    sexo = str(input("digite o sexo da pessoa (fem,mas): "))
    sexos.append(sexo)
    if sexo == "mas":
        masculino.append(sexo)
    else:
        feminino.append(sexo)

 #quando c for 1 ele vai me retornar 19 nayara e fem 
    contador += 1


for i in range(4):
   tupla=(idade[i],nome[i],sexos[i] )
   uniao.append(tupla)

#pega as listas idade, nome e sexos e une todas em uma grande lista uniao

for c in range(4):
   if uniao[c][2] == "mas":
       aa.append(uniao[c])

#ele vai rodar 4 vezes para que o [c] seja alterado de 0 até 3, com isso ele vai validar se a posição 0,1,2,3 na posição 2 vai ser "mas", caso seja ele vai adicionar essa união na lista "aa" que eh preenchida somente por homens.

for c in range(4):
   if uniao[c][2] == "fem":
       bb.append(uniao[c])

#vai fazer a mesma coisa que o último for, porem vai ver se são mulheres e adicioná-la s na lista BB, que só tem mulheres.


media = sum(idade)/4 #somatoria da lista idade e dividido por 4

uniao_ordenada = tuple(sorted(uniao)) #responsavel por organizar a lista uniao

aa_ordenado = tuple(sorted(aa, reverse=True)) #está pegando a união ordenada e organizando ela do maior para o menor.





print(uniao_ordenada)



print("\nA media de idade dos participantes eh: {}".format(media))
print("\nO nome do homen mais velho eh: {}".format(aa_ordenado[0][1]))

print("\nO numero de mulheres com menos de 20 anos eh: {}".format())


