tabela = []

for c in range(3):
    tabela.append(int(input("Enter a value: ")))

def maior(*num):
    return max(num)

result = maior(*tabela)
print("The maximum value is:", result)

print("Original list:", tabela)
