valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))
    c += 1
maior = max(valores)
menor = min(valores)
print(f'O maior valor é o {maior} e ele está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end =' ')
print()

print(f'O maior valor é o {menor} e ele está na posição ', end = '')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end = ' ')
