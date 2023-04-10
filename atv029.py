vl = float(input('Em que velocidade você estava? '))
if vl > 80:
    print('Você foi multado por ultrapassar o limite de velocidade, sua multa será de R${:.2f}'.format((vl - 80)*7))
else:
    print('Parabéns! Você estava dentro do limite de velocidade estabelecido.')