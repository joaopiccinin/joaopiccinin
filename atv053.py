while True:
    frase = str(input('Digite uma frase: ')).upper().strip().split()
    junto = ''.join(frase)
    inverso = junto[::-1]
    if junto == inverso:
        print(f'{junto} fica {inverso}, portanto, é um palíndromo.')
    else:
        print(f'{junto} fica {inverso}, portanto, não é um palíndromo.')
    continue

