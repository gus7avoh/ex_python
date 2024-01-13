usuarios = []
temporario = []
total = 0
while True:
    temporario.append(str(input("Digite o nome da pessoa: ")))
    temporario.append(float(input("Digite o peso da pessoa: ")))
    usuarios.append(temporario[:])
    temporario.clear()
    total += 1
    mais = str(input("Deseja adicionar mais alguma pessoa? ")).strip().lower()
    if mais not in ["s", "sim", "ss"]:
        break
pesado = max(usuarios, key=lambda x: x[1])
leves  = min(usuarios, key=lambda x: x[1])
if len(usuarios) > 1:
    print("\nLista de usuários com maior peso:")
    for cadastro in usuarios:
        if cadastro[1] == pesado[1]:
            print(f"Nome: {cadastro[0]}, Peso: {cadastro[1]}")
    print("\nLista de usuarios mais leves")
    for c in usuarios:
        if c[1] == leves[1]:       
            print(f"Nome: {leves[0]}, peso: {leves[1]}")
else:
    print("sobre o usuario cadastrado")
    print(f"\nNome: {usuarios[0][0]}, Peso: {usuarios[0][1]} ")
print(f"\nO número de pessoas cadastradas foi {total}")
todos = str(input("Deseja ver todos os usuario cadastrados? "))
if todos in ["s", "ss", "sim"]:
    for b in usuarios:
        print(f"\nNome: {b[0]}, Peso: {b[1]} ")


