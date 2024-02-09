from click import echo,style
def leiaInt(n):
    try:
        nInt = int(n)
        if (nInt % 1 == 0):
            return nInt
        else:
            return echo(style('Não inteiro', fg='red')) 
    except ValueError:
        return echo(style('Não inteiro', fg='red')) 

b = input("Número: ")
resposta = leiaInt(b)
print(resposta)


