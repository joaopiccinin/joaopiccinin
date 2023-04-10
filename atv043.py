peso = float(input('Digite o seu peso (kg): '))
alt = float(input('Digite a sua altura em (m): '))
imc = peso/alt**2
if imc < 18.5:
    print('\033[1;36mVocê está abaixo do peso ideal.\033[m')
elif imc >= 18.5 and  imc < 25:
    print('\033[1;32mVocê está no peso ideal\033[m.')
elif imc > 25 and imc <= 30:
    print('\033[1;33mVocê está com sobrepeso.\033[m')
elif imc > 30 and imc <= 40:
    print('\033[1;31mVocê está obeso, tome cuidado.\033[m')
elif imc > 40:
    print('\033[1;35mVocê está com obesidade mórbida, procure ajuda.\033[m')
print('\033[1;33mSeu IMC é {:.1f}\033[m'.format(imc))