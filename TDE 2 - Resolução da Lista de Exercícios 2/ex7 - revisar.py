peso = float(input('Insira se peso em quilogramas:'))
altura = float(input('Insira sua altura em metros:'))
formula = peso / altura**2
print('Seu imc é:', formula)
if formula >= 18.5 and formula <= 25:
    print('Seu imc é considerado normal')
else:
    print('Sua massa considerada ideal é:')
