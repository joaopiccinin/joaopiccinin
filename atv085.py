valores = [[], []]
for c in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f'Os valores pares são {sorted(valores[0])}')
print(f'Os valores impares são {sorted(valores[1])}')






'''for n in valores:
    if n % 2 == 0:
        pares.append(n)
for n in valores:
    if n % 2 != 0:
        impares.append(n)'''

'''print(f'Os números pares digitados foram: {sorted(pares)}')
print(f'Os números impares digitados foram: {sorted(impares)}')'''


