import math
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hip = math.hypot(co, ca)
print("O valor da hipotenusa é {:.2f} ".format(hip))
