def leiaInt(n):
    try:
        nInt = int(n)
        return nInt
    except ValueError:

        return 'Não inteiro'
        
b = input("Número: ")
resposta = leiaInt(b)
print(resposta)

