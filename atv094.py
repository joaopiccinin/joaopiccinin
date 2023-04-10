dados = {}
pessoas = []

while True:
    #extraindo dados
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('''ERRO! Por favor digite apenas M ou F
    Sexo: [M/F] ''')).upper().strip()
    idade = int(input('Idade: '))

    #adicionando dados no dicionario
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade

    #colocando tudo na lista
    pessoas.append(dados.copy())

#verificando se deseja continuar
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    while op not in 'SN':
        op = str(input('''ERRO! Responda apenas S ou N 
Quer continuar? [S/N] ''')).upper().strip()
    if op == 'N':
        break
print('-='*30)

#mostrando o número de pessoas cadastradas
print(pessoas)
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')

#calculando a media de idade
media = 0
for v in pessoas:
    media += v['idade']
media = media/len(pessoas)
print(f'B) A média de idade é {media:5.2f} anos')

#listando as mulheres
print('C) Mulheres cadastradas: ', end ='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(f' {c["nome"]}', end =' ')
print()

#listando quem está acima da media de idade
print('D) Lista de pessoas que estão acima da média: ')
for c in pessoas:
    if c['idade'] > media:
        print(f'    nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}; ')
print('<<ENCERRADO>>')

