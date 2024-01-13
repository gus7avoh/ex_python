print("-"*50)
print("MEGA CENA".center(50))
print("-"*50)

from random import randint
from time import sleep
pergunta = int(input("Quantos jogos voce vai querer? "))
jogo = []
print("-="*25)
for d in range(pergunta):   
    while len(jogo) < 6: 
        n = randint(0,60)
        if n not in jogo:
            jogo.append(n)
    sleep(1)
    print(f"O {d+1}º Jogo: {sorted(jogo)}", end='\n\n')
    jogo.clear()








