from time import sleep
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
p = 10
t = 0
while p != 0:
    t = t + p
    while c <= t:
        print(f'{n1} ->', end =' ')
        n1 += r
        c += 1
    print('PAUSA')
    p = int(input('Quantos termos você quer mostrar a mais? '))
print('Encerrando...')
sleep(1)
print(f'Progressão finalizada com {t} termos.')









