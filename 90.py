import os
aluno = {}
aluno["nome"] = str(input("Nome: ")).strip().lower()
aluno["nota"] = float(input("nota: "))
print()
os.system('cls')
print("-="*10)
print (f"Nome: {aluno['nome']}")
print(f"Media: {aluno['nota']}")
if aluno['nota'] >= 7:
    print("Aprovado")
else:
    print("Reprovado")
print("-="*10)
