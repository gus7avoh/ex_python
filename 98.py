import time

def contador():
    for c in range(1, 11, 1):
        
        print(f"{c} ")
        time.sleep(1)
        
    print("\n" + "-=" * 10)

    for c in range(10, 0, -1):
        print(f"{c} ")
        time.sleep(1)

    print("\n" + "-=" * 10)
    print("programado".center(20))
    print("-=" * 10 + "\n")
    
    n1 = int(input("Inicio: "))
    n2 = int(input("Fim: "))
    n3 = int(input("Passo: "))
    print("-=" * 10)
    
    if n3 ==  0:
        n3 = 1
    if n1 > n2 and n3 > 0:
        n3 *= -1
    
    for c in range(n1, n2 + 1, n3):
        print(f"{c} ")
        time.sleep(1)

contador()
