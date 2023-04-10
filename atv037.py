n1 = int(input('Digite um número apra conversão: '))
print('''Escolha uma das opções de conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3]converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('\033[1;33mO número {} convertido para BINÁRIO é igual a {}\033[m'.format(n1, bin(n1)[2:] ))
elif opção == 2:
    print('\033[1;36mO número {} convertido para OCTAL é igual a {}\033[m'.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('\033[1;34mO número {} convertido para HEXADECIMAL é igual a {}\033[m'.format(n1, hex(n1)[2:]))
else:
    print('\033[1;31mOpção inexistente, escolha uma das opções disponiveis.\033[m')