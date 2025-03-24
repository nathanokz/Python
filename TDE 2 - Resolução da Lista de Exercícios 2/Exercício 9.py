idade = int(input('Insira sua idade:'))
if idade <= 16:
    print('Não votante')
elif idade > 16 and idade < 18:
    print('Eleitor facultativo')
elif idade >= 65:
    print('Eleitor facultativo')
else:
    print('Voto obrigatório')
