from random import randint
numeros = (randint(0,9), randint(0,9),randint(0,9),randint(0,9),randint(0,9), )
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior número sorteado foi o {max(numeros)}')
print(f'O menor número sorteado foi o {min(numeros)}')