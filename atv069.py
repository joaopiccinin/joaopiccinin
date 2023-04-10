from time import sleep
c= 0
totmaior = 0
toth = 0
totmenor = 0
while True:
    c+=1
    idade = int(input(f'Idade da {c}ª pessoa: '))
    if idade > 18:
        totmaior+=1
    sexo =' '
    print('-=' * 15)
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Sexo da {c}ª pessoa, [M]asculino ou [F]eminino: ')).upper().strip()[0]
        print('-=' * 15)
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totmenor += 1

    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('-=' * 15)
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        print('-=' * 15)

    if op == 'N':
        print('Encerrando...')
        sleep(1)
        break

print('-='*10, 'FIM DO PROGRAMA', '-='*10)
print(f'Total de pessoas com mais de 18 anos: {totmaior}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totmenor} mulheres com menos de 20 anos.')