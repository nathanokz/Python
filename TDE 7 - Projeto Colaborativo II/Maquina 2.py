valoresQuantidades = [
    [1, 3.75, 2],
    [2, 3.67, 5],
    [3, 9.96, 1],
    [4, 1.25, 100],
    [5, 13.99, 2]
]

produtos = ['Coca-Cola', 'Pepsi', 'Monster', 'Café', 'Redbull']

while True:

    def modalidade():
        print('-' * 20)
        print('1 - modo administrador')
        print('2 - comprar')
        return int(input('escolha o modo:'))
    escolha = modalidade()

    if escolha == 1:
        def modo_administrador():
            print('-' * 20)
            modos = int(input('voce deseja 1 - cadastrar 2 - remover ou 3 - editar produtos:'))
            if modos == 1:
                novo_produto = str(input('insira o nome do produto:'))
                produtos.append(novo_produto)
                print('cadastrando produto...\nproduto cadastrado!')
                print(produtos)

            elif modos == 2:
                for i in range(len(produtos)):
                    print(f'{i} - {produtos[i]}')
                produto_remover = int(input('escolha o produto que voce deseja remover:'))
                if produto_remover == 0:
                    produtos.remove(produtos[0])
                elif produto_remover == 1:
                    produtos.remove(produtos[1])
                elif produto_remover == 2:
                    produtos.remove(produtos[2])
                elif produto_remover == 3:
                    produtos.remove(produtos[3])
                elif produto_remover == 4:
                    produtos.remove(produtos[4])
                print('removendo produto...\nproduto removido!')
                print(produtos)

            elif modos == 3:
                for i in range(len(produtos)):
                    print(f'{i} - {produtos[i]}')
                selecao_produto = int(input('qual produto voce deseja trocar o preço:'))
                novo_preco = float(input('insira o novo preço do produto:'))
                valoresQuantidades[selecao_produto][1] = novo_preco
                print('substituindo valor...\nvalor trocado com sucesso!')
        modo_administrador()

    if escolha == 2:
        def escolha_produto():
            print('-' * 20)
            print('produtos disponiveis:')
            for i in range(len(produtos)):
                print(f'{i} - {produtos[i]} R${valoresQuantidades[i][1]}')
            print('-' * 20)
            return int(input('selecione o item desejado:'))
        selecionar = escolha_produto()

        def se_estiver_disponivel(selecionar):
            if valoresQuantidades[selecionar][2] > 0:
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



