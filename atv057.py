sexo = ''
while sexo != 'M' and sexo !='F':
    sexo = str(input('Qual o seu gênero, [M]asculino ou [F]eminino? ')).upper().strip()
    if sexo != 'M' and sexo !='F':
        print('Opção inválida, tente novamente!')
