limite = int(input('Insira um limite inicial:'))
limite2 = int(input('Insira um limite final:'))
contador = 1
while contador <= limite:
    if contador % 3 == 0:
        print('Número', contador)
        contador = contador + 1