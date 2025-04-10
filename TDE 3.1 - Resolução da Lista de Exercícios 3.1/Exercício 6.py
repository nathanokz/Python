entrada = int(input('Insira o número de pessoas que vão informar a idade:'))
contador = 1
numeros = 0
soma = 0
while contador <= entrada:
    entradas = int(input('Insira sua idade:'))
    soma += entradas
    contador += 1
formula = soma / entrada
if 0 <= formula <= 25:
    print('Média da idade:', formula,'\nA turma é considerada jovem')
elif 26 <= formula <= 60:
    print('Média da idade:', formula, '\nA turma é considerada adulta')
elif formula > 60:
    print('Média da idade:', formula, '\nA turma é considerada idosa')