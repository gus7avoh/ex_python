nay = ("nayara", "dos", "santos", "tavares")

for palavra in nay:
    for letra in "aeiou":
        if letra in palavra:
            print(f"{palavra} tem {letra}")