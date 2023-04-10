n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('\033[1;32mÉ possivel formar um triângulo.\033[m')
    if n1 == n2 == n3:
        print('Será um triângulo \033[1;32mEQUILÁTERO\033[m')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 !=n2:
        print('Será um triângulo \033[1;32mISÓSCELES\033[m')
    elif n1 != n2 != n3:
        print('Será um triângulo \033[1;32mESCALENO\033[m')
else:
    print('\033[1;31mNão é possivel formar um triângulo\033[m')
