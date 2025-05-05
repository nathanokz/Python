vetor = []
for i in range(4):
    a = int(input('insira um numero'))
    vetor.append(a)
pares = []
for numero in vetor:
    if numero % 2 == 0:
        pares.append(numero)
print(f'soma dos que sao pares = {sum(pares)}')
