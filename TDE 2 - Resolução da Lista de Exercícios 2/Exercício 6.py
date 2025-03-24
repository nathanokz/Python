altura = float(input('Insira sua altura:'))
sexo = int(input('Qual seu gênero? Digite: 1-masculino e 2-feminino'))
masc = 1
fem = 2
if sexo == masc:
    formula = (72 * altura) - 58
    print('Seu peso ideal é:', formula)
else:
    formula2 = (62.1 * altura) - 44.7
    print('Seu peso ideal é:', formula2)

