from random import randint
from time import sleep
pc = ''
print('-='*11)
print(' JOGO DA ADIVINHAÇÃO')
print('-='*11)
print('O computador vai pensar em um número entre 1 e 10, sua missão é adivinhá-lo!')
j = 0
tot = 1
while j != pc:
    pc = randint(1, 10)
    j = int(input('Número escolhido: '))
    print('Processando...')
    sleep(1)
    if j != pc:
        print(f'Você errou, o computador pensou no número {pc}, tente novamente!')
        tot+=1

print(f'Parábens, depois de {tot} tentativas, você acertou!')
