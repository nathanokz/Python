contador = 1
paisA = 80000
paisB = 200000
taxaA = 1.03
taxaB = 1.015
anos = 0
while paisA <= paisB:
    paisA *= taxaA
    paisB *= taxaB
    print('----------------------------------------------------')
    print('População de A =', paisA, '\nPopulação de B =', paisB)
    print('Ano:', anos)
    anos += 1



