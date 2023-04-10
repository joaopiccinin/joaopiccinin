n = 0
m = 0
c = 0
soma = 0
op = ''
maior = 0
menor = 0
while op != 'N':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    if c > 1:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()

m = soma/c
print(f'A média entre os valores digitados é igual a {m}')
print(f'O maior número digitado foi o {maior}')
print(f'O menor número digitado foi o {menor}')