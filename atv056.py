c = 0
idt = 0
hmv = 0
nhv = ''
mn = 0
while c < 4:
    c += 1
    print(f'===== {c}ª pessoa =====')
    nome = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    idt += id
    sx = str(input(f'Sexo [M/F]: ')).strip().upper()
    if sx == 'M':
        if id > hmv:
            hmv = id
            nhv = nome
    if sx == 'F':
        if id < 20:
            mn += 1

print(f'A média de idade entre essas pessoas é de', idt/c)
print(f'O homem mais velho do grupo é o {nhv}, com {hmv} anos de idade. ')
print(f'Nesse grupo há {mn} mulheres com menos de 20 anos.')


'''if sx != 'M' and sx != 'F':
    print('Valor inválido, tente novamente!')
    break'''