import random
letras = ['p', 'q','r']
valores = ['ꓥ', 'V', '->', '<->']
negativo = ['~', '']
VouF = ['V', 'F']
while True:
    print(f'Considerando que: p = {random.choice(VouF)}, q = {random.choice(VouF)} e r = {random.choice(VouF)}')
    print(f'{random.choice(letras)} {random.choice(valores)} {random.choice(negativo)} {random.choice(letras)} ')
    resultado = str(input('Qual a resposta correta:'))
