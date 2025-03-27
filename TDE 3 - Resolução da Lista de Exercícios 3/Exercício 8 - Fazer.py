contador = 1
soma = 0 #inicia a soma com zero
while contador < 10:
    numeros = float(input('Insira um número:'))
    contador = contador + 1
    soma += numeros #soma o valor digitado ao valor acumulado
print('Valor total', soma)
