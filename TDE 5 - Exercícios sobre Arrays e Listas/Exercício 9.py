posicao = 0
contador = 0
vetor = []
for i in range(10):
    a = int(input('insira um numero'))
    vetor.append(a)
b = int(input('qual valor voce gostaria de verificar?'))
numeroDetectado = []
for numero in vetor:
    if numero == b:
        contador += 1
        numeroDetectado.append(posicao)
    posicao += 1
print(f'o numero esta na posiçao {numeroDetectado} e aparece'
f' {contador}  vezes')

