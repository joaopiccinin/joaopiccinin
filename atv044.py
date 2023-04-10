print('\033[1;34m{:=^40}\033[m'.format(' LOJA DO JOÃO '))
valor = float(input('Digite o valor do produto: '))
print('''Escolha uma opção de pagamento: 
[1] A vista dinheiro/cheque(10% de desconto)
[2] A vista no cartão(5% de desconto)
[3] Em até 2x no cartão(preço padrão)
[4] 3x ou mais no cartão(20% de juros)''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('Você receberá \033[1;36mR${:.2f}\033[m de desconto, portanto pagará apenas \033[1;36mR${:.2f}\033[m.'.format(valor*10/100, valor - valor*10/100))
elif opção == 2:
    print('Você receberá \033[1;34mR${:.2f}\033[m de desconto, portanto pagará apenas \033[1;34mR${:.2f}\033[m.'.format(valor*5/100, valor - valor*5/100))
elif opção == 3:
    print('Você pagará o produto em duas vezes de \033[1;33mR${:.2f}\033[m.'.format(valor/2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Você terá de pagar \033[1;31m{}\033[m parcelas de \033[1;31mR${:.2f}\033[m \033[1;4mCOM JUROS\033[m, totalizando \033[1;31mR${:.2f}\033[m.'.format(parcelas, (valor + (valor*20/100))/parcelas,valor + valor*20/100 ))
else:
    print('\033[1;31mOpção inexistente, escolha uma das opções disponiveis!\033[m')