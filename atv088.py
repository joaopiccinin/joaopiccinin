from random import sample
from time import sleep
print('-='*15)
print('     JOGO DA MEGA-SENA        ')
print('-='*15)
jogos = int(input('Quantos jogos deseja fazer? '))
fixa = []
for j in range(jogos):
    fixa.append(sample(range(0,60),6))
    sleep(1)
    print(f'Jogo {j+1}: {sorted(fixa[:])}')
    fixa.clear()
