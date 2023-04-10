from time import sleep
soma = 0
c = 0
while True:
    n = int(input('Digite um número (999 para encerrar): '))
    if n == 999:
        print('Encerrando...')
        sleep(1)
        break
    soma+=n
    c+=1
print(f'Você digitou {c} números, e a soma entre eles é igual a {soma}')