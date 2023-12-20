bra = "Palmeiras","Grêmio","Atlético-MG","Flamengo","Botafogo","Bragantino","Fluminense","Athletico-PR","Internacional","Fortaleza","São Paulo","Cuiabá","Corinthians","Cruzeiro","Vasco","Bahia","Santos","Goiás","coritiba","America-mg"

print(f"Os primeiro 5 colocados sao: {bra[:5]}\n")
print(f"Os quatro ultimos colocados sao: {bra[-4:]}\n")
print(f"O campeoto organizado alfabeticamnte eh: {sorted(bra)}\n")
c = bra.index("Cruzeiro")
print(f"O maior time do praneta Cruzeiro se encontra na posisao {c+1}\n")