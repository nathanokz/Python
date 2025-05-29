matriz = [[int(input(f"M[{a}][{b}]: ")) for b in range(4)] for a in range(4)]
vetor = [max(matriz[a][b] for a in range(4)) for b in range(4)]
media = sum(vetor) / 4

print("\nMatriz:")
for linha in matriz:
    print(linha)

print("\nVetor:", vetor)
print(f"Média: {media:.2f}")
