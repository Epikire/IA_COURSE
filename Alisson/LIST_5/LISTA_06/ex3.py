matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        num = int(input(f"Digite o número da posição [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

transposta = []
for j in range(3):
    linha = []
    for i in range(2):
        linha.append(matriz[i][j])
    transposta.append(linha)

if matriz == transposta:
    print("\nA matriz é simétrica (igual à sua transposta).")
else:
    print("\nA matriz NÃO é simétrica.")
