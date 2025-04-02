contador = 1
soma = 0
pares = 0
impares = 0
numeros = []
while contador <= 5:
    entradas = int(input('Insira um número inteiro:'))
    contador += 1
    soma += entradas
    numeros.append(entradas)
    if entradas % 2 == 0:
        pares += entradas
    else:
        impares += entradas
amplitude = max(numeros) - min(numeros)
print('Valor total:', soma)
print('Soma dos pares:', pares)
print('Soma dos ímpares:', impares)
print('Amplitude amostral:', amplitude)