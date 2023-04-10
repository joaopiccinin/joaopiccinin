lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'S/N':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)




print(f'Lista de todos os valores: {lista}')
print(f'Lista dos valores pares: {listapar}')
print(f'Lista dos valores impares: {listaimpar}')
'''if n % 2 == 0:
    listapar.append(n)
else:
    listaimpar.append(n)'''
