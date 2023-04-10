n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#calculando o maior
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#calculando o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O \033[1;31mMENOR\033[m número é \033[1;31m{}\033[m'.format(menor))
print('O \033[1;34mMAIOR\033[m número é \033[1;34m{}\033[m'.format(maior))
