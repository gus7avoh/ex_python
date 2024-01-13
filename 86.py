matriz = [[0,0,0],[0,0,0],[0,0,0]]
for elementos in matriz:
    print(elementos)
print("-="*30)
while True:
    linha = int(input("\nDigite qual linha deseja modificar: "))
    coluna = int(input("Digite qual coluna deseja modificar: "))
    valor = int(input("Qual valor quer colocar? "))
    matriz[linha-1][coluna-1]=valor
    mais = str(input("quer modificar mais algum valor? "))
    if mais not in ["s","ss","sim"]:
        break
print("-="*30)
print("A TABELA FORMATADA".center(60))
for elementos in matriz:
    print (elementos)
