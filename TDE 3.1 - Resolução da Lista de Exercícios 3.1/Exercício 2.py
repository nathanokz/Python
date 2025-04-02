contador = 1
multiplicacao = 1
numeros = []
while contador <= 3:
    entradas = int(input('Insira um número inteiro:'))
    contador += 1
    multiplicacao *= entradas
    numeros.append(entradas)
print('Valor total:', multiplicacao)
if numeros[0] + 1 == numeros[1] and numeros[0] + 2 == numeros[2]:
    print('O número é triangular')
else:
    print('O número não é triangular')
