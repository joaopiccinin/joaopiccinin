print('\033[7;40m-=\033[m'*20)
print('')
print('       \033[7;40mAnalisador de Triângulos\033[m')
print('')
print('\033[7;40m-=\033[m'*20)
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1<r2+r3 and r2< r3+ r1 and r3<r1+r2:
    print('\033[4;34mÉ possível formar um triângulo\033[m')
else:
    print('\033[4;31mNão é possivel formar um triângulo\033[m')