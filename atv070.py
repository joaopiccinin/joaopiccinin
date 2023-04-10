soma = 0
tot = 0
menor = 0
pb = ''
c = 0
print('-='*10)
print(' LOJA ATACADÃO TECH')
print('-='*10)

while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor: R$'))
    c += 1
    soma += valor

    if c == 1:
        menor = valor
        pb = produto
    if valor < menor:
        menor = valor
        pb = produto
    if valor > 1000:
        tot += 1

    op = ' '
    while op != 'S' and op != 'N':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*10, 'FIM DO PROGRAMA!', '-='*10)
print(f'O valor total da compra foi de \033[1;33mR${soma:.2f}\033[m')
print(f'{tot} produtos custaram mais de R$1000.00')
print(f'O produto mais barato foi \033[1;32m{pb}\033[m que custa R${menor:.2f}')