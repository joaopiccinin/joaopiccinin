n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    c+=1
    print(f'{n1} ->', end =' ')
    n1 += r
print('FIM',end ='')