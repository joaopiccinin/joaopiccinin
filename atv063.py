termos = int(input('Quantos termos voce quer mostrar? '))
n1 = 0
n2 = 1
c = 3
print(f'{n1} -> {n2}', end = ' -> ')
while c <= termos:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(f'{n3}', end = ' -> ')
    c+=1
print('FIM',end='')