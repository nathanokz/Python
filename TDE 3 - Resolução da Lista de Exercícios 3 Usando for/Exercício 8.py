soma = 0
for cont in range(1,11):
    entrada = int(input('Insira um número:'))
    soma += entrada
    media = soma / cont
print('Soma total: {}'.format(soma))
print('Média Aritmética: {}'.format(media))
