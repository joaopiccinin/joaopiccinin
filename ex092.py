#importando biblioteca
from datetime import date

#extraindo dados
ano = date.today().year
cadastro = {'Nome': str(input('Nome: ')),
            'idade': int(input('Ano de nascimento: ')),
            'CTPS': int(input('Carteira de trabalho (0 se não tiver): '))}

#verificando se a pessoa tem carteira de trabalho
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Sálario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['Contratação'] - cadastro['idade']) + 35

#calculando a idade
cadastro['idade'] = ano - cadastro['idade']

#finalizando
print('-='*30)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')