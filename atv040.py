
nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('A media do aluno {} foi de \033[1;31m{:.1f}\033[m, portanto ele está \033[1;31mreprovado!\033[m'.format(nome, media))
elif media > 5 and media < 7:
    print('A média do aluno {} foi de \033[1;33m{:.1f}\033[m, portanto ele está em \033[1;33mrecuperação!\033[m'.format(nome, media))
elif media >= 7:
    print('A média do aluno {} foi de \033[1;32m{:.1f}\033[m, portanto o aluno está \033[1;32maprovado!\033[m'.format(nome, media))