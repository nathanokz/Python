import random
vetor = [random.sample(range(1,60),6)]
vetor2 =[]
vetor3 = []
for i in range(6):
    a = int(input('insira sua aposta - numeros de 1 ate 60'))
    vetor2.append(a)
for numero in vetor:
    if numero in vetor2:
        vetor3.append(numero)
print(f'aposta da mega-sena: {vetor}')
print(f'sua aposta {vetor2} voce acertou {len(vetor3)} numeros')


