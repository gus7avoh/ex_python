while True:
    n = int(input("digite o numero que deseja ver a tabuada: "))
    if n < 0:
        break
    for c in range(10):
        print(f"\n{n}X{c}={n*c}")
print("obringado por calcular!!!")