entrada = int(input('Insira um número inteiro:'))
contador = entrada
fatorial = 1
if entrada < 0:
    print('Não existe fatorial de número negativo')
while contador > 1:
    fatorial *= contador
    contador -= 1
print('O fatorial de:', entrada,'é igual a', fatorial)