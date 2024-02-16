def leiaNum():
    certo = 0
    correto = 0
    while certo !=  1:
        try:
            n = int(input("Numero inteiro: "))
        except KeyboardInterrupt:
            print(" \033[1;31mErro!!! O usuario nao digitou um valor\033[m")
            n = 0
            continue
        except ValueError:
            print(" \033[1;31mErro!!! O usuario nao digitou um valor valido\033[m")

        else:
            certo =  1
                       
    while correto != 1:
        try:
            f = float(input("Numero real: "))
        except KeyboardInterrupt:
            print(" \033[1;31mErro!!! O usuario nao digitou um valor\033[m")
            f = 0
        except ValueError:
            print(" \033[1;31mErro!!! O usuario nao digitou um valor valido\033[m")

        else:
            correto = 1

    print(f"O valor inteiro foi {n} e o real foi {f}")
            
            
             
            
leiaNum()