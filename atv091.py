from random import randint
from time import sleep
from operator import  itemgetter
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = []
print('Valores Sorteados:')
for k, v in dados.items():
    print(f'    {k} um tirou {v}')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')

for i, v in enumerate(ranking):
    print(f'    {i+1}o lugar: {v[0]} com {v[1]}')
    sleep(1)

