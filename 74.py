import random

tupla = random.sample(range(1, 101), 5)
print(tupla)

ord = sorted(tupla)

print(f"O maior numero sorteado eh {ord[-1]} e o menor eh {ord[0]}")