palavra = 'manalu'
letra_usuario = []
chances = 5

while True:

    for letras in palavra:
        if letras in letra_usuario:
            print(letras, end='')
        else:
            print('_', end='')
    print(f'    voce tem {chances} chances')

    jogadas = str(input('insira um letra:'))
    letra_usuario.append(jogadas)

    if jogadas not in palavra:
        chances -= 1

    if len(letra_usuario) == len(palavra):
        print('voce ganhou!')
        break
    if chances <= 0:
        print(f'voce perdeu a palavra era: {palavra}')
        break
    else:
        continue







