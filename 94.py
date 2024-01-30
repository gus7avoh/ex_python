import os
lista = []
idade = []
mulheres = []
maiores = []
contador = 0
while True:
    os.system("cls")
    dicionario = {}  
    dicionario["nome"] = str(input("Nome: ")).strip().lower()
    dicionario["sexo"] = str(input("Sexo: ")).strip().lower()
    dicionario["idade"] = float(input("Idade: "))
    idade.append(dicionario["idade"])
    contador += 1  
    lista.append(dicionario.copy())
    add = str(input("\nDeseja adicionar mais alguma pessoa? "))
    if add not in ['sim', 'ss', 's']:
        break
media = sum(idade) / contador
for pessoa in lista:
    if pessoa["sexo"] in ['fem', 'f', 'feminino']:
        mulheres.append(pessoa["nome"])
    if pessoa["idade"] >= media:
        maiores.append(pessoa["nome"])
os.system("cls")
print(f"{contador} pessoas foram adicionadas")
print(f"\nA média de idade do grupo é: {media:.2f}")
if mulheres:
    print(f"\nmulheres: {', '.join(mulheres)}\n")
if maiores:
    print("=-"*50)
    print("MAIOR OU IGUAL A MEDIA DE IDADE".center(100))
    for pessoas in lista:
        print(f"{pessoas['nome']} com {pessoa['idade']}")
    print("=-"*50)
  

