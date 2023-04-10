def cal_area(larg=0, comp=0):
    a = larg*comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {a}m²')


l = float(input('LARGURA (m): '))
c = float(input(f'COMPRIMENTO (m): '))

cal_area(l, c)