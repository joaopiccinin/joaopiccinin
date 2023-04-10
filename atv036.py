valor = float(input('Qual o valor da casa? '))
s = float(input('Qual é o seu sálario? '))
anos = int(input('Em quantos anos você pretende pagar? '))
pm = valor/(anos*12)
print('O valor das parcelas será de \033[;31mR${:.2f}\033[m ao mês'.format(pm))
if pm > s * 30/100:
    print('\033[1;31mEsse valor excede os 30% do seu salário,  portanto, NÃO poderemos realizar o empréstimo.\033[m')
else:
    print('\033[1;32mEsse valor não excede os 30% do seu salário, portanto, poderemos realizar o empréstimo.\033[m')
