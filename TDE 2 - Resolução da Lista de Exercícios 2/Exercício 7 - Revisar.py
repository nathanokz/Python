peso = float(input('Insira se peso em quilogramas:'))
altura = float(input('Insira sua altura em metros:'))
formula = peso / altura**2
formula2 = 24.9 * altura**2
print('Seu imc é:', formula)
if formula >= 18.5 and formula <= 25:
    print('Seu imc é considerado normal')
else:
    print('Seu peso deveria ser de:', formula2, ' para seu imc ser considerado ideal')
