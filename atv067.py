from time import sleep
print('='*35)
print('{:^35}'.format('TABUADA'))
print('='*35)
c = 0
n = int(input('Quer ver a tabuada de qual valor? '))
print('='*35)
while True:
    c += 1
    if c > 10:
        c=0
        print('=' * 35)
        n = int(input('Quer ver a tabuada de qual valor? '))
        print('=' * 35)
        if n < 0:
            print('Encerrando o programa...')
            sleep(1)
            break
        c+=1
    print(f'{n} x {c} = {n*c}')

