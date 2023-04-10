from math import factorial
print('-='*15)
print('    DESCOBRINDO FATORIAIS')
print('-='*15)
n1 = int(input('Digite um número: '))
c = n1
print(f'{n1}!=', end=' ')
while c > 0:
    if c > 1:
        print( f'{c} *', end=' ' )
    else:
        print(f'{c} =', end=' ')
    c -= 1
r = factorial(n1)
print(r)


