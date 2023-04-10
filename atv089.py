from time import sleep
#variaveis
lista = []
listat = []
nota = []
notas = []
aluno = ''
c = 0
#extraindo valores
while True:
    #lendo os dados principais
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    #adicionando os dados nas devidas listas
    listat.append(nome)
    listat.append(media)

    #notas
    nota.append(nota1)
    nota.append(nota2)

    #copiando os dados das temporarias para as fixas
    lista.append(listat[:])
    notas.append(nota[:])

    #limpando as temporarias
    listat.clear()
    nota.clear()

    #opção de continuar
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break

#layout
print('-='*30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)

for c, v in enumerate(lista):
    print(f'{c:<4}{v[0]:<10}{v[1]:>8}')
while True:
    print('-=' * 30)
    aluno = int(input('Mostrar nota de qual aluno? '))
    if aluno == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
    print(f'Notas de {lista[aluno][0]} {notas[aluno]}')







