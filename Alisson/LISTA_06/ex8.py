print("Digite os valores da matriz A (4x4):")
A = []
for i in range(4):
    linha = []
    for j in range(4):
        num = int(input(f"A[{i}][{j}]: "))
        linha.append(num)
    A.append(linha)

print("\nDigite os valores da matriz B (4x4):")
B = []
for i in range(4):
    linha = []
    for j in range(4):
        num = int(input(f"B[{i}][{j}]: "))
        linha.append(num)
    B.append(linha)

SOMA = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(A[i][j] + B[i][j])
    SOMA.append(linha)

print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

print("\nMatriz SOMA (A + B):")
for linha in SOMA:
    print(linha)
