s = float(input('Digite o seu sálario: '))
if s >= 1250.00:
    print('Você receberá um AUMENTO de \033[1;32m10%\033[m, então seu novo salário será \033[4;1;32mR${:.2f}\033[m'.format(s*10/100+s))
else:
    print('Você reberá um AUMENTO de \033[1;34m15%\033[m, então seu novo salário será \033[4;1;34mR${:.2f}\033[m'.format(s*15/100+s))
