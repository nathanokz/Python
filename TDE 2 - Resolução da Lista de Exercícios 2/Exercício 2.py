nascimento = int(input('Insira seu ano de nascimento:'))
idade = 2023 - nascimento
print('Você tem', idade, 'anos')
if idade >= 18:
    print('Você pode fazer a carteira de motorista')
else:
    print('Você não pode fazer a carteira de motorista')
