matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ' ))

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end ='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}.')
print(f'O maior valor da segunda coluna é {max(matriz[1])}')
print('A soma dos valores da terceira coluna é ', end='')
print(matriz[0][2] + matriz [1][2] + matriz [2][2])



