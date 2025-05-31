valoresQuantidades = [
    [1, 3.75, 2],
    [2, 3.67, 5],
    [3, 9.96, 1],
    [4, 1.25, 100],
    [5, 13.99, 2]
]

produtos = ['Coca-Cola', 'Pepsi', 'Monster', 'Café', 'Redbull']

def escolha_produto():
    print('-' * 20)
    print('produtos disponiveis:')
    for i in range(len(produtos)):
        print(f'{i} - {produtos[i]} R${valoresQuantidades[i][1]}')
    print('-' * 20)
    return int(input('selecione o item desejado:'))
selecionar = escolha_produto()

def se_estiver_disponivel(selecionar):
    if valoresQuantidades[selecionar][1] > 0:
        if 0 <= selecionar < len(produtos):
            print(f'produto disponivel! ha {valoresQuantidades[selecionar][2]} unidades')
            print('-' * 20)
            return int(input('deseja comprar? 1 - sim 2 - nao'))
        else:
            print('produto indisponivel!')
comprar = se_estiver_disponivel(selecionar)

def pagamento(selecionar, comprar):
    if comprar == 1:
        print(f'valor total: R${valoresQuantidades[selecionar][1]}')
        print('-' * 20)
        return float(input('insira o pagamento:'))
    if comprar == 2:
        print('operaçao encerrada')
pagar = pagamento(selecionar, comprar)

def verificar_pagamento(selecionar, pagar):
    if pagar >= valoresQuantidades[selecionar][1]:
        print('retirando produto...')
        print('-' * 20)
        print(f'pegue sua {produtos[selecionar]}')
    else:
        print('dinheiro insuficiente')
verificar_pagamento(selecionar, pagar)

def calcular_troco(selecionar, pagar):
    troco = pagar - valoresQuantidades[selecionar][1]
    if troco > 0:
        print(f'seu troco: {troco}')
    else:
        print('sem troco!')
calcular_troco(selecionar, pagar)




