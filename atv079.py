numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros :
        numeros.append(numero)
        print('Número adicionado com sucesso!')
    else:
        print('Valor duplicado, não irei adicionar!')
    op = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Digite [S/N] '))
    if op == 'N':
        break
print('-='*20)
print(f'Os valores digitados foram {sorted(numeros)}')

