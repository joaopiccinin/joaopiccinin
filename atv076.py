titulo = 'LISTAGEM DE PREÇOS'
print('-'*50)
print(titulo.center(50))
print('-'*50)
c=0
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15)
for p in produtos:
    if c == 1 or c == 3 or c == 5:
        print('R$', end=' ')
    if c == 0 or c == 2 or c == 4:
        print(f'{p:.<30} ', end=' ')
    else:
        print(f'{p:.2f} ')
    c += 1
print('-'*50)


'''print(produtos[0], end =' R$')
print(f'{produtos[1]:.2f}')
print(produtos[2], end =' R$')
print(f'{produtos[3]:.2f}')
print(produtos[4], end =' R$')
print(f'{produtos[5]:.2f}')'''