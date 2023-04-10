import random
from time import sleep
n1 = random.randint(0, 5)
print('-='*30)
print('Vou pensar em um número de 0 a 5, tente adivinhar! ')
print('-='*30)
n2 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n2 == n1:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no número {}. Boa sorte na próxima tentativa!'.format(n1, n2))