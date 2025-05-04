import random

paises_america_do_sul = ["argentina","bolívia","brasil","chile","colômbia","equador","guiana","paraguai","peru","suriname","uruguai","venezuela"]
palavra = random.choice(paises_america_do_sul)
letras_usuario = []
chances = 5

while True:
    for letras in palavra:
        if letras in letras_usuario:
            print(letras, end='')
        else:
            print('_', end='')
    print(f'    voce tem {chances} chances')

    jogadas = str(input('insira sua jogada:'))
    letras_usuario.append(jogadas)

    if jogadas not in palavra:
        chances -= 1

    if len(letras_usuario) == len(palavra):
        print(f'voce ganhou! a palavra era {palavra}')
        break
    elif chances == 0:
        print(f'voce perdeu! a palavra era {palavra}')
        break
    else:
        continue
