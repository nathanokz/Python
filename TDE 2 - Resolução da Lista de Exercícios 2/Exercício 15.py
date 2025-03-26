a = int(input('Insira um número inteiro:'))
b = int(input('Insira outro número inteiro:'))
c = int(input('Insira mais um número inteiro'))
if a >= b and a >= c:
    if b >= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a >= b:
        print(c, a, b)
    else:
        print(c, b, a)








