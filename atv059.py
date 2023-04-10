from time import sleep
print('-='*15)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('-='*15)
op = 0
while op != "5":
    op = input('''Selecione a opção que desejar!
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa
Opção escolhida: ''')
    if op == '1':
        r = n1 + n2
        print('-='*17)
        print(f'A soma dos números é igual a {r}')
        print('-=' * 17)
    if op == '2':
        r = n1*n2
        print('-=' * 25)
        print(f'A multiplicação entre os dois números é igual a {r}')
        print('-=' * 25)
    if op == '3':
        if n1>n2:
            print('-=' * 10)
            print(f'{n1} é o maior número')
            print('-=' * 10)
        elif n1 < n2:
            print('-=' * 10)
            print(f'{n2} é o maior número')
            print('-=' * 10)
        else:
            print('-=' * 15)
            print('Os números são iguais')
            print('-=' * 15)
    if op == '4':
        print('-=' * 15)
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print('-=' * 15)
print('Encerrando...')
sleep(1)
