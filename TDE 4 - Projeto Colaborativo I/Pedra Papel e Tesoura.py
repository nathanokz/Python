import random

modalidade = int(input('Selecione uma modalidade: (1) 2 Players, (2) Player x Bot e (3) Bot x Bot'))
contador = 1
placarjogada1 = 0
placarjogada2 = 0
placarempate = 0

while contador == 1:
    
    jogadas = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
   
    if modalidade == 1:
        jogada1 = int(input('Selecione uma jogada: (1) Pedra, (2) Papel e (3) Tesoura'))
        jogada2 = int(input('Selecione uma jogada: (1) Pedra, (2) Papel e (3) Tesoura'))
        if jogada1 == jogada2:
            print('Player 1 jogou', jogadas[jogada1], 'e o Player 2 jogou', jogadas[jogada2], '!' 'Empate!')
            placarempate += 1
        elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
            print('Player 1 jogou', jogadas[jogada1], 'e o Player 2 jogou', jogadas[jogada2], '!' 'Player 1 venceu!')
            placarjogada1 += 1
        else:
            print('Player 1 jogou', jogadas[jogada1], 'e o Player 2 jogou', jogadas[jogada2], '!' 'Player 2 venceu!')
            placarjogada2 += 1
   
    elif modalidade == 2:
        jogada1 = int(input('Selecione uma jogada: (1) Pedra, (2) Papel e (3) Tesoura'))
        jogadabot1 = random.randint(1, 3)
        if jogada1 == jogadabot1:
            print('Player 1 jogou', jogadas[jogada1], 'e o Bot jogou', jogadas[jogadabot1], '!' 'Empate!')
            placarempate += 1
        elif (jogada1 == 1 and jogadabot1 == 3) or (jogada1 == 2 and jogadabot1 == 1) or (jogada1 == 3 and jogadabot1 == 2):
            print('Player 1 jogou', jogadas[jogada1], 'e o Bot jogou', jogadas[jogadabot1], '!' 'Player 1 venceu!')
            placarjogada1 += 1
        else:
            print('Player 1 jogou', jogadas[jogada1], 'e o Bot jogou', jogadas[jogadabot1], '!' 'O Bot venceu!')
            placarjogada2 += 1
   
    elif modalidade == 3:
        jogadabot1 = random.randint(1, 3)
        jogadabot2 = random.randint(1, 3)
        if jogadabot1 == jogadabot2:
            print('Bot 1 jogou', jogadas[jogadabot1], 'e o Bot 2 jogou', jogadas[jogadabot2], '!' 'Empate!')
            placarempate += 1
        elif (jogadabot1 == 1 and jogadabot2 == 3) or (jogadabot1 == 2 and jogadabot2 == 1) or (jogadabot1 == 3 and jogadabot2 == 2):
            print('Bot 1 jogou', jogadas[jogadabot1], 'e o Bot 2 jogou', jogadas[jogadabot2], '!' 'Bot 1 venceu!')
            placarjogada1 += 1
        else:
            print('Bot 1 jogou', jogadas[jogadabot1], 'e o Bot 2 jogou', jogadas[jogadabot2], '!' 'Bot 2 venceu!')
            placarjogada2 += 1
    
    continuar = input('Deseja continuar? (s) Sim e (n) Não')
    if modalidade == 1:
        if continuar == 'n':
            print('Placar: Player 1 = {} pontos, Player 2 = {} pontos e Empates = {} \nObrigado por jogar! Feito por: Heitor, Hugo, João e Nathan'.format(placarjogada1, placarjogada2, placarempate))
            break
    
    if modalidade == 2:
        if continuar == 'n':
            print('Placar: Player 1 = {} pontos, Bot = {} pontos e Empates = {} \nObrigado por jogar! Feito por: Heitor, Hugo, João e Nathan'.format(placarjogada1, placarjogada2, placarempate))
            break
    
    if modalidade == 3:
        if continuar == 'n':
            print('Placar: Bot 1 = {} pontos, Bot 2 = {} pontos e Empates = {} \nObrigado por jogar! Feito por: Heitor, Hugo, João e Nathan'.format(placarjogada1, placarjogada2, placarempate))
            break
