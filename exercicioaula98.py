import sys

#calculando primeiro digito

cpf = '111.111.111-11'

cpf_formatado = cpf.replace('.','')
cpf_formatado = cpf_formatado.replace('-','')
nove_digitos = cpf_formatado[:9]


if nove_digitos[0] * len(nove_digitos) == nove_digitos:
    print('CPF INVÁLIDO')
    sys.exit()



c = 10
soma = 0
resultado_final = 0
primeiro_digito = 0

for i in cpf_formatado:
    i = int(i)
    n = (i * c)
    soma += n
    resultado_final = soma * 10
    resultado_final = resultado_final % 11
    
    c -= 1
    if c == 1:
        break

if resultado_final > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado_final

print('Primeiro digito:', primeiro_digito)


#calculando o segundo digito

cpf = cpf + str(primeiro_digito)
cpf_formatado2 = cpf.replace('.','')
cpf_formatado2 = cpf_formatado2.replace('-','')
c = 11
soma = 0
resultado_final = 0
segundo_digito = 0

for i in cpf_formatado2:
    i = int(i)
    n = (i * c)
    soma += n
    resultado_final = soma * 10
    resultado_final = resultado_final % 11
    
    c -= 1
    if c == 1:
        break

if resultado_final > 9:
    segundo_digito = 0
else:
    segundo_digito = resultado_final

print('Segundo digito:', segundo_digito)
novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
print('CPF COMPLETO:', novo_cpf)


if novo_cpf == cpf_formatado:
    print("CPF VÁLIDO!")
else:
    print('CPF INVÁLIDO!')



