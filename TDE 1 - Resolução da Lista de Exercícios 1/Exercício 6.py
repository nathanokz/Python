#Entrada
altura = float(input('Insira a altura do cilindro:'))
raio = float(input('Insira o raio do cilindro:'))

#Processamento
pi = 3.14
formula = 2 * pi * raio * altura + 2 * pi * (raio * raio)
formula2 = formula / 3
formula3 = formula2 / 5
formula4 = formula3 * 50

#Saída
print('Valor total:', formula4, 'reais')
print('Quantidade de latas:', formula3)
