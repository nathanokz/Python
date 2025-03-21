idade = int(input('Insira sua idade:'))
if idade >= 5 and idade <= 7:
    print('Categoria infantil A')
elif idade >= 8 and idade <= 10:
    print('Categoria infantil B')
elif idade >= 11 and idade <= 13:
    print('Categoria juvenil A')
elif idade >= 14 and idade <= 17:
    print('Categoriaa juvenil B')
else:
    print('Categoria adulto')
