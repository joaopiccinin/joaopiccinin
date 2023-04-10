v1 = float(input('Qual a distância da viagem? '))
if v1<= 200:
    print('Sua viagem de {:.0f}km custará R${:.2f}'.format(v1, v1*0.50))
else:
    print('Sua viagem de {:.0f}km custará R${:.2f}'.format(v1, v1*0.45))