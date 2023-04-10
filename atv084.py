temp = []
princ = []
mai = men = 0
while True:
    #extraindo os dados
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    #verificando qual é o maior
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp [1]
            nmai = temp[0]
        if temp [1] < men:
            men = temp[1]
            nmen = temp [0]
    #copiando os dados temporarios
    princ.append(temp[:])
    #limpando os dados temporarios após a cópia
    temp.clear()
    #opção de continuar
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Temos {len(princ)} pessoas cadastradas!')
print(f'O maior peso é {mai}Kg. Peso de ', end = '')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end = ' ')
print()
print(f'O menor peso é {men}Kg. Peso de ', end = '')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end = ' ')





