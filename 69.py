homens = []
mulheres = []
sexos = []
idade = []
uniao = []
nidade = []
m_maior = []
contador = 0

while True:
    print("-_-"*5,"SEXO","-_-"*5)
    sex = str(input("Digite o sexo da pessoa (h, m): "))
    while sex != "h" and sex != "m":
        sex = str(input("Digite o sexo da pessoa (h, m): "))
    sexos.append(sex)
    print("-_-"*5,"IDADE","-_-"*5)
    idade.append(int(input("Digite a idade da pessoa: ")))
    contador += 1
    print("-_-"*5,"MAIS CADASTROS?","-_-"*5)
    cadastrar = str(input("\033[1;31mDeseja cadastrar mais alguma pessoa? \033[m"))
    if cadastrar.lower() != "s":
        break

for i in range(contador):
    tupla = (idade[i], sexos[i])
    uniao.append(tupla)
    if idade[i] >= 18:
        nidade.append(idade[i])
    if sexos[i] == "h":
        homens.append(uniao[i])
    elif sexos[i] == "m":
        mulheres.append(idade[i])

for c in range(len(mulheres)):
    if mulheres[c] >= 18:
        m_maior.append(mulheres[c])

print(f"\n{len(nidade)} pessoas têm mais de 18 anos!")
print(f"{len(homens)} homens foram cadastrados!")
print(f"{len(m_maior)} mulheres maiores de idade!")