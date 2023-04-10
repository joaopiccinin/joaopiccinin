vog = ('a', 'e', 'i', 'o', 'u')
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis')
for p in palavras:
    print(p, end =' ')
    for letra in p:
        if letra in vog:
            print(letra, end =' ')
    print('')

