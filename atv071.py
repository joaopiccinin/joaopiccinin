print('~'*30)
print('{:^30}'.format('BANCO DO JOÃO'))
print('~'*30)
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
valor = int(input('Que valor você quer sacar? '))
while True:
    if valor - 50 >= 0:
        valor -= 50
        cont50+=1
    elif valor - 20 >= 0:
        valor -= 20
        cont20+=1
    elif valor - 10 >= 0:
        valor-=10
        cont10+=1
    elif valor - 1 >= 0:
        valor-=1
        cont1 += 1
    if valor == 0:
        break
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
print('~'*30)
print('Volte sempre ao BANCO DO JOÃO! Tenha um ótimo dia!')


