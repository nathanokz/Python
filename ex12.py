peso = float(input('Insira seu peso em quilogramas'))
formula = peso * 2.20462262
if formula >= 161 and formula <= 168:
    print('Categoria super-médio')
elif formula >= 169 and formula <= 175:
    print('Categoria meio-pesado')
elif formula >= 176 and formula <= 200:
    print('Categoria cruzador')
elif formula >= 201:
    print('Categoria peso-pesado')
else:
    print('Categoria inferior a super-médio')

