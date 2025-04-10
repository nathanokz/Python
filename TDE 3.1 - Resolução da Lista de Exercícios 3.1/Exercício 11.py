entrada = int(input('Insira um número de termos desejados:'))
contador = 2
formula = 1
while contador <= entrada:
    formula += 1 / contador
    contador += 1
print(formula)

