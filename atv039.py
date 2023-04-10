from datetime import date
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year
id = ano - nasc
if id > 18:
    print('Você tem \033[1;4;31m{}\033[m anos, portanto deveria ter se alistado em \033[1;4;31m{}\033[m, há \033[1;4;31m{}\033[m anos atrás.'.format(id,(18 - id) + ano, id - 18))
elif id == 18:
    print('Você tem \033[1;4;34m{}\033[m anos, portando deve se alistar neste ano.'.format(id))
else:
    print('Você tem \033[1;4;32m{}\033[m anos, portanto terá de se alistar em \033[1;4;32m{}\033[m, daqui há \033[1;4;32m{}\033[m anos'.format(id,(18 - id) + ano, 18 - id))
