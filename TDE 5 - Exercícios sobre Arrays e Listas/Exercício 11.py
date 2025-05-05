vetor = []
for i in range(10):
    a = int(input('insira um numero'))
    vetor.append(a)
    if a < 1:
        print('valor invalido')
        break
pares = []
impares = []
for numero in vetor:
    if numero % 2 == 0:
        pares.append(numero)
    if numero % 2 != 0:
        impares.append(numero)
vetor2 = pares + impares #concatenaçao das listas
print(f'vetor modificado (pares primeiro): {vetor2}')

