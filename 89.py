alunos = []
pessoas = []
notas = []
while True:
    pessoas.append(str(input("Digite o nome da pessoa: ")))
    for c in range(2):
        notas.append(float(input(f"Digite {c+1}º a nota da pessoa: ")))
    pessoas.append(notas[:])
    notas.clear()
    alunos.append(pessoas[:])
    pessoas.clear()
    pergunta =  str(input("\033[1;34mQuer adicionar mais alguma pessoa? \033[m")).strip().lower()
    if pergunta not in ["s","ss","sim"]:
        break
print("-="*25)
print("MEDIA DOS ALUNOS".center(50))
print("-="*25)
for c in range(len(alunos)):
    print(f"{c} Nome: {alunos[c][0]}".ljust(30) + f"Media: {(sum(alunos[c][1]))/2}")
while True:
    p = str(input("Deseja ver a nota de algum aluno? ")).strip().lower()
    if p not in ["s","ss","sim"]:
        break
    print("-="*25)
    i = int(input("Digite o indice do aluno: "))
    print(f"Aluno(a) {alunos[i][0]} Nota 1: {alunos[i][1][0]} Nota 2: {alunos[i][1][1]} ")
    print("-="*25)








   