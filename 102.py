def fatorial(n, show=False):
    """
    Mostra o fatorial do numero solicitado

    :Param n: Numero que sera feito o fatorial
    :Param show: Define se vai ou nao ser mostrado o calculo do fatorial
    
    
    """
    fa = 1
    for c in range(n, 1, -1):
        fa *= c
    if show:
        print(n, end=" ")
        for c in range(n-1, 0, -1):
            print(f"X {c}", end =' ')
        print("= ", end=" ")
    return fa

help(fatorial)

numero = input("Número: ")
while not numero.isdigit():
    print("ERRO!\n")
    numero = input("Número: ")
ver = input("Deseja ver o cálculo (S/N)? ").strip().lower()
while ver not in ["s", "n"]:
    print("ERRO!\n")
    ver = input("Deseja ver o cálculo (S/N)? ").strip().lower()
if ver == 's':
    ver = True
else:
    ver = False
print(fatorial(int(numero), ver))

