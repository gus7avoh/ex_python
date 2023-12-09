precos = []
pv = []
p_m1000 = []
nome = []
preco = []
contador = 0
while True:
    print("-"*10,"CADASTRO","-"*10,"\n")
    nome.append(str(input("Digite o nome do produto: ")).lower().strip())
    pr = (int(input("Digite o preço do produto: ")))
    preco.append(pr)
    if pr >= 1000:
        p_m1000.append(pr)
    contador += 1 
    print("-"*31)
    print("-"*10,"CONTINUAR","-"*10,"\n")
    continuar = str(input("deseja cadastrat mais um produto? ")).strip()
    print("-"*31)
    if continuar.lower() != "s":
        break
for i in range(contador):
    tupla = (preco[i],nome[i])
    pv.append(tupla)
pv_ordenada = tuple(sorted(pv))  
print ("\n","-"*31)
print (f"O total gasto na compra foi de {sum(preco)}R$")
if p_m1000:
    print (f"{len(p_m1000)} produto(s custao mais de 1000R$")
print(f"O nome do produto mais barato eh: {pv_ordenada[0][1]} que custa {pv_ordenada[0][0]}R$")