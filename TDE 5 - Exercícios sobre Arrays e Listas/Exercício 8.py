vetor = []
for i in range(10):
    a = int(input('insira um numero'))
    vetor.append(a)
print(f'o valor maximo foi {max(vetor)}')
print(f'o valor minimo foi {min(vetor)}')
print(f'amplitude amostral: {max(vetor) - min(vetor)}')
