n1 = int(input('\033[1;34mPrimeiro valor:\033[m '))
n2 = int(input('\033[1;32mSegundo valor:\033[m '))
if n1 > n2:
    print('\033[1;34mO primeiro valor é o maior.\033[m')
elif n2 > n1:
    print('\033[1;32mO segundo valor é o maior.\033[m')
else:
    print('Não existe valor maior, os dois são iguais.')