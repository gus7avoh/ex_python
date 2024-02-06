tabela = []

for c in range(3):
    tabela.append(int(input("Enter a value: ")))

def maior(tabela):
    maior = tabela[0]  # Inicializa o maior valor como o primeiro da lista
    for n in tabela:
        if n > maior:
            maior = n 
    return maior  # Retorna o maior valor encontrado

result = maior(tabela)
print("The maximum value is:", result)
print("Original list:", tabela)
