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


for c in range(4):
   if uniao[c][2] == "mas":
       aa.append(uniao[c])

for c in range(4):
   if uniao[c][2] == "fem":
       bb.append(uniao[c])


media = sum(idade)/4
uniao_ordenada = tuple(sorted(uniao))
aa_ordenado = tuple(sorted(aa, reverse=True))





print(uniao_ordenada)



print("\nA media de idade dos participantes eh: {}".format(media))
print("\nO nome do homen mais velho eh: {}".format(aa_ordenado[0][1]))

print("\nO numero de mulheres com menos de 20 anos eh: {}".format())


