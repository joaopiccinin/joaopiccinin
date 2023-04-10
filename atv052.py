n = int(input('Digite um número: '))
c = 0
tot = 0
tot2 = 0
while c < n:
    c += 1
    if n % c == 0:
        print('\033[32m',end='')
        tot += 1
    else:
        print('\033[31m',end='')

    print(c, end=' ')
print('')
if tot == 2:
    print(f'\n\033[mO número {n} foi dividido {tot} vezes, portanto é um número primo.')
else:
    print(f'\n\033[mO número {n} foi dividido {tot} vezes, portanto não é um número primo.')













