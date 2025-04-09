inicio = int(input('Insira um limite inicial:'))
fim = int(input('Insira um limite final:'))
for cont in range(inicio +1 ,fim):
    if cont % 3 == 0:
        print(cont)