tot = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        tot+=1
print(f'O usuário digitou um total de {tot} números.')
print(f'A soma dos números digitados pelo usuário é igual a {soma}.')

