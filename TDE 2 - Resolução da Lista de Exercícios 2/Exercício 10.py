peso = float(input('Insira seu peso:'))
altura = float(input('Insira sua altura:'))
imc = peso / altura**2
print('Seu imc é:', imc)
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está com o imc ideal')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso')
else:
    print('Você está obeso')
