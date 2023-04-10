from random import randint
print('-='*10)
print('JOGO DO PAR OU IMPAR')
print('-='*10)
c = 0
while True:
    jog = int(input('Digite um número: '))
    pc = randint(0, 10)
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    if op == 'P':
        if (jog + pc) % 2 == 0:
            print('-=' * 20)
            print(f'Você jogou {jog} e o computador {pc}. Total de {jog+pc} DEU PAR')
            print('-=' * 20)
            print('Você venceu!')
            print('Vamos jogar novamente...')
            c+=1
        else:
            print('-=' * 20)
            print(f'Você jogou {jog} e o computador {pc}. Total de {jog+pc} DEU ÍMPAR')
            print('-=' * 20)
            print('Você perdeu!')
            break
    if op == 'I':
        if (jog + pc) % 2 != 0:
            print('-=' * 20)
            print(f'Você jogou {jog} e o computador {pc}. Total de {jog+pc} DEU ÍMPAR')
            print('-=' * 20)
            print('Você venceu!')
            print('Vamos jogar novamente...')
            c+=1
        else:
            print('-=' * 20)
            print(f'Você jogou {jog} e o computador {pc}. Total de {jog+pc} DEU PAR')
            print('-=' * 20)
            print('Você perdeu!')
            break
print('-'*30)
print(f'GAME OVER! Você venceu {c} vezes.')
print('-'*30)