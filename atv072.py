cont = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete','oito','nove',
           'dez', 'onze', 'doze','treze','quatorze','quinze',
           'dezesseis', 'dezessete', 'dezoito',
           'dezenove','vinte')
while True:
    while True:
            n = int(input('Digite um número entre 0 e 20: '))
            if n <= 20:
                break
            print('Insira um número válido! ', end = '')

    print(f'Você digitou o número {cont[n]}')
    op = ' '
    while True:
        op = str(input('Deseja continuar? [S/N] '))
        if op in 'SN':
            break
    if op == 'N':
        break
print('Encerrando Programa')


