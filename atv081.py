numeros = []
c = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    c+=1
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Digite [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Foram digitados {c} números!')
print(sorted(numeros, reverse=True))
for pos, n in enumerate(numeros):
    if n == 5:
        print(f'O número 5 foi digitado na posição {pos}')
if 5 not in numeros:
    print('O número 5 não foi digitado!')