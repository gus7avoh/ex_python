while True:
    num = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quanze","dezeseis","dezessete","dezoito","dezenove","vinte")
    g = -1
    while g < 0 or g > 20:
       g = int(input("Digite um numero no intervalo de 0 ate 20: "))
    else:
        print(num[g])
    j = str(input("que ver outro ? "))
    if (j != "s") and (j != "sim") :
        break