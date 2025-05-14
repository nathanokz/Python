numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(100):
    multilinhas = numeros[i // len(numeros)]
    multiculunas = numeros[i % len(numeros)]
    produto = multiculunas * multilinhas
    print(f'{multilinhas} x {multiculunas} = {produto}')
