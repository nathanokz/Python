dolar = 5.76
euro = 6.24
libra = 7.43
moedadesejada = 0
while moedadesejada < 1 or moedadesejada > 3:
    print('Escolha uma moeda:')
    print('1 - Dólar')
    print('2 - Euro')
    print('3 - Libra')
    moedadesejada = int(input('Insira a moeda desejada:'))
montante = float(input('Digite a quantidade da moeda desejada:'))
if moedadesejada == 1:
    if montante < 1000:
        print('Valor total:', montante * dolar * 1.05)
    else:
        print('Valor total:', montante * dolar * 1.03)
elif moedadesejada == 2:
    if montante < 1000:
        print('Valor total:', montante * euro * 1.05 )
    else:
        print('Valor total:', montante * euro * 1.03)
elif moedadesejada == 3:
    if montante < 1000:
        print('Valor total:', montante * libra * 1.05)
    else:
        print('valor total:', montante * libra * 1.03)





