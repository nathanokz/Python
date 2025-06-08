from time import sleep

valores_e_quantidades = [
    [1, 3.75, 2],
    [2, 3.67, 5],
    [3, 9.96, 1],
    [4, 1.25, 100],
    [5, 13.99, 2],
]

produtos = ['Coca-Cola', 'Pepsi', 'Monster', 'Café', 'Redbull']

while True:

    def seleção_de_modo():
        print('-=' * 20)
        sleep(2)
        print('Bem-vindo a Máquina de Bebidas! \n1 -> Modo Administrador \n2 -> Comprar')
        return int(input('Selecione o modo desejado:'))
    escolha = seleção_de_modo()

    if escolha == 1:

        def modo_administrador():
            print('-=' * 20)
            print('Você está no modo administrador!')
            print('1 -> Cadastrar Produto \n2 -> Editar Produtor \n3 -> Remover Produto ')
            return int(input('Selecione a opção desejada:'))
        modos = modo_administrador()

        if modos == 1:
            print('-=' * 20)
            print('Você selecionou a opção cadastar produto!')
            novo_nome = str(input('Insira o nome do novo produto:'))
            novo_preço = float(input('Insira o preço do novo produto:'))
            qtd_produto = int(input('Insira a quantidade disponível do novo produto:'))
            novo_id = len(valores_e_quantidades) + 1
            print(f'Cadastrando produto...')
            sleep(2)
            print('Produto cadastrado com sucesso!')
            produtos.append(novo_nome)
            valores_e_quantidades.append([novo_id, novo_preço, qtd_produto])

        if modos == 2:
            print('-=' * 20)
            print('Você selecionou a opção editar produto!')
            for i in range (len(produtos)):
                print(f'{i} -> {produtos[i]} R$ {valores_e_quantidades[i][1]}')
            produto_id = int(input('Insira o ID do produto que você deseja editar:'))
            editar_preço = float(input('Insira o novo preço do produto:'))
            editar_qtd = int(input('Insira a nova quantidade do produto:'))
            print('Editando produto...')
            sleep(2)
            print('Produto editado com sucesso!')
            valores_e_quantidades[produto_id][1] = editar_preço
            valores_e_quantidades[produto_id][2] = editar_qtd

        if modos == 3:
            print('-=' * 20)
            print('Você selecionou a opção remover produto!')
            for i in range (len(produtos)):
                print(f'{i} -> {produtos[i]} R$ {valores_e_quantidades[i][1]}')
            remover_produto = int(input('Insira o ID do produto que você deseja remover:'))
            print('Removendo produto...')
            sleep(2)
            print('Produto removido com sucesso!')
            produtos.remove(produtos[remover_produto])

    if escolha == 2:

        def escolher_produto():
            print('-=' * 20)
            print('Você está no modo de compra!')
            for i in range (len(produtos)):
                print(f'{i} -> {produtos[i]} R$ {valores_e_quantidades[i][1]}')
            return int(input('Selecione o produto que você deseja comprar:'))
        produto_selecionado = escolher_produto()
        if produto_selecionado < 0 or produto_selecionado >= len(produtos):
                print('ID inválido! Selecione uma bebida válida!')
                continue

        def se_estiver_disponivel(produto_selecionado):
            print('-=' * 20)
            if valores_e_quantidades[produto_selecionado][2] > 0:
                for i in range (len(produtos)):
                    print(f'Você escolheu: {produtos[produto_selecionado]}! Há {valores_e_quantidades[produto_selecionado][2]} unidades!')
                    return int(input('Você deseja comprar o produto? \n1 - Sim \n2 - Não \nSelecione a opção desejada:'))
        if valores_e_quantidades[produto_selecionado][2] <= 0:
            print(f'Você escolheu: {produtos[produto_selecionado]}, porém está indisponível =(')
            continue
        deseja_comprar = se_estiver_disponivel(produto_selecionado)

        def pagamento(produto_selecionado, deseja_comprar):
            print('-=' * 20)
            if deseja_comprar == 1:
                print('Boa escolha! É uma ótima bebida!')
                print(f'O valor total é de: R$ {valores_e_quantidades[produto_selecionado][1]}')

                while True:
                    pagamento = float(input('Insira o pagamento:'))
                    if pagamento >= valores_e_quantidades[produto_selecionado][1]:
                        return pagamento
                    else:
                        print('Valor insuficiente! Tente Novamente!')

            if deseja_comprar == 2:
                print('Você pode escolher outra bebida se quiser!')
                print('Encerrando operação...')
                sleep(2)
                print('Operação encerrada!')
        fazendo_pagamento = pagamento(produto_selecionado, deseja_comprar)

        def conferindo_pagamento(produto_selecionado, deseja_comprar, fazendo_pagamento):
            print('-=' * 20)
            if fazendo_pagamento >= valores_e_quantidades[produto_selecionado][1]:
                print('Efetuando pagamento...')
                sleep(2)
                print('Pagamento efetuado com sucesso!')
                print('Retirando sua bebida...')
                sleep(2)
                print(f'Pegue seu/sua {produtos[produto_selecionado]}! \nObrigado pela preferência! Tenha um ótimo dia!')
            else:
                print('Dinheiro insuficiente =( \nVocê pode tentar outra bebida!')
        conferir_pagamento = conferindo_pagamento(produto_selecionado, deseja_comprar, fazendo_pagamento)

        #CODIGO DE TROCO CHAT GPT! ESTUDAR!

        estoque_troco = {
            10000: 2,  # R$ 100,00 → 2 unidades
            5000: 3,  # R$ 50,00
            2000: 5,  # R$ 20,00
            1000: 5,  # R$ 10,00
            500: 5,  # R$ 5,00
            200: 10,  # R$ 2,00
            100: 20,  # R$ 1,00
            50: 30,  # R$ 0,50
            25: 40,  # R$ 0,25
            10: 50,  # R$ 0,10
            5: 50,  # R$ 0,05
            1: 100  # R$ 0,01
        }

        def calcular_troco(produto_selecionado, deseja_comprar, fazendo_pagamento):
            print('-=' * 20)
            troco = fazendo_pagamento - valores_e_quantidades[produto_selecionado][1]
            cedulas_e_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
            troco_centavos = int(troco * 100 + 0.5)
            if troco > 0:
                print(f'Seu troco é: R$ {troco:.2f}')
                for valor in cedulas_e_moedas:
                    quantidade = troco_centavos // valor
                    if quantidade > 0:
                        if valor >= 100:
                            print(f'{quantidade} cédula(s) de R$ {valor // 100}')
                        else:
                            print(f'{quantidade} moeda(s) de R$ {valor / 100:.2f}')
                        troco_centavos -= quantidade * valor
                valores_e_quantidades[produto_selecionado][2] -= 1
            else:
                print('Você não tem troco!')
        dinheiro_de_troco = calcular_troco(produto_selecionado, deseja_comprar, fazendo_pagamento)
