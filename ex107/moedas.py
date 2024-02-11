def metade(n):
    """
    divide o valor pela metade
    :var n: Parametro para o calculo 
    """
    resp = n/2
    return resp

def dobro(n):
    """
    Dobra o valor
    :var n: Parametro para o calculo 
    """
    resp = n * 2
    return resp

def aumentar(n, porc = 10):
    """
    aumenta uma % do valor
    :var n: Parametro para o calculo
    :var porc: Parametro para a porcentagem  
    """
    resp= n+(n*(porc/100))
    return resp

def reduzir(n, porc = 10):
    """
    reduz uma % do valor
    :var n: Parametro para o calculo
    :var porc: Parametro para a porcentagem 
    """
    resp = n - (n*(porc/100))
    return resp
