numeros = []
a = int(input('insira um numero'))
for i in range(a):
    multiplicacao = i * (i + 1) * (i + 2)
    numeros.append(multiplicacao)
    if multiplicacao == a:
        print('o numero é triangular')
        break
else:
    print('o numero não é triangular')
