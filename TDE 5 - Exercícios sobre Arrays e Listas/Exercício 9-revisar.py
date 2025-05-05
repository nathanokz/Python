vetor = []
for i in range(10):
    a = int(input('insira um numero'))
    vetor.append(a)
b = int(input('qual valor voce gostaria de verificar?'))
print(f'o numero esta na posiçao {vetor.index(b)}')

