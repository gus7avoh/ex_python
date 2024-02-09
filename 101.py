import datetime 
idade = 0 

def voto():
    global idade
    nasc = int(input("Ano de nascimento: "))
    idade = datetime.datetime.now().year - nasc

    if idade < 18:
        return "Voto não obrigatório"
    elif idade >= 18 and idade < 65:
        return "Voto obrigatório"
    else:
        return "Voto opcional"
    
situacao = voto()  
print(f"Com {idade} anos: {situacao}")  
