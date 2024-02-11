
def leiaDinheiro(texto):
    n =  str(input(texto))
    conversor = n 
    conversor = n.replace(",", ".")
    while True:
        try:
            float(conversor)
        except:
            print('\033[1;31mErro!!! DIgite um valor valido\033[m\n') 
            n =  str(input(texto))
            conversor = n 
            conversor = n.replace(",", ".")           
        else:
            final = float(conversor)
            break

    return final





    #Antes do erro tenho que validar o pq do erro, caso o erro seja por causa da virgula
    #tenho que subistituir a virgula por um ponto e converter novamnete em um float



    #quanod o usuario digitar um valor com virgula no terminal o sitema tem que aceitar 
    #quando o usuario digitar um valor vazio o sistema tem que enviar uma mensagem de erro 
    #quando o ususario digitar um texto o sistema tem que reportar um erro 
