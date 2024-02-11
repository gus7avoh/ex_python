
def leiaDinheiro(texto):
    n =  str(input(texto)).strip()
    conversor = n 
    conversor = n.replace(",", ".")
    while True:
        try:
            float(conversor)
        except:
            print('\033[1;31mErro!!! Digite um valor valido\033[m\n') 
            n =  str(input(texto))
            conversor = n 
            conversor = n.replace(",", ".")           
        else:
            final = float(conversor)
            break

    return final


def leiaInt(n):
    from click import echo,style
    try:
        nInt = int(n)
        if (nInt % 1 == 0):
            return nInt
        else:
            return echo(style('Não inteiro', fg='red')) 
    except ValueError:
        return echo(style('Não inteiro', fg='red')) 
