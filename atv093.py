#desempenho jogador

#extraindo dados
nome = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantos jogos {nome} jogou? '))
desempenho = {'Nome': nome,
              'Jogos': jogos}
gols = []
totgol = 0

#calculando os gols do jogador
for c in range(0, jogos):
    gol = (int(input(f'Quantos gols na partida {c+1}? ')))
    desempenho['gols'] = gols
    gols.append(gol)
    totgol += gol

print('-='*30)

#finalizando
desempenho['Totgol'] = totgol
del desempenho['Jogos']
for k, v in desempenho.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

for v, c in enumerate(gols):
    print(f'-> Na partida {v+1} , fez {c} gols')
print(f'Foi um total de {totgol} gols.')