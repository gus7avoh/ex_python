def moeda(resp):
    teste = float(resp)
    return f'R${teste:.2f}'.replace('.', ',')


def dobro(n):
    """
    Dobra o valor
    :var n: Parametro para o calculo 
    """
    resp = n * 2
    return resp

n = float(input("Digite o preço: R$ "))

print(f"O dobro do valor {moeda(n)}: {moeda(dobro(n))}")
