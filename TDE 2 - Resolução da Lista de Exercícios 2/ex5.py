copias = int(input('Insira o número de cópias desejadas:'))
if copias < 100:
    formula = copias * 0.25
    print('Valor total:', formula, 'reais')
else:
    formula2 = copias * 0.20
    print('Valor total:', formula2,'reais')