vLido = []
for i in range(10):
    a = int(input('insira um numero'))
    vLido.append(a)
vPares = []
vImpares = []
for numero in vLido:
    if numero % 2 == 0:
        vPares.append(numero)
for numero in vLido:
    if numero % 2 != 0:
        vImpares.append(numero)
print(f'os valores de vLido: {vLido}')
print(f'os valores de vPares: {vPares}')
print(f'os valores de vImpares: {vImpares}')



