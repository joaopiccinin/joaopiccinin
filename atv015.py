km = float(input('Quantos KM o carro percorreu? '))
d = int(input('Por quantos dias o carro foi utilizado? '))
vkm = km * 0.15
vd = d * 60
vt = vkm+vd
print('Você irá pagar {:.2f}R$ por {} km rodados e {:.2f}R$ por {} dias de uso, totalizando {:.2f}R$ '.format(vkm, km, vd, d, vt))

