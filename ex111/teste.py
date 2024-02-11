from utilidadescev.moeda import resumo
from utilidadescev import dado
import os 

os.system('cls')
p= dado.leiaDinheiro("Digite o valor: ")

resumo(p, 35 , 22)