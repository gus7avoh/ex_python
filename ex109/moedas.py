def metade(n, formatado = False):
    """
    divide o valor pela metade
    :var n: Parametro para o calculo 
    """
    resp = n/2
    return resp if formatado is False else moeda(resp)

def dobro(n, formatado = False):
    """
    Dobra o valor
    :var n: Parametro para o calculo 
    """
    resp = n * 2
    return resp if formatado is False else moeda(resp)

def aumentar(n, porc = 10, formatado = False):
    """
    aumenta uma % do valor
    :var n: Parametro para o calculo
    :var porc: Parametro para a porcentagem  
    """
    resp= n+(n*(porc/100))
    return resp if formatado is False else moeda(resp)

def reduzir(n, porc = 10, formatado = False):
    """
    reduz uma % do valor
    :var n: Parametro para o calculo
    :var porc: Parametro para a porcentagem 
    """
    resp = n - (n*(porc/100))
    return resp if formatado is False else moeda(resp)


def moeda(resp, sifra = "R$"):
    teste = float(resp)
    return f'{sifra}{teste:.2f}'.replace('.', ',')
