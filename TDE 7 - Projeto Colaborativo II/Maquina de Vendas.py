valoresQuantidades = [
    [1, 3.75, 2],
    [2, 3.67, 5],
    [3, 9.96, 1],
    [4, 1.25, 100],
    [5, 13.99, 2]
]

produtos = ['Coca-cola', 'Pepsi', 'Monster', 'Café', 'RedBull']

def selecionar_produto():
    contador = 0
    print('-' * 20)
    print('lista de produtos:')
    while contador < len(produtos):
        print(f'{contador} - {produtos[contador]} R${valoresQuantidades[contador][1]}')
        contador += 1
    print('-' * 20)
    produto = int(input('selecione o item desejado:'))
    return produto
produto = selecionar_produto()

def se_estiver_disponivel():
    contador = produto
    if 0 <= contador <= len(produtos):
        print(f'produto disponivel! ha {valoresQuantidades[contador][2]} unidades')
        print('-' * 20)
        disponivel = valoresQuantidades[contador][2] - 1
        return disponivel
    else:
        print('produto indisponivel')
estoque = se_estiver_disponivel()

def pagamento():
    contador = produto
    opçao = int(input('deseja comprar? 1 - sim 2 - não'))
    if opçao == 1:
        print(f'valor total: R${valoresQuantidades[contador][1]}')
        print('-' * 20)
        pagar = float(input('insira o pagamento:'))
        return pagar
    if opçao == 2:
        print('operaçao encerrada!')
pagar = pagamento()

def verificar_pagamento():
    contador = produto
    pagamento = pagar
    if  pagamento >= valoresQuantidades[contador][1] :
        print('retirando o produto...')
        print('-' * 20)
        print(f'pegue sua {produtos[contador]}')
        return print()
    else:
        print('dinheiro insuficiente! ')
suficiente = verificar_pagamento()
