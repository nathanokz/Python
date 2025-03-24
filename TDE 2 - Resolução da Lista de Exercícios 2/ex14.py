a = int(input('Insira um número inteiro:'))
b = int(input('Insira outro número inteiro:'))
c = int(input('Insira mais um número inteiro'))
if a > b and a > c:
    print('O maior número é:', a)
elif b > a and b > c:
    print('O maior número é:', b)
elif c > a and c > b:
    print('O maior número é:', c)

