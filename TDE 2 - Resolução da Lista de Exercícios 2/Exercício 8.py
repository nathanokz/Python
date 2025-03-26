tempo = int(input('Insira quanto tempo você passou no estacionamento em minutos:'))
valor = 8
valor2 = 1.50
if tempo <= 60:
    print('Valor mínimo: 8 reais ')
else:
    minutosexcedentes = tempo - 60
    partes = (minutosexcedentes + 14) // 15
    valortotal = valor + (partes * valor2)
    print('Valor total é de:', valortotal, 'reais')







