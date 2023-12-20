nay = ("nayara", "dos", "santos", "tavares")
vogais = set("aeiou")

for palavra in nay:
    letras_presentes = set(palavra) & vogais
    if letras_presentes:
        print(f"{palavra} tem {letras_presentes}")




#', '.join(letras_presentes)