entradas = int(input('1 - 2 Players , 2 - Player x Bot e 3 - Bot x Bot \nSelecione uma modalidade:'))

if entradas == 1:
    print('Modalidade selecionada: Player x Player')
    print('Regras do jogo: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra')

    contador = 1
    while contador:
        jogadas1 = int(input('Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada:'))
        jogadas2 = int(input('Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada:'))
        placarplayer1 = 0
        placarplayer2 = 0
        if jogadas1 == 1 and jogadas2 == 2:
            print('Jogador 2 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer2 += 1
            placarplayer1 += 0
            if opcao == 2:
                    break

        if jogadas1 == 1 and jogadas2 == 3:
            print('Jogador 1 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            placarplayer2 += 0
            if opcao == 2:
                    break

        if jogadas1 == 2 and jogadas2 == 1:
            print('Jogador 1 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            placarplayer2 += 0
            if opcao == 2:
                    break

        if jogadas1 == 2 and jogadas2 == 3:
            print('Jogador 2 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer2 += 1
            placarplayer1 += 0
            if opcao == 2:
                    break

        if jogadas1 == 3 and jogadas2 == 1:
            print('Jogador 2 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer2 += 1
            placarplayer1 += 0
            if opcao == 2:
                    break

        if jogadas1 == 3 and jogadas2 == 2:
            print('Jogador 1 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            placarplayer2 += 0
            if opcao == 2:
                    break
        contador += contador
elif entradas == 2:
    print('Modalidade selecionada: Player x Bot')
elif entradas == 3:
    print('Modalidade selecionada: Bot x Bot')
else:
    print('Modalidade inválidade. Tente novamente.')

#            print('Player 1 =', placarplayer1, 'pontos','\nPlayer 2 =', placarplayer2, 'pontos' )




