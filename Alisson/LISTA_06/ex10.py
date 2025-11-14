matriz = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz original:")
for linha in matriz:
    print(linha)

matriz_270 = [[matriz[j][2 - i] for j in range(3)] for i in range(3)]


print("\nMatriz girada 270°:")
for linha in matriz_270:
    print(linha)
