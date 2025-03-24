tempo = float(input('Insira o tempo em minutos que você ficou no estacionamento:'))
tempo2 = tempo - 60
preco = 8
if tempo == 60:
    print('O valor a ser pago é:', preco, 'reais')
elif tempo > 60:
    print('O valor a ser pago é:', tempo + 1.5 + 8, 'reais')





