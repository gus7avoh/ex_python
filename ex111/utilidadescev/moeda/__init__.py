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


def resumo(n = 0, aume = 1,  redu = 1):

    print("=-"*20)
    print("Resumo".center(40))
    print("=-"*20)

    print(f"Preço analizado: ".ljust(25), f"{moeda(n)}")
    print(f"O dobro do valor: ".ljust(25), f"{dobro(n, True)}")
    print(f"Metade do valor: ".ljust(25), f"{metade(n, True)}")
    print(f"20% aumento: ".ljust(25), f"{aumentar(n, aume,  True)}")
    print(f"12% redução: ".ljust(25), f"{reduzir(n, redu, True)}")
    print()


