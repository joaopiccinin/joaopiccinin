import random
print('\033[1;32m-=\033[m'*10)
print('      \033[1;32mJOKENPÔ\033[m')
print('\033[1;32m-=\033[m'*10)
p = 'pedra'
pa = 'papel'
t = 'tesoura'
pat = [p, pa, t]
pc = random.choice(pat)
j = str(input('Escolha: pedra, papel ou tesoura: '))
if pc == p and j == p:
    print('Opa, empatamos, vamos de novo!')
elif pc == p and j == pa:
    print('Parabéns, você ganhou!')
elif pc == p and j == t:
    print('Eu ganhei!')
elif pc ==  pa and j == p:
    print('Eu ganhei!')
elif pc == pa and j == pa:
    print('Opa, empatamos, vamos de novo!')
elif pc == pa and j == t:
    print('Você ganhou!')
elif pc == t and j == p:
    print('Você ganhou!')
elif pc == t and j == pa:
    print('Eu ganhei!')
elif pc == t and j == t:
    print('Opa, empatamos, vamos de novo!')
print('Eu escolhi {}.'.format(pc))


