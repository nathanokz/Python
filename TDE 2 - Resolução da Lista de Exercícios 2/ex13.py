valor = float(input('Insira o valor do produto:'))
print('Opções de pagamento:')
print('1 - à vista | 2 - 2 parcelas | 3 - 3 parcelas | 4 - 4 parcelas')
opcao = int(input('Escolha uma opção de pagamento:'))
opcao1 = valor - valor * 0.08
opcao2 = valor / 2 - valor * 0.04
opcao3 = valor / 3
opcao4 = valor / 4 + valor * 0.04
if opcao == 1:
    print('Valor total:', opcao1, 'reais')
if opcao == 2:
    print('Valor total:', opcao2, 'reais por mês')
if opcao == 3:
    print('Valor total:', opcao3, 'reais por mês')
if opcao == 4:
    print('Valor total:', opcao4, 'reais por mês')





