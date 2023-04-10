tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio','Cruzeiro',
          'Flamengo','Vasco','Chapecoense',
          'Atlético MG','Botafogo','Athletico PR','Bahia','São Paulo','Fluminense',
          'Sport','EC Vitória','Coritiba','Avaí','Ponte Preta','Atlético GO')
print('='*30)
print(f'Lista de times do brasileirão: {tabela}')
print('='*30)
print(f'Os 5 primeiros colocados: {tabela[0:5]}')
print('='*30)
print(f'Os 4 últimos colocados: {tabela[-4:]}')
print('='*30)
print(sorted(tabela))
print('='*30)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')




