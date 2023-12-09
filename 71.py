valor =  int(input("Digite qual valor vai ser sacado: R$ "))
contador50 = 0
contador20 = 0
contador10 = 0
contador1 = 0
while True:
    if valor >= 50:
        valor -= 50 
        contador50 += 1
    elif valor >=20:
        valor -= 20
        contador20 += 1
    elif valor >= 10:
        valor -= 10
        contador10 += 1  
    elif valor >= 1:
        valor -= 1
        contador1 += 1
    if valor == 0:
        break
print("Voce recebera:\n ")
print (f"{contador50} notas de 50R$")
print (f"{contador20} notas de 20R$")
print (f"{contador10} notas de 10R$")
print (f"{contador1} notas de 1R$")

