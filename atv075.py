n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))
n4 = int(input('Quarto valor:'))
tupla = (n1, n2, n3, n4)
c = 0
print('Os números pares são: ', end = '')
for p in tupla:
    if p%2 == 0:
        c = p
        print(f'{c}', end = ' ')

cont9 = tupla.count(9)
print(f' \nO número 9 apareceu {cont9} vezes')
if 3 in tupla:
    cont3 = tupla.index(3)
    print(f'O número três apareceu na posição {cont3}')
else:
    print('Não há o número 3 na tupla')
