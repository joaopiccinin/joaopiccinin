c = 0
maior = 0
menor = 0
while c < 5:
    c += 1
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg.')
print(f'O menor peso lido foi {menor}Kg.')




