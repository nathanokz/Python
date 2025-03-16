#Entrada
produto = float(input('Insira o valor do produto:'))

#Processamento
aVista = produto - produto * 0.05
parcelado_2x = produto / 2
parcelado_3x = produto / 3 + produto * 0.05

#Saída
print('Valor a vista:', aVista, 'reais')
print('Valor em 2 vezes:', parcelado_2x, 'reais por mês')
print('Valor em 3 vezes:', parcelado_3x, 'reais por mês')