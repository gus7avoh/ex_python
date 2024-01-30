import datetime
funcionario = {}
funcionario["nome"] = str(input("Nome: ")).strip().lower()
funcionario["Nascimento"] = int(input("Ano de nascimento: "))
funcionario["ctps"] = int(input("Numero da carteira de trablho (0 Nao tem): "))
if funcionario["ctps"] != 0:
    funcionario["anoContrataçao"] = int(input("Ano de contrataçao: "))
    funcionario["salario"] = int(input("Salario: R$ "))
    funcionario["aposentadoria"] = (((datetime.datetime.now().year - funcionario["anoContrataçao"]) - 35) + (funcionario["Nascimento"] - datetime.datetime.now().year ))*-1

print("-="*50)
print(funcionario)

for k, v in funcionario.items():
    print(f"O {k} tem {v}")

