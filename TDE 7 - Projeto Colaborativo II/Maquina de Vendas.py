valoresQuantidades = [
    [1, 3.75, 2],
    [2, 3.67, 5],
    [3, 9.96, 1],
    [4, 1.25, 100],
    [5, 13.99, 2]
]

produtos = ['Coca-Cola', 'Pepsi', 'Monster', 'Café', 'Redbull']

dinheiro = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

def escolha_produto():
    contador = 0
    print('-' * 20)
    print('produtos disponiveis:')
    while contador < len(produtos):
        print(f'{contador} - {produtos[contador]} R${valoresQuantidades[contador][1]}')
        contador += 1
    print('-' * 20)
escolha_produto()
selecionar = int(input('selecione o produto desejado:'))

def se_estiver_disponivel():
    contador = selecionar
    if 0 <= contador < len(produtos):
        print(f'produto disponivel! ha {valoresQuantidades[contador][2]} unidades')
        print('-' * 20)
        valoresQuantidades[contador][2] -= 1
    else:
        print('produto indisponivel')
se_estiver_disponivel()
opcao = int(input('deseja comprar? 1 - sim 2 - não'))

def exibir_valor():
    contador = selecionar
    if opcao == 1:
        print(f'valor total: R${valoresQuantidades[contador][1]}')
        print('-' * 20)
    if opcao == 2:
        print('operaçao encerrada!')
exibir_valor()
pagar = float(input('insira o pagamento:'))

def verificar_pagamento():
    contador = selecionar
    comprar= pagar
    if comprar >= valoresQuantidades[contador][1]:
        print('retirando o produto...')
        print('-' * 20)
        print(f'pegue sua {produtos[contador]}')
    else:
        print('dinheiro insuficiente! ')
verificar_pagamento()

def calcular_troco():
    contador = selecionar
    troco = pagar - valoresQuantidades[contador][1]
    if troco <= 0:
        print('sem troco!')
    else:
        print(f'seu troco: {troco}')
calcular_troco()

