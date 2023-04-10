from datetime import date
c = 1
totmaior = 0
totmenor = 0
ano = date.today().year
while c < 8:
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    id = ano - nasc
    if id >= 18:
        totmaior += 1
    else:
        totmenor += 1
    c+=1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')
