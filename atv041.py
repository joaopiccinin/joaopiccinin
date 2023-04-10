from datetime import date
nasc = int(input('Em que ano o atleta nasceu? '))
ano = date.today().year
id = ano - nasc
if id <=9:
    print('O atleta tem \033[1;4;36m{}\033[m anos, portanto é um atleta \033[1;4;36mMIRIM\033[m.'.format(id))
elif id > 9 and id <= 14:
    print('O atleta tem \033[1;4;34m{}\033[m anos, portanto é um atleta \033[1;4;34mINFANTIL\033[m.'.format(id))
elif id > 14 and id <=19:
    print('O atleta tem \033[1;4;32m{}\033[m anos, portanto é um atleta \033[1;4;32mJUNIOR\033[m.'.format(id))
elif id == 20:
    print('O atleta tem \033[1;4;33m{}\033[m anos, portanto é um atleta \033[1;4;33mSÊNIOR\033[m.'.format(id))
elif id > 20:
    print('O atleta tem \033[1;4;35m{}\033[m anos, portanto é um atleta \033[1;4;35mMASTER\033[m.'.format(id))